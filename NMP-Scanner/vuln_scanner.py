#!/usr/bin/env python3
"""
Network Vulnerability Scanner — Executive PDF Report Generator
Scans a target domain/IP for open ports, checks CVEs via Vulners API,
and audits SSL/TLS configuration, then outputs a formatted PDF summary.

Usage:
    python vuln_scanner.py <target> [--api-key <vulners_api_key>]

Examples:
    python vuln_scanner.py scanme.nmap.org
    python vuln_scanner.py 192.168.1.0/24
    python vuln_scanner.py 10.0.0.1 --api-key YOUR_VULNERS_KEY
"""

import argparse
import json
import re
import socket
import ssl
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional
import ipaddress
import html

import nmap
import requests

# ── ReportLab imports ──────────────────────────────────────────────────────────
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    HRFlowable,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

# ── Colour palette ─────────────────────────────────────────────────────────────
C_DARK      = colors.HexColor("#0D1117")
C_HEADER    = colors.HexColor("#161B22")
C_ACCENT    = colors.HexColor("#238636")
C_HIGH      = colors.HexColor("#DA3633")
C_MED       = colors.HexColor("#D29922")
C_LOW       = colors.HexColor("#388BFD")
C_INFO      = colors.HexColor("#8B949E")
C_WHITE     = colors.HexColor("#F0F6FC")
C_SURFACE   = colors.HexColor("#21262D")
C_BORDER    = colors.HexColor("#30363D")

SEV_COLOUR  = {"HIGH": C_HIGH, "MEDIUM": C_MED, "LOW": C_LOW, "INFO": C_INFO}
SEV_ORDER   = {"HIGH": 0, "MEDIUM": 1, "LOW": 2, "INFO": 3}


# ══════════════════════════════════════════════════════════════════════════════
# Data models
# ══════════════════════════════════════════════════════════════════════════════
@dataclass
class Finding:
    severity:     str          # HIGH / MEDIUM / LOW / INFO
    category:     str          # Port / CVE / SSL-TLS / Config
    title:        str
    description:  str
    remediation:  str
    references:   list[str] = field(default_factory=list)
    port:         Optional[int] = None
    service:      Optional[str] = None
    cvss:         Optional[float] = None


@dataclass
class HostResult:
    ip: str
    hostname: str
    os_guess: str
    open_ports: list[dict]
    findings: list[Finding]
    ssl_info: dict


@dataclass
class ScanResult:
    target_input:  str               
    scan_time:     datetime
    hosts:         list[HostResult]   
    total_findings: list[Finding]     
    scan_duration: float = 0.0


# ══════════════════════════════════════════════════════════════════════════════
# 1.  Nmap scanning configurations
# ══════════════════════════════════════════════════════════════════════════════
COMMON_PORTS = "21,22,23,25,53,80,110,111,135,139,143,389,443,445,465,587," \
               "636,993,995,1433,1521,3306,3389,5432,5900,6379,8080,8443,27017"


# ══════════════════════════════════════════════════════════════════════════════
# 2.  Vulners CVE lookup
# ══════════════════════════════════════════════════════════════════════════════
VULNERS_URL = "https://vulners.com/api/v3/burp/software/"


def query_vulners(service: str, version: str, api_key: str) -> list[dict]:
    """Return list of CVE dicts from Vulners for a given service/version."""
    if not api_key or not service or service in ("unknown", "tcpwrapped"):
        return []

    query = service if not version else f"{service} {version}"
    try:
        resp = requests.post(
            VULNERS_URL,
            json={"software": query, "version": version or "0", "type": "software",
                  "apiKey": api_key},
            timeout=10,
        )
        if resp.status_code != 200:
            return []
        data = resp.json()
        if data.get("result") != "OK":
            return []
        vulns = data.get("data", {}).get("search", [])
        return vulns[:5]          
    except Exception:
        return []


