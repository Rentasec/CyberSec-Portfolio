# Network Vulnerability Scanner & PDF Report Generator

A lightweight, automated infrastructure reconnaissance and security auditing tool written in Python. This tool combines rapid network port scanning via **Nmap** with remote **SSL/TLS configuration audits** and threat intelligence lookups via the **Vulners API** to aggregate point-in-time telemetry into a polished, modern, dark-themed executive PDF report.

Designed for security enthusiasts and system administrators looking to perform rapid multi-host network discovery and asset hardening from a single command-line interface.

---

## 🚀 Key Features

* **Multi-Host & Subnet Mapping:** Natively accepts domains, single IP targets, or wide CIDR notation scopes (e.g., `192.168.1.0/24`) without crashing structural socket connection pipelines.
* **Passive Operating System & Service Fingerprinting:** Discovers alive assets, identifies running services, and securely captures raw software banners without needing administrative privileges (`sudo`).
* **Heuristic Risk Identification:** Automatically flags common risky perimeter entries, legacy cleartext protocols (like FTP or Telnet), and exposed critical database listener ports.
* **SSL/TLS Infrastructure Audit:** Performs automated diagnostic handshakes on secure ports to identify deprecated protocols (SSLv2/v3, TLS 1.0/1.1), weak cipher suites (RC4, 3DES), short symmetric key lengths, or expiring/expired certificates.
* **Threat Intelligence Matching (Optional):** Correlates software service versions dynamically against the **Vulners database API** to extract real-time CVE entries, exploit links, and CVSS severity metrics.
* **Executive-Ready Reports:** Employs a robust **ReportLab** backend to map all discoveries into a visually striking, beautifully formatted dark-mode PDF document complete with dynamic risk matrix charts and vulnerability category summaries.

---

## 🛠️ Installation & Setup

### 1. System Prerequisite (Nmap)
This Python script functions as a wrapper and coordinator around the core Nmap application. The Nmap binary must be installed on your host system:
* **Windows:** Download and run the installer from the [Official Nmap Download Page](https://nmap.org/download.html).
* **Linux (Debian/Ubuntu):** `sudo apt update && sudo apt install nmap`
* **macOS:** `brew install nmap`

> **Note for Windows users:** Ensure you restart your terminal after installation so the binary is registered to your system environment PATH.

### 2. Python Packages
Install the required dependency libraries using pip:
```bash
pip install python-nmap requests reportlab
```

---

## 💻 Usage
Run the script from your terminal by providing a target scope. The script automatically determines whether you're scanning a single machine or an entire network subnet.

### Basic Network Scan
```bash
python vuln_scanner.py 192.168.1.1
```
### Full Multi-Host Subnet Scan
Bash
python vuln_scanner.py 192.168.1.0/24

### Deep Vulnerability Scan with Vulners API Key
To query exact application versions for known vulnerabilities (CVEs), feed your API key into the command line argument:
```bash
python vuln_scanner.py scanme.nmap.org --api-key YOUR_VULNERS_API_KEY
```
### Specifying a Custom Output Destination
```bash
python vuln_scanner.py 127.0.0.1 --output home_test_audit.pdf
```

---

## 📊 Report Architecture
The report is systematically sectioned to bridge raw technical findings with clear executive highlights:

* **Target Meta-Data Block:** Tracks scan date, duration, target scope limits, and live host counts.

* **Global Risk Matrix Summary:** A high-level visual color-blocked grid aggregating criticalities (HIGH, MEDIUM, LOW, INFO) to give an immediate posture overview.

* **Host Enumeration Matrix:** A quick-reference inventory mapping out exactly which IPs are alive, their hostnames, detected ports, and best-guess OS.

* **Detailed Findings Panels:** Granular deep-dives into detected risks complete with customized remediation actions, software version descriptions, and references.

* **Cryptographic Configuration Logs:** Advanced tables mapping SSL/TLS handshakes, negotiated cipher strings, bit-lengths, common names, and valid certificate dates.

---

## ⚖️ Disclaimer
*This tool is intended strictly for authorized security auditing, network troubleshooting, and educational purposes. Ensure you have explicit permission from the asset owner before executing scans against any network infrastructure.*
