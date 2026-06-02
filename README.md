# Cybersecurity Portfolio

*This repository shall act as a space for me to keep track of the various notes and assignments given throughout my journey in learning cybersecurity. Notes from each course will be updated as I go through Google's Cybersecurity Course. Additionally, the course's portfolio assignments will also be added into this repository eventually as well.*

---
## Personal Projects!
### Network Vulnerability Assessment Scanner and Report Generator
The [NMP Scanner](NMP-Scanner/NMP-Scanner.md) is a lightweight, automated infrastructure reconnaissance and security auditing tool written in Python. This tool combines rapid network port scanning via **Nmap** with remote **SSL/TLS** configuration audits and threat intelligence lookups via the *Vulners API* to aggregate point-in-time telemetry into a polished, modern, dark-themed executive PDF report.
## 01 · Security Audits & Compliance

**Skills gained:** Conducting internal security audits, evaluating controls against compliance frameworks (PCI DSS, GDPR, SOC), identifying gaps in administrative, technical, and physical controls, and producing structured audit reports.

Working through these exercises built a practical understanding of how organizations assess their security posture. I learned to distinguish between control types — preventative, corrective, detective, and deterrent — and apply them to real business contexts. Mapping findings to compliance standards like GDPR and PCI DSS made abstract regulation feel concrete and actionable.

| File | Description |
|---|---|
| [controls-and-compliance-checklist.md](01-security-audits/controls-and-compliance-checklist.md) | Audit of Botium Toys against PCI DSS, GDPR, and SOC standards |
| [security-risk-assessment-report.md](01-security-audits/security-risk-assessment-report.md) | Hardening recommendations including MFA, password policy, and port filtering |

---

## 02 · Network Security

**Skills gained:** Analyzing network traffic using tcpdump and Wireshark, identifying attack types from packet data, writing incident reports for network-layer events, and understanding DNS/ICMP/TCP/UDP protocol behavior under attack conditions.

Network traffic analysis was one of the most hands-on areas of the course. Reading log files and tracing attack paths through protocol layers gave me a much clearer picture of how DoS attacks, SYN floods, and DNS failures actually manifest in the data. Writing the incident reports sharpened my ability to communicate technical findings clearly.

| File | Description |
|---|---|
| [cybersecurity-incident-report-dos.md](02-network-security/cybersecurity-incident-report-dos.md) | SYN flood DoS attack analysis using TCP three-way handshake logs |
| [cybersecurity-incident-report-network-traffic.md](02-network-security/cybersecurity-incident-report-network-traffic.md) | DNS/ICMP traffic analysis identifying unreachable port 53 |
| [security-incident-report.md](02-network-security/security-incident-report.md) | Brute force + malware redirect attack documented via HTTP traffic logs |

---

## 03 · Linux & SQL

**Skills gained:** Managing file permissions in Linux using `chmod` and `ls -la`, reading and interpreting permission strings, filtering and querying databases with SQL using `WHERE`, `AND`, `OR`, `NOT`, and `LIKE` operators, and writing Python scripts for file-based automation.

This section covered tools that analysts use daily. Linux permission management and SQL filtering felt unfamiliar at first but became intuitive through repetition. The Python exercise tied the scripting skills together by automating a real-world IP allowlist update workflow.

| File | Description |
|---|---|
| [file-permissions-in-linux.md](03-linux-and-sql/file-permissions-in-linux.md) | Auditing and updating file/directory permissions in a Linux environment |
| [apply-filters-to-sql-queries.md](03-linux-and-sql/apply-filters-to-sql-queries.md) | SQL queries to investigate login attempts and filter employee records |
| [algorithm-for-file-updates-in-python.md](03-linux-and-sql/algorithm-for-file-updates-in-python.md) | Python algorithm to update an IP allowlist by removing flagged addresses |

---

## 04 · Incident Response

**Skills gained:** Applying the NIST Incident Response lifecycle (Identify, Protect, Detect, Respond, Recover), documenting incidents using the 5 W's framework, triaging phishing alerts with SIEM tools and VirusTotal, and maintaining an incident handler's journal.

Incident response requires both speed and structure. These exercises trained me to move quickly through the stages of a response while keeping documentation thorough enough to be useful after the fact. The journal format made it easy to track patterns across multiple incidents over time.

| File | Description |
|---|---|
| [incident-handlers-journal.md](04-incident-response/incident-handlers-journal.md) | Multi-entry journal covering ransomware, phishing, and data theft incidents |
| [incident-report-analysis.md](04-incident-response/incident-report-analysis.md) | NIST CSF-based analysis of a DoS attack with Protect/Detect/Respond/Recover plan |
| [alert-ticket.md](04-incident-response/alert-ticket.md) | Phishing alert triage using VirusTotal and file hash verification |

---

## 05 · Asset & Risk Management

**Skills gained:** Performing risk assessments using likelihood and severity scoring, building risk registers, evaluating physical and digital asset threats, analyzing access control weaknesses, and applying least privilege principles.

Risk management is about making informed decisions under uncertainty. These exercises taught me to think like both a defender and an attacker — identifying not just what could go wrong, but how likely it is and what the impact would be. The access control and data leak scenarios highlighted how often security failures are process failures, not just technical ones.

| File | Description |
|---|---|
| [risk-register.md](05-asset-and-risk-management/risk-register.md) | Risk register for a bank, scoring likelihood and severity across five threat scenarios |
| [vulnerability-assessment-report.md](05-asset-and-risk-management/vulnerability-assessment-report.md) | Three-month assessment of a MySQL server using NIST SP 800-30 |
| [access-control-worksheet.md](05-asset-and-risk-management/access-control-worksheet.md) | Investigation of unauthorized payroll access by an expired contractor account |
| [data-leak-worksheet.md](05-asset-and-risk-management/data-leak-worksheet.md) | Least privilege failure analysis mapped to NIST SP 800-53 AC-6 |
| [parking-lot-usb-exercise.md](05-asset-and-risk-management/parking-lot-usb-exercise.md) | Attacker mindset exercise analyzing risks of a found USB device |

---

## 06 · Threat Modeling

**Skills gained:** Applying the PASTA (Process for Attack Simulation and Threat Analysis) framework, decomposing applications into threat surfaces, identifying relevant threats and vulnerabilities for a given business context, and producing risk-ranked remediation recommendations.

Threat modeling sits at the intersection of technical and business thinking. The PASTA framework provided a structured way to work from business objectives all the way down to specific attack vectors. Going through this process for a consumer-facing app made the value of proactive security planning very clear.

| File | Description |
|---|---|
| [pasta-worksheet.md](06-threat-modeling/pasta-worksheet.md) | PASTA threat model for a sneaker e-commerce app covering all 7 stages |

---

*Certificate issued by Google via Coursera.*