# ══════════════════════════════════════════════════════════════════════════════
# 3.  SSL / TLS audit
# ══════════════════════════════════════════════════════════════════════════════
WEAK_CIPHERS = {
    "RC4", "DES", "3DES", "EXPORT", "NULL", "ANON", "MD5",
}
DEPRECATED_PROTOS = {"SSLv2", "SSLv3", "TLSv1", "TLSv1.1"}


def audit_ssl(hostname: str, port: int = 443) -> tuple[dict, list[Finding]]:
    """Connect via TLS and return (cert_info_dict, findings_list)."""
    findings = []
    info: dict = {}

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode    = ssl.CERT_NONE

    try:
        with socket.create_connection((hostname, port), timeout=8) as raw_sock:
            with ctx.wrap_socket(raw_sock, server_hostname=hostname) as tls:
                proto  = tls.version()
                cipher = tls.cipher()          
                cert   = tls.getpeercert()

                info["protocol"]    = proto
                info["cipher"]      = cipher[0] if cipher else "?"
                info["bits"]        = cipher[2] if cipher else 0
                info["subject"]     = dict(x[0] for x in cert.get("subject", [])) if cert else {}
                info["issuer"]      = dict(x[0] for x in cert.get("issuer",  [])) if cert else {}
                info["not_after"]   = cert.get("notAfter", "") if cert else ""
                info["san"]         = [v for _, v in cert.get("subjectAltName", [])] if cert else []

                if proto in DEPRECATED_PROTOS:
                    findings.append(Finding(
                        severity    = "HIGH",
                        category    = "SSL/TLS",
                        title       = f"Deprecated TLS Protocol in Use ({proto})",
                        description = f"Port {port} negotiated {proto}, which is cryptographically broken.",
                        remediation = "Disable SSLv2, SSLv3, TLSv1.0, and TLSv1.1. Enforce TLSv1.2 as minimum.",
                        port = port, service = "HTTPS",
                    ))

                cipher_name = (cipher[0] or "").upper() if cipher else ""
                for weak in WEAK_CIPHERS:
                    if weak in cipher_name:
                        findings.append(Finding(
                            severity    = "HIGH",
                            category    = "SSL/TLS",
                            title       = f"Weak Cipher Suite Detected ({cipher[0]})",
                            description = f"The negotiated cipher '{cipher[0]}' contains a weak component ({weak}).",
                            remediation = "Configure the server's cipher suite list to allow only AEAD ciphers.",
                            port = port, service = "HTTPS",
                        ))
                        break

                if info["bits"] and info["bits"] < 128:
                    findings.append(Finding(
                        severity    = "HIGH",
                        category    = "SSL/TLS",
                        title       = f"Insufficient Cipher Key Length ({info['bits']} bits)",
                        description = "Cipher key length below 128 bits is considered insecure.",
                        remediation = "Enforce a minimum of 128-bit symmetric key length.",
                        port = port, service = "HTTPS",
                    ))

                if info["not_after"]:
                    try:
                        exp = datetime.strptime(info["not_after"], "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
                        days_left = (exp - datetime.now(timezone.utc)).days
                        if days_left < 0:
                            findings.append(Finding(
                                severity    = "HIGH",
                                category    = "SSL/TLS",
                                title       = "SSL Certificate Has Expired",
                                description = f"The certificate expired {abs(days_left)} day(s) ago.",
                                remediation = "Renew the certificate immediately.",
                                port = port, service = "HTTPS",
                            ))
                        elif days_left < 30:
                            findings.append(Finding(
                                severity    = "MEDIUM",
                                category    = "SSL/TLS",
                                title       = f"SSL Certificate Expiring Soon ({days_left} days)",
                                description = "Certificate expiry within 30 days risks service interruption.",
                                remediation = "Renew the certificate before it expires.",
                                port = port, service = "HTTPS",
                            ))
                    except ValueError:
                        pass

    except (ssl.SSLError, socket.timeout, ConnectionRefusedError, OSError) as exc:
        info["error"] = str(exc)

    return info, findings


# ══════════════════════════════════════════════════════════════════════════════
# 4.  Heuristic findings from open ports
# ══════════════════════════════════════════════════════════════════════════════
RISKY_PORTS = {
    21:    ("HIGH",   "FTP Service Exposed", "FTP transmits credentials and data in plaintext.", "Replace with SFTP/SCP."),
    23:    ("HIGH",   "Telnet Service Exposed", "Telnet is an unencrypted legacy protocol.", "Disable Telnet immediately and replace with SSH."),
    25:    ("MEDIUM", "SMTP Open Relay Potential", "Port 25 is open.", "Restrict SMTP relay to authenticated senders only."),
    135:   ("HIGH",   "RPC Endpoint Mapper Exposed", "Microsoft RPC is exposed.", "Block port 135 at the perimeter firewall."),
    139:   ("HIGH",   "NetBIOS Session Service Exposed", "NetBIOS is exposed externally.", "Block ports 137-139 at the firewall."),
    445:   ("HIGH",   "SMB Exposed to Network", "SMB on port 445 has been the attack vector for critical exploits.", "Block port 445 at the perimeter."),
    1433:  ("HIGH",   "MSSQL Database Port Exposed", "Microsoft SQL Server is directly reachable.", "Restrict access to trusted application servers only."),
    1521:  ("HIGH",   "Oracle DB Listener Exposed", "Oracle Database listener exposed publicly.", "Firewall the port to private app subnets."),
    3306:  ("HIGH",   "MySQL/MariaDB Exposed", "Database port exposed directly to the network.", "Bind MySQL to 127.0.0.1 or block external access."),
    3389:  ("HIGH",   "RDP (Remote Desktop) Exposed", "RDP is a frequent target for brute-force.", "Move RDP behind a VPN. Enable NLA."),
    5432:  ("HIGH",   "PostgreSQL Exposed", "PostgreSQL port is reachable from untrusted networks.", "Bind to a private interface and restrict access."),
    5900:  ("HIGH",   "VNC Service Exposed", "VNC provides graphical remote access with weak authentication.", "Tunnel VNC over SSH or a VPN."),
    6379:  ("HIGH",   "Redis Exposed Without Authentication", "Redis exposed publicly can allow unauthenticated data access.", "Bind Redis to 127.0.0.1 and enable a password."),
    27017: ("HIGH",   "MongoDB Exposed", "MongoDB open to the internet has led to mass data breaches.", "Enable MongoDB authentication and firewall it."),
    8080:  ("LOW",    "Alternate HTTP Port Open", "Non-standard HTTP port in use.", "Verify this service is intentional and hardened."),
}


def port_findings(open_ports: list[dict]) -> list[Finding]:
    findings = []
    for p in open_ports:
        port = p["port"]
        if port in RISKY_PORTS:
            sev, title, desc, remed = RISKY_PORTS[port]
            findings.append(Finding(
                severity    = sev,
                category    = "Port/Service",
                title       = title,
                description = desc,
                remediation = remed,
                port        = port,
                service     = p["service"],
            ))
    return findings


# ══════════════════════════════════════════════════════════════════════════════
# 5.  Vulners CVE → Findings Conversion
# ══════════════════════════════════════════════════════════════════════════════
def cve_findings(open_ports: list[dict], api_key: str) -> list[Finding]:
    findings = []
    for p in open_ports:
        service = p.get("service", "")
        version = p.get("version", "")
        vulns   = query_vulners(service, version, api_key)
        for v in vulns:
            src   = v.get("_source", {})
            cvss  = src.get("cvss", {}).get("score", 0.0)
            cve_id = src.get("id", "N/A")
            title  = src.get("title", cve_id)

            if cvss >= 7.0:
                sev = "HIGH"
            elif cvss >= 4.0:
                sev = "MEDIUM"
            else:
                sev = "LOW"

            findings.append(Finding(
                severity    = sev,
                category    = "CVE",
                title       = f"{cve_id}: {title[:80]}",
                description = src.get("description", "No description available.")[:300],
                remediation = "Apply the vendor patch or upgrade to a fixed version.",
                port        = p["port"],
                service     = service,
                cvss        = cvss,
                references  = [f"https://vulners.com/{cve_id}"],
            ))
    return findings


# ══════════════════════════════════════════════════════════════════════════════
# 6.  Target Resolution & Scan Orchestration
# ══════════════════════════════════════════════════════════════════════════════
def parse_and_resolve_targets(target_str: str) -> list[str]:
    target_str = target_str.strip()
    try:
        network = ipaddress.ip_network(target_str, strict=False)
        return [str(network)]
    except ValueError:
        pass
    try:
        socket.gethostbyname(target_str)
        return [target_str]
    except socket.gaierror:
        return [target_str]


def scan(target_input: str, vulners_api_key: str = "") -> ScanResult:
    t0 = datetime.now(timezone.utc)
    targets = parse_and_resolve_targets(target_input)
    
    if not targets:
        print("[!] No valid targets found.")
        return ScanResult(target_input, t0, [], [])

    print(f"[*] Initializing network scan over scope: {targets[0]}")
    nm = nmap.PortScanner()
    try:
        nm.scan(
            hosts=targets[0],
            ports=COMMON_PORTS,
            arguments="-sV --script=banner -T4 --open",
            sudo=False,
        )
    except nmap.PortScannerError as exc:
        print(f"[!] Nmap execution error: {exc}")
        return ScanResult(target_input, t0, [], [])

    discovered_hosts = []
    global_findings = []

    for host_ip in nm.all_hosts():
        print(f"[*] Processing discovered host: {host_ip}")
        hostname = nm[host_ip].hostname() or host_ip
        
        os_guess = "Unknown"
        try:
            osmatch = nm[host_ip].get("osmatch", [])
            if osmatch:
                os_guess = osmatch[0].get("name", "Unknown")
        except Exception:
            pass

        host_ports = []
        for proto in nm[host_ip].all_protocols():
            for port in sorted(nm[host_ip][proto].keys()):
                info = nm[host_ip][proto][port]
                if info.get("state") == "open":
                    raw_banner = info.get("script", {}).get("banner", "")
                    clean_banner = html.escape(raw_banner).replace("\n", " ").replace("\r", "")
                    
                    host_ports.append({
                        "port":    port,
                        "proto":   proto,
                        "service": info.get("name", "unknown"),
                        "version": html.escape((info.get("product", "") + " " + info.get("version", "")).strip()),
                        "state":   info.get("state"),
                        "banner":  clean_banner,
                    })

        host_findings = port_findings(host_ports)

        if vulners_api_key:
            print(f"   [-] Querying Vulners CVEs for {host_ip}...")
            host_findings += cve_findings(host_ports, vulners_api_key)

        host_ssl_info = {}
        https_ports = [p["port"] for p in host_ports 
                       if p["service"] in ("https", "ssl", "http-alt") or p["port"] in (443, 8443)]
        
        for port in https_ports:
            print(f"   [-] Auditing SSL/TLS on {host_ip}:{port}...")
            info, ssl_findings = audit_ssl(host_ip, port)
            host_ssl_info[port] = info
            host_findings += ssl_findings

        discovered_hosts.append(HostResult(
            ip=host_ip, hostname=hostname, os_guess=os_guess,
            open_ports=host_ports, findings=host_findings, ssl_info=host_ssl_info
        ))
        global_findings.extend(host_findings)

    seen = set()
    unique_findings = []
    for f in global_findings:
        key = (f.title, f.port, f.description[:50])
        if key not in seen:
            seen.add(key)
            unique_findings.append(f)
            
    unique_findings.sort(key=lambda f: SEV_ORDER.get(f.severity, 99))
    duration = (datetime.now(timezone.utc) - t0).total_seconds()

    return ScanResult(
        target_input=target_input, scan_time=t0,
        hosts=discovered_hosts, total_findings=unique_findings, scan_duration=duration
    )


# ══════════════════════════════════════════════════════════════════════════════
# 7.  PDF Styles Helper & Report Generator
# ══════════════════════════════════════════════════════════════════════════════
def _styles():
    def ps(name, **kw):
        return ParagraphStyle(name, **kw)

    return {
        "cover_title": ps("cover_title", fontSize=28, textColor=C_WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER, leading=34),
        "cover_sub": ps("cover_sub", fontSize=13, textColor=C_INFO, fontName="Helvetica", alignment=TA_CENTER, leading=18),
        "section": ps("section", fontSize=14, textColor=C_WHITE, fontName="Helvetica-Bold", leading=20, spaceBefore=18, spaceAfter=6),
        "body": ps("body", fontSize=9, textColor=C_WHITE, fontName="Helvetica", leading=14, spaceAfter=4),
        "small": ps("small", fontSize=8, textColor=C_INFO, fontName="Helvetica", leading=12),
        "label": ps("label", fontSize=8, textColor=C_WHITE, fontName="Helvetica-Bold", leading=12),
        "remed": ps("remed", fontSize=8.5, textColor=colors.HexColor("#7EE787"), fontName="Helvetica", leading=13),
        "footer": ps("footer", fontSize=7, textColor=C_INFO, fontName="Helvetica", alignment=TA_CENTER),
    }


def build_pdf(result: ScanResult, output_path: str):
    st = _styles()
    doc = SimpleDocTemplate(
        output_path, pagesize=A4,
        leftMargin=1.8*cm, rightMargin=1.8*cm, topMargin=1.5*cm, bottomMargin=1.5*cm,
        title="Vulnerability Assessment Executive Summary", author="vuln_scanner.py",
    )

    W = A4[0] - 3.6 * cm   
    story = []

    story.append(Spacer(1, 1.5 * cm))
    story.append(Paragraph("VULNERABILITY ASSESSMENT", st["cover_title"]))
    story.append(Paragraph("Multi-Host Infrastructure Summary", st["cover_sub"]))
    story.append(Spacer(1, 0.4 * cm))
    story.append(HRFlowable(width=W, color=C_ACCENT, thickness=2))
    story.append(Spacer(1, 0.4 * cm))

    high_c = sum(1 for f in result.total_findings if f.severity == "HIGH")
    med_c  = sum(1 for f in result.total_findings if f.severity == "MEDIUM")
    low_c  = sum(1 for f in result.total_findings if f.severity == "LOW")
    info_c = sum(1 for f in result.total_findings if f.severity == "INFO")
    total_ports = sum(len(h.open_ports) for h in result.hosts)

    meta_data = [
        ["Target Scope", result.target_input, "Active Hosts Found", str(len(result.hosts))],
        ["Scan Date", result.scan_time.strftime("%Y-%m-%d %H:%M UTC"), "Duration", f"{result.scan_duration:.1f}s"],
        ["Total Open Ports", str(total_ports), "Aggregated Risks", f"H: {high_c} | M: {med_c} | L: {low_c} | I: {info_c}"],
    ]
    meta_table = Table(meta_data, colWidths=[3.2*cm, 5.6*cm, 3.2*cm, 5.3*cm])
    meta_table.setStyle(TableStyle([
        ("BACKGROUND",  (0, 0), (-1, -1), C_SURFACE),
        ("BACKGROUND",  (0, 0), (0, -1), C_HEADER),
        ("BACKGROUND",  (2, 0), (2, -1), C_HEADER),
        ("TEXTCOLOR",   (0, 0), (-1, -1), C_WHITE),
        ("FONTNAME",    (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME",    (2, 0), (2, -1), "Helvetica-Bold"),
        ("FONTSIZE",    (0, 0), (-1, -1), 8.5),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [C_SURFACE, C_HEADER]),
        ("GRID",        (0, 0), (-1, -1), 0.5, C_BORDER),
        ("VALIGN",      (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 0.5 * cm))

    story.append(Paragraph("RISK MATRIX SUMMARY", st["section"]))
    story.append(HRFlowable(width=W, color=C_BORDER, thickness=0.5))
    story.append(Spacer(1, 0.2 * cm))

    bar_data = [["HIGH", "MEDIUM", "LOW", "INFO"], [str(high_c), str(med_c), str(low_c), str(info_c)]]
    bar_table = Table(bar_data, colWidths=[W/4]*4, rowHeights=[0.6*cm, 0.9*cm])
    bar_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), C_HIGH), ("BACKGROUND", (1, 0), (1, -1), C_MED),
        ("BACKGROUND", (2, 0), (2, -1), C_LOW),  ("BACKGROUND", (3, 0), (3, -1), C_INFO),
        ("TEXTCOLOR", (0, 0), (-1, -1), C_WHITE), ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 8), ("FONTSIZE", (0, 1), (-1, 1), 18), ("ALIGN", (0, 0), (-1, -1), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(bar_table)
    story.append(Spacer(1, 0.5 * cm))

    story.append(Paragraph("HOST ENUMERATION MATRIX", st["section"]))
    story.append(HRFlowable(width=W, color=C_BORDER, thickness=0.5))
    story.append(Spacer(1, 0.2 * cm))

    if result.hosts:
        host_rows = [[Paragraph("Host IP Address", st["label"]), Paragraph("System Hostname", st["label"]), Paragraph("Ports", st["label"]), Paragraph("OS Match", st["label"])]]
        for h in result.hosts:
            host_rows.append([Paragraph(h.ip, st["body"]), Paragraph(h.hostname, st["body"]), Paragraph(str(len(h.open_ports)), st["body"]), Paragraph(h.os_guess, st["small"])])
        ht_tbl = Table(host_rows, colWidths=[3.5*cm, 4.5*cm, 1.5*cm, W-9.5*cm])
        ht_tbl.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), C_HEADER), ("ROWBACKGROUNDS", (0, 1), (-1, -1), [C_SURFACE, C_DARK]),
            ("GRID", (0, 0), (-1, -1), 0.4, C_BORDER), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]))
        story.append(ht_tbl)

    for sev_level in ("HIGH", "MEDIUM", "LOW", "INFO"):
        group = [f for f in result.total_findings if f.severity == sev_level]
        if not group:
            continue
        story.append(Spacer(1, 0.4 * cm))
        story.append(Paragraph(f"{sev_level} SEVERITY VULNERABILITIES ({len(group)})", st["section"]))
        story.append(HRFlowable(width=W, color=SEV_COLOUR[sev_level], thickness=1.5))
        story.append(Spacer(1, 0.2 * cm))

        for i, finding in enumerate(group, 1):
            title_str = f"{i}. {finding.title}" + (f" [Port {finding.port}]" if finding.port else "") + (f" (CVSS {finding.cvss:.1f})" if finding.cvss else "")
            title_para = Paragraph(title_str, ParagraphStyle("find_title", fontSize=10, textColor=SEV_COLOUR[sev_level], fontName="Helvetica-Bold", leading=14))
            find_data = [
                [title_para, ""],
                [Paragraph("<b>Category:</b>", st["label"]), Paragraph(finding.category, st["body"])],
                [Paragraph("<b>Description:</b>", st["label"]), Paragraph(finding.description, st["body"])],
                [Paragraph("<b>Remediation:</b>", st["label"]), Paragraph(finding.remediation, st["remed"])],
            ]
            ft = Table(find_data, colWidths=[2.8*cm, W-2.8*cm])
            ft.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), C_HEADER), ("BACKGROUND", (0, 1), (-1, -1), C_SURFACE), ("SPAN", (0, 0), (1, 0)),
                ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, -1), (-1, -1), 0.5, C_BORDER),
                ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]))
            story.append(ft)
            story.append(Spacer(1, 0.2 * cm))

    has_ssl_data = any(h.ssl_info for h in result.hosts)
    if has_ssl_data:
        story.append(PageBreak())
        story.append(Paragraph("SSL / TLS CERTIFICATE CONFIGURATION LOGS", st["section"]))
        story.append(HRFlowable(width=W, color=C_BORDER, thickness=0.5))
        story.append(Spacer(1, 0.2 * cm))

        for host in result.hosts:
            for port, info in host.ssl_info.items():
                story.append(Paragraph(f"Host Verification: <b>{host.ip}</b> (Port {port})", st["body"]))
                if "error" in info:
                    story.append(Paragraph(f"TLS handshaking negotiation dropped: {info['error']}", st["small"]))
                    continue
                rows = [
                    ["Negotiated Protocol", info.get("protocol", "?")], ["Cipher Suite In Use", info.get("cipher", "?")],
                    ["Symmetric Key Length", f"{info.get('bits', '?')} bits"], ["Expiration Valid Until", info.get("not_after", "?")],
                    ["Subject Common Name", info.get("subject", {}).get("commonName", "?")], ["Issuer Authority", info.get("issuer", {}).get("organizationName", "?")],
                ]
                tbl = Table([[Paragraph(r[0], st["label"]), Paragraph(str(r[1]), st["body"])] for r in rows], colWidths=[4*cm, W-4*cm])
                tbl.setStyle(TableStyle([
                    ("ROWBACKGROUNDS", (0, 0), (-1, -1), [C_HEADER, C_SURFACE]), ("GRID", (0, 0), (-1, -1), 0.4, C_BORDER),
                    ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ]))
                story.append(tbl)
                story.append(Spacer(1, 0.4 * cm))

    story.append(Spacer(1, 0.8 * cm))
    story.append(HRFlowable(width=W, color=C_BORDER, thickness=0.5))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph("This report was generated automatically by vuln_scanner.py state telemetry.", st["footer"]))

    def dark_background(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(C_DARK)
        canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(C_INFO)
        canvas.drawCentredString(A4[0] / 2, 0.8 * cm, f"Page {doc.page}  |  vuln_scanner.py  |  {datetime.now(timezone.utc).strftime('%Y-%m-%d')}")
        canvas.restoreState()

    doc.build(story, onFirstPage=dark_background, onLaterPages=dark_background)
    print(f"[+] PDF report written to: {output_path}")


# ══════════════════════════════════════════════════════════════════════════════
# 8.  CLI entry-point
# ══════════════════════════════════════════════════════════════════════════════
def main():
    parser = argparse.ArgumentParser(description="Network Vulnerability Scanner → Executive PDF Report")
    parser.add_argument("target", help="Domain, IP address, or CIDR range (e.g., 127.0.0.1)")
    parser.add_argument("--api-key", default="", metavar="VULNERS_KEY", help="Vulners.com API key for CVE lookups")
    parser.add_argument("--output", default="", metavar="FILE", help="Output PDF path")
    args = parser.parse_args()

    target = args.target.strip()
    out = args.output or f"{re.sub(r'[^a-zA-Z0-9_.-]', '_', target)}_assessment_report.pdf"

    print(f"\n{'='*60}")
    print(f"  Network Infrastructure Vulnerability Scanner")
    print(f"  Target Scope : {target}")
    print(f"  Output PDF   : {out}")
    print(f"{'='*60}\n")

    result = scan(target, vulners_api_key=args.api_key)
    
    if result.hosts:
        build_pdf(result, out)
        print(f"\n{'='*60}")
        print(f"  Scan complete — Analyzed {len(result.hosts)} host(s) with {len(result.total_findings)} finding(s)")
        print(f"  Report Generated: {out}")
        print(f"{'='*60}\n")
    else:
        print("[!] Execution terminated: No network assets were reachable.")

if __name__ == "__main__":
    main()