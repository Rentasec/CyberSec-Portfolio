# CyberSec Course 1 — Condensed Notes
*Google Cybersecurity Certificate, Course 1*

---

## 1. Core Concepts & Key Terms

**Cybersecurity** — Protecting networks, devices, people, and data from unauthorized access to ensure **confidentiality, integrity, and availability (CIA)**.

| Term | Definition |
|---|---|
| **Compliance** | Adhering to internal standards and external regulations to avoid fines/breaches |
| **Security Framework** | Guidelines for building plans to mitigate risks and threats |
| **Security Controls** | Safeguards that reduce specific security risks; used alongside frameworks |
| **Security Posture** | An org's ability to defend critical assets and adapt to change |
| **Threat Actor** | Any person/group posing a security risk |
| **Internal Threat** | Current/former employee, vendor, or partner who poses a risk (intentional or accidental) |
| **Network Security** | Protecting an org's network infrastructure from unauthorized access |
| **Cloud Security** | Ensuring cloud-stored assets are correctly configured and access-controlled |

---

## 2. Analyst Skills

### Transferable Skills
- **Communication** — Relay technical info clearly to both technical and non-technical audiences
- **Problem-solving** — Identify attack patterns and find efficient solutions
- **Time management** — Prioritize urgent tasks to minimize damage
- **Growth mindset** — Stay current; tech evolves constantly
- **Diverse perspectives** — Collaboration leads to better security outcomes

### Technical Skills
- **Programming** (Python, SQL) — Automate tasks, query databases, analyze patterns
- **SIEM Tools** — Collect/analyze log data; monitor and alert on critical activity
- **IDS (Intrusion Detection Systems)** — Monitor network activity for intrusions
- **Threat landscape knowledge** — Stay aware of current attacker tactics and malware trends
- **Incident response** — Follow procedures to investigate and remediate incidents

---

## 3. Tools Overview

| Tool | Purpose |
|---|---|
| **Python** | Automate repetitive tasks, reduce human error |
| **SQL** | Query and interact with databases |
| **Linux (CLI)** | Open-source OS used heavily in security workflows |
| **SIEM Tools** | Aggregate logs, provide dashboards, alert on threats (cloud or on-premise) |
| **Packet Sniffer / Network Protocol Analyzer** | Capture and analyze network traffic |
| **IDS** | Scan packets and alert on possible intrusions |
| **Antivirus / Anti-malware** | Detect and eliminate malware via memory pattern scanning |
| **Penetration Testing** | Simulated attacks to identify vulnerabilities |
| **Encryption** | Converts plaintext → ciphertext to protect data confidentiality |

### Playbooks
Manuals that guide analysts through security procedures step-by-step.
- **Chain of Custody** — Documents evidence possession throughout an investigation
- **Protecting & Preserving Evidence** — Prioritizes volatile data first; work from copies, not originals

---

## 4. Ethics & Legal Considerations

### Counterattacks
- **US Law** — Counterattacks are **illegal** for civilians (Computer Fraud and Abuse Act 1986, Cybersecurity Information Sharing Act 2015). Only federal/military personnel are authorized.
- **ICJ (International)** — Counterattacks are permissible only if: targeted only at the original attacker, intended as a stop-communication, non-escalatory, and reversible in effect.
- In practice, organizations avoid counterattacks due to legal uncertainty and risk of escalation.

### Ethical Principles
- **Confidentiality** — Only authorized users access protected assets; respect privacy
- **Privacy Protection** — Safeguard PII (name, phone) and SPII (SSN, credit card numbers)
- **Laws** — Act honestly, transparently, and with respect for the law; stay informed

---

## 5. Frameworks, Controls & Compliance

### CIA Triad
The three foundational principles guiding cybersecurity decisions: **Confidentiality, Integrity, Availability**.

### Key Frameworks
- **NIST CSF / RMF** — Voluntary risk management frameworks widely used globally
- **CIS Controls** — Actionable safeguards for systems and networks

