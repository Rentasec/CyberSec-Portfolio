# CyberSec Course 2 — Condensed Notes
*Security Domains, Risk Management, Frameworks, Audits, SIEM & Playbooks*

---

## 1. The 8 CISSP Security Domains

| Domain | Focus |
|---|---|
| **1. Security & Risk Management** | Security goals, compliance, business continuity, ethics, InfoSec processes (incident response, vuln management, cloud/app security) |
| **2. Asset Security** | Managing storage, maintenance, retention, and destruction of physical and digital assets; backups and recovery planning |
| **3. Security Architecture & Engineering** | Tools, systems, and processes to protect data; shared responsibility model; design principles (see below) |
| **4. Communication & Network Security** | Securing physical networks, wireless, remote/cloud communications; network access controls |
| **5. Identity & Access Management (IAM)** | Authenticating user identities and authorizing access; principle of least privilege |
| **6. Security Assessment & Testing** | Pen testing, security audits, data collection/analysis, validating user permissions |
| **7. Security Operations** | Incident investigation, prevention, IDS, SIEM, log management, playbooks, forensics |
| **8. Software Development Security** | Integrating security into every phase of the SDLC; app security testing, QA, pen testing |

### Domain 3 — Key Design Principles
Threat modeling, Least privilege, Defense in depth, Fail securely, Separation of duties, Keep it simple, Zero trust, Trust but verify

---

## 2. Risk Management

**Asset** — anything of value to an organization (digital: SSNs, bank accounts; physical: servers, office spaces).

### Risk Strategies
| Strategy | Description |
|---|---|
| **Acceptance** | Accept the risk to avoid disrupting business continuity |
| **Avoidance** | Create a plan to eliminate the risk entirely |
| **Transference** | Hand the risk off to a third party (e.g. insurance) |
| **Mitigation** | Reduce the impact of a known risk |

### Threat vs. Risk vs. Vulnerability
- **Threat** — event or circumstance that can negatively impact assets (e.g. insider threats, APTs)
- **Risk** — likelihood that a threat will impact confidentiality, integrity, or availability
- **Vulnerability** — weakness that can be exploited by a threat

### Risk Factors
- External risk, Internal risk, Legacy systems, Multiparty/vendor risk, Software compliance failures

### Notable Vulnerabilities
| Vulnerability | Description |
|---|---|
| **ProxyLogon** | Pre-auth exploit on Microsoft Exchange; enables remote code execution |
| **ZeroLogon** | Flaw in Windows Netlogon; allows identity spoofing |
| **Log4Shell** | Remote code execution via Log4j; affects internet-connected devices |
| **PetitPotam** | Windows NTLM theft; allows attacker to hijack authentication requests |
| **Security logging failures** | Insufficient monitoring lets attackers operate undetected |
| **Server-side request forgery (SSRF)** | Tricks server into accessing backend resources; enables data theft |

> Patch promptly — the sooner a vulnerability is mitigated, the less exposure an org faces.

---

## 3. CIA Triad

The three pillars of cybersecurity used to design systems and policies:

- **Confidentiality** — Only authorized users can access specific data. Enforced via least privilege.
- **Integrity** — Data is accurate, authentic, and unaltered. Enforced via cryptography and encryption.
- **Availability** — Data is accessible to authorized users when needed. Enforced via access controls and uptime practices.

---

## 4. Frameworks & Controls

### Key Frameworks
| Framework | Purpose |
|---|---|
| **NIST CSF / RMF** | Voluntary US risk management standards; widely adopted globally |
| **ISO/IEC 27001** | International standard for information security management systems |
| **Cyber Threat Framework (CTF)** | US government standard; common language for describing cyber threat activity |
| **HITRUST** | Security assurance program supporting HIPAA compliance |

### OWASP Security Principles
- **Minimize attack surface** — Reduce all potential entry points for attackers
- **Least privilege** — Give users only the access they need
- **Defense in depth** — Layer multiple security controls
- **Separation of duties** — Critical actions require more than one person
- **Keep it simple** — Complexity weakens security
- **Fix issues correctly** — Find root cause, contain, test the fix
- **Secure defaults** — Apps should be secure out of the box
- **Fail securely** — On failure, default to the most restrictive state (e.g. firewall closes all connections)
- **Don't trust services** — Verify third-party partners' security independently
- **Avoid security by obscurity** — Don't rely on hidden source code as a security measure