### Major Compliance Standards

| Standard | Scope |
|---|---|
| **FERC-NERC** | US/North American power grid security requirements |
| **FedRAMP** | US federal cloud services security standardization |
| **GDPR** | EU data privacy; 72-hour breach notification required |
| **PCI DSS** | Securing credit card data globally; reduces fraud |
| **HIPAA** | US patient health data protection (Privacy, Security, Breach Notification rules) |
| **ISO** | International standards for technology and management processes |
| **SOC 1 & 2** | Assess user access policies and financial compliance across org levels |

> **Tip:** Stay current on Gramm-Leach-Bliley Act and Sarbanes-Oxley Act as well.

---

## 6. Threat Actors

| Type | Description |
|---|---|
| **APT (Advanced Persistent Threat)** | Highly skilled; targets large orgs/governments; stays hidden long-term; aims at infrastructure or IP |
| **Insider Threat** | Authorized user who sabotages, corrupts, or leaks data |
| **Hacktivist** | Politically motivated; uses hacking for propaganda or social change |
| **Authorized Hacker** | Ethical hacker; conducts legal risk assessments |
| **Semi-Authorized Hacker** | Finds vulnerabilities but doesn't exploit them (researchers) |
| **Unauthorized Hacker** | Malicious; sells stolen data for profit |
| **Unskilled / Script Kiddie** | Uses existing tools; motivated by learning, revenge, or curiosity |

---

## 7. Attack Types

### Password Attacks
Attempt to gain access to password-protected systems.
- **Brute Force** — Try all combinations
- **Rainbow Table** — Use precomputed hash lookups

### Social Engineering
Exploits human trust and error rather than technical vulnerabilities.

**Common tactics:**
- **Phishing** — Deceptive emails to steal data/deploy malware
- **Spear Phishing** — Targeted phishing at a specific user/group
- **Whaling** — Spear phishing aimed at executives
- **Vishing** — Voice-based phishing
- **Smishing** — SMS-based phishing
- **BEC (Business Email Compromise)** — Impersonates a trusted source for financial gain
- **Watering Hole** — Compromises a site frequented by the target group
- **USB Baiting** — Leaves infected USB for victim to plug in
- **Physical Social Engineering** — Impersonates staff or vendors for physical access

**Why it works:** Authority, intimidation, social proof, scarcity, familiarity, trust, and urgency.

### Physical Attacks
- Malicious USB cables/flash drives
- Card cloning and skimming

### Other Attack Types
- **Adversarial AI** — Manipulates ML/AI systems to conduct attacks more efficiently
- **Supply-Chain Attack** — Targets vendors/third parties to inject malware into legitimate products
- **Cryptographic Attacks** — Breaks secure communication (Birthday, Collision, Downgrade attacks)

---

## 8. Malware Types

| Type | How It Works |
|---|---|
| **Virus** | Requires user action to activate; hides in files and damages/destroys data |
| **Worm** | Self-replicates and spreads across networks without user interaction |
| **Ransomware** | Encrypts org data and demands payment for decryption |
| **Spyware** | Silently collects personal data (emails, location, recordings) and sells it |

---

## 9. CISSP Security Domains (Brief Reference)

Attacks map to specific domains:
- **Security & Risk Management** — Social engineering, phishing
- **Asset Security** — Physical attacks
- **Communication & Network Security** — Password attacks, adversarial AI, cryptographic attacks
- **Identity & Access Management** — Adversarial AI
- **Security Architecture & Engineering** — Supply-chain attacks
- **Security Operations** — Supply-chain, incident response

---

## Resources
- [NIST Glossary](https://csrc.nist.gov/glossary)
- [OWASP Top 10](https://owasp.org) — Critical web application risks
- [CISA Free Tools](https://www.cisa.gov) — Open-source cybersecurity tools
- [Tallinn Manual](https://ccdcoe.org/research/tallinn-manual/) — International cyber law guidance