### Control Categories
| Type | Examples |
|---|---|
| **Physical** | Gates, locks, CCTV, security guards, access badges |
| **Technical** | Firewalls, MFA, antivirus software |
| **Administrative** | Separation of duties, authorization policies, asset classification |

---

## 5. Security Audits

**Security audit** — an independent review of an org's security controls, policies, and procedures against internal and external criteria.

### Audit Goals
- Ensure IT practices meet industry and organizational standards
- Identify failures and create a remediation plan
- Avoid fines and penalties from regulatory non-compliance

### Factors Affecting Audit Type
Industry type, org size, applicable regulations, geographic location, chosen compliance standards.

### Audit Checklist Steps
1. **Identify scope** — List assets to assess, goals, frequency, and relevant policies
2. **Risk assessment** — Evaluate risks related to budget, controls, and external standards
3. **Conduct audit** — Assess security of all assets in scope
4. **Mitigation plan** — Strategy to lower risk and costs
5. **Communicate results** — Detailed report with findings and improvement recommendations for stakeholders

---

## 6. Playbooks

**Playbook** — a manual with predefined, up-to-date steps to follow when responding to a security incident.

- Treated as **living documents** — updated regularly as threats, laws, and standards evolve
- Used alongside **SIEM tools** (flagged events → analyst follows playbook)
- Used alongside **SOAR tools** (automated response → analyst follows playbook for resolution)

### Incident & Vulnerability Response Steps
1. Preparation
2. Detection
3. Analysis
4. Containment
5. Eradication
6. Recovery
7. Post-incident activities + coordination

> Mishandling data during an incident can compromise forensic evidence, rendering it unusable.

---

## 7. SIEM Tools

**SIEM** — collects and analyzes log data to monitor critical activities, detect threats, and alert analysts in real time. Currently requires human interaction for analysis.

### Splunk Dashboards
| Dashboard | Purpose |
|---|---|
| **Security Posture** | Last 24hrs of notable events; monitors infrastructure performance for SOC teams |
| **Executive Summary** | Overall org security health over time; used for stakeholder reporting |
| **Incident Review** | Visualizes event timeline leading up to an incident; highlights high-risk items |
| **Risk Analysis** | Tracks risk per user/device/IP; shows abnormal activity patterns |

### Chronicle (Google) Dashboards
| Dashboard | Purpose |
|---|---|
| **Enterprise Insights** | Recent alerts with IOCs; confidence scores and severity levels |
| **Data Ingestion & Health** | Monitors log sources and processing success rates |
| **IOC Matches** | Top threats by domain, IP, device over time; guides prioritization |
| **Main Dashboard** | High-level event activity summary; identifies trends across sources |
| **Rule Detections** | Stats on alerts triggered by detection rules; helps manage recurring incidents |
| **User Sign-in Overview** | Tracks user access behavior; flags anomalies like simultaneous logins from multiple locations |

---

## 8. Open-Source vs. Proprietary Tools

| | Open-Source | Proprietary |
|---|---|---|
| **Cost** | Usually free | Paid license/training |
| **Source code** | Publicly available | Owner-controlled only |
| **Customization** | High | Limited |
| **Examples** | Linux, Suricata | Splunk, Chronicle |
| **Security** | Community-reviewed; harder to exploit | Vendor-managed updates |

> Common misconception: open-source tools are less secure. In reality, public visibility means issues are found and fixed faster.

**Suricata** — open-source network analysis and threat detection tool; inspects traffic, detects suspicious behavior, generates logs. Integrates with many SIEM tools.

---

## 9. The Future of SIEM

- **Cloud-hosted SIEM** — vendor-managed infrastructure; accessed via internet; easier to set up
- **Cloud-native SIEM** — built to leverage cloud capabilities (scalability, flexibility, availability)
- **IoT expansion** — more connected devices = larger attack surface = more data to monitor
- **AI/ML integration** — will improve threat identification, dashboards, and data storage
- **SOAR** — automates responses to common incidents, freeing analysts for complex cases
- **Goal** — fully interconnected security platforms that communicate with each other (still in progress)
