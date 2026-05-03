# Assets, Threats & Vulnerabilities

---

## Asset Management & Classification

**Asset management** is the process of tracking assets and the risks that affect them. You can only protect what you know you have.

**Types of assets**: digital (customer data, financial records), information systems (networks, software), physical (facilities, equipment), and intangible (brand reputation, IP).

**Classification scheme** (high → low):

| Level | Description |
|-------|-------------|
| Restricted | Highest sensitivity; need-to-know only |
| Confidential | Disclosure could significantly harm the organization |
| Internal-only | Available to employees and business partners |
| Public | No negative impact if released |

**Challenges**: Ownership can be ambiguous (e.g., employee laptops used personally), and information can hold multiple classification values simultaneously.

---

## Cloud Computing & Cloud Security

**Cloud computing**: On-demand, massively scalable service hosted on shared infrastructure, accessible via the internet.

**Three service models:**

| Model | Description | Examples |
|-------|-------------|---------|
| SaaS | Front-end apps accessed via browser | Gmail, Slack, Zoom |
| PaaS | Back-end dev tools hosted by provider | Google App Engine, Heroku |
| IaaS | Remote access to back-end infrastructure | AWS, Azure, Google Cloud |

**Shared responsibility model**: Clients secure what they control (identity/access management, resource config, data handling); providers secure the underlying infrastructure.

**Key cloud security challenges:**
- Misconfiguration — most common risk; clients use default settings that don't meet their security needs
- Cloud-native breaches stemming from misconfigured services
- Difficulty monitoring access
- Regulatory compliance (HIPAA, PCI DSS, GDPR)

---

## NIST Cybersecurity Framework (CSF)

Originally released in 2014 to protect U.S. critical infrastructure; updated in 2024 to add the **Govern** function.

**Three components:**

- **Core** — Six functions: Identify, Protect, Detect, Respond, Recover, Govern
- **Tiers** — Scale of 1–4 measuring the sophistication of a security program
- **Profiles** — Industry-specific templates for building or benchmarking a security baseline

**CISA's implementation steps:**
1. Create a current profile of security operations
2. Perform a risk assessment against business/regulatory standards
3. Analyze and prioritize security gaps
4. Implement a plan to meet organizational goals

> Note: Regulations must be followed; frameworks are voluntary resources you can choose to adopt.

---

## Principle of Least Privilege (PoLP)

Users are granted only the **minimum access required** to complete their tasks. This supports the CIA triad and reduces the risk of breaches, accidental data loss, and insider threats.

**Account types:**

| Type | Description |
|------|-------------|
| Guest | External users (clients, contractors) |
| User | Staff accounts based on job duties |
| Service | Assigned to applications/software |
| Privileged | Elevated/administrative access |

**Auditing approaches:**
- **Usage audits** — Review what resources accounts are accessing
- **Privilege audits** — Identify privilege creep (accumulated excess access over time)
- **Account change audits** — Review directory logs for suspicious modifications

---

## Data Lifecycle & Governance

**Five stages**: Collect → Store → Use → Archive → Destroy

**Data governance roles:**
- **Data owner** — Decides who can access, edit, or destroy information
- **Data custodian** — Responsible for safe handling, transport, and storage
- **Data steward** — Maintains and implements governance policies

**Legally protected data types:**

| Type | Description |
|------|-------------|
| PII | Personally Identifiable Information — used to identify/contact an individual |
| PHI | Protected Health Information — regulated by HIPAA (US) and GDPR (EU) |
| SPII | Sensitive PII — stricter handling required (e.g., bank accounts, credentials) |

---

## Privacy Regulations

**Key distinction**: Privacy = people's control over their data. Security = protecting data from unauthorized access.

**Three major regulations:**

| Regulation | Scope |
|------------|-------|
| GDPR | EU regulation; applies to any business handling EU residents' data |
| PCI DSS | Financial industry; secures credit/debit card transactions |
| HIPAA | US law; protects sensitive patient health information |

**Compliance evaluation:**
- **Security audit** — Reviews controls/policies against a set of expectations (~annually)
- **Security assessment** — Tests resilience of current implementations against threats (~every 3–6 months)

---

## Hashing & Encryption

### Hash Functions

Hashing converts data into a fixed-size value (digest) that cannot be reversed. Used for verifying integrity and securing stored passwords.

| Algorithm | Digest Size | Notes |
|-----------|------------|-------|
| MD5 | 128-bit (32 chars) | Vulnerable to hash collisions — avoid for security |
| SHA-1 | 160-bit | Not collision-resistant |
| SHA-256 | 256-bit | Widely used; collision-resistant |
| SHA-512 | 512-bit | High security; collision-resistant |

**Hash collision**: When two different inputs produce the same hash — exploitable by attackers to spoof authentic data.

**Rainbow table attack**: Using a pre-generated dictionary of hash values to crack passwords.

**Salting**: Adding a random string to data before hashing, making rainbow table attacks ineffective. Longer, more complex salts = harder to crack.

---

### Encryption

| Type | Keys Used | Speed | Use Case |
|------|-----------|-------|----------|
| Symmetric | Single shared secret key | Faster | Bulk data (e.g., active web sessions) |
| Asymmetric | Public key (encrypt) + Private key (decrypt) | Slower | Sensitive data, key exchange |

**Approved algorithms:**

| Algorithm | Type | Key Size |
|-----------|------|----------|
| 3DES | Symmetric | 168-bit effective |
| AES | Symmetric | 128, 192, or 256-bit |
| RSA | Asymmetric | 1,024–4,096-bit |
| DSA | Asymmetric | 2,048-bit |

**Kerckhoff's Principle**: A cryptographic system should be secure even if everything about it except the private key is public knowledge. Security through obscurity is not real security.

---

## Identity & Access Management (IAM)

IAM is a collection of processes and technologies to manage digital identities and enforce access controls.

**Authentication factors** (Something you...):
- **Know** — password, PIN
- **Have** — token, smart card
- **Are** — biometrics

**Access control models:**

| Model | Description |
|-------|-------------|
| MAC (Mandatory) | Strictest; central authority grants access on a need-to-know basis |
| DAC (Discretionary) | Data owner decides access levels (e.g., Google Drive sharing) |
| RBAC (Role-Based) | Access determined by a user's role in the organization |

**Key concepts**: SSO (Single Sign-On) combines multiple logins; MFA requires two or more verification factors.

**User provisioning**: Creating and maintaining digital identities. **Deprovisioning** removes access when it's no longer needed.

---

## Vulnerability Management

### Vulnerability Scanning

Scanners automatically compare known vulnerabilities against technologies on a network.

| Scan Type | Description |
|-----------|-------------|
| External | Tests outward-facing systems (websites, firewalls) |
| Internal | Tests systems from inside the network |
| Authenticated | Uses real login credentials to test access controls |
| Unauthenticated | Simulates an external attacker with no credentials |
| Limited | Focuses on specific devices |
| Comprehensive | Scans all connected devices and systems |

### Penetration Testing

A **pen test** is an authorized simulated attack to find and exploit vulnerabilities, determining real-world consequences.

| Strategy | Also Known As | Access Level |
|----------|---------------|--------------|
| Open-box | White-box / Full knowledge | Internal developer-level access |
| Closed-box | Black-box / Zero knowledge | No internal access (simulates real attacker) |
| Partial knowledge | Gray-box | Limited access (e.g., customer service rep) |

**Team types**: Red team (attack/exploit), Blue team (defend/respond), Purple team (collaborative).

> Organizations regulated by PCI DSS, HIPAA, or GDPR must conduct pen tests regularly.

---

## OWASP Top 10

A regularly updated list of the most critical web application vulnerabilities:

1. **Broken Access Control** — Unauthorized access to data or functions
2. **Cryptographic Failures** — Weak or missing encryption (e.g., using MD5 for PII)
3. **Injection** — Malicious code inserted into a vulnerable app (e.g., SQL injection)
4. **Insecure Design** — Missing security controls at the design stage
5. **Security Misconfiguration** — Default or improperly configured settings
6. **Vulnerable & Outdated Components** — Using unpatched open-source libraries
7. **Identification & Authentication Failures** — Weak login/access controls
8. **Software & Data Integrity Failures** — Unreviewed updates; supply chain attacks
9. **Security Logging & Monitoring Failures** — Insufficient audit trails
10. **Server-Side Request Forgery (SSRF)** — Attacker manipulates server to fetch unauthorized data

---

## CI/CD Pipeline Security

**CI/CD** automates the software release pipeline: code → build → test → deploy.

- **CI** (Continuous Integration): Frequently merges code; runs automated builds and tests
- **CD** (Continuous Delivery): Code always ready to release; manual approval before production
- **CD** (Continuous Deployment): Fully automated — changes go live without manual approval

**Common vulnerabilities:**

| Vulnerability | Risk | Mitigation |
|---------------|------|------------|
| Insecure dependencies | CVEs inherited from third-party libraries | Regularly scan and update dependencies (e.g., Dependabot, Snyk) |
| Misconfigured permissions | Unauthorized code/config access | Implement RBAC and least privilege |
| No automated security testing | Vulnerabilities reach production undetected | Integrate SAST and DAST into the pipeline |
| Exposed secrets | Hardcoded credentials get stolen | Use secrets management tools (e.g., HashiCorp Vault) |
| Unsecured build environments | Attackers inject malicious code | Harden environments; use secure containers |

**DevSecOps**: Embedding security into every stage of development — not just at the end.

---

## Threat Actors & Attack Vectors

**Threat actor categories:**

| Category | Description |
|----------|-------------|
| Competitors | Rival companies seeking leaked information |
| State actors | Government intelligence agencies |
| Criminal syndicates | Organized crime groups |
| Insider threats | Employees or former employees with authorized access |
| Shadow IT | Individuals using unauthorized technology (e.g., personal email for work) |

**Hacker types**: Unauthorized (malicious/unethical), Authorized (ethical/pen testers), Semi-authorized (hacktivists).

**APT (Advanced Persistent Threat)**: Long-term unauthorized access, often state-sponsored; targets surveillance and intelligence gathering.

**Common attack vectors**: Direct physical access, removable media (USB), social media, email, wireless networks, cloud services, supply chains.

---

## Brute Force Attacks

| Attack Type | Description |
|-------------|-------------|
| Simple brute force | Manually guessing all credential combinations |
| Dictionary attack | Using a list of common credentials |
| Reverse brute force | Testing one password against many usernames |
| Credential stuffing | Using stolen credentials from previous breaches |

**Common tools**: Aircrack-ng, Hashcat, John the Ripper, Ophcrack, THC Hydra.

**Defenses**: Hashing + salting, MFA, CAPTCHA, strong password policies (lockout thresholds, complexity requirements, rotation).

---

## Social Engineering

**Social engineering** exploits human psychology rather than technical vulnerabilities.

**Common tactics:**

| Tactic | Description |
|--------|-------------|
| Baiting | Tempts users into compromising security (e.g., infected USB drops) |
| Phishing | Fraudulent digital communications to steal data or deploy malware |
| Quid pro quo | Promises a reward in exchange for sensitive information |
| Tailgating | Unauthorized person follows an authorized person into a restricted area |
| Watering hole | Compromising a website frequently visited by the target group |

**Phishing types:**

| Type | Channel |
|------|---------|
| Email phishing | Email |
| Smishing | SMS / text messaging |
| Vishing | Voice calls |
| Spear phishing | Targeted email at specific individuals |
| Whaling | Spear phishing aimed at executives |
| Angler phishing | Impersonating customer support on social media |

**Defenses**: Security awareness training, email filtering, MFA, firewalls, block lists.

---

## Malware Types

| Type | Description |
|------|-------------|
| Virus | Requires user installation; damages data/software |
| Worm | Self-replicating; spreads across networks without user action |
| Trojan | Disguised as legitimate software; used for spying or backdoor access |
| Adware | Displays ads; malicious versions monetize without consent |
| Spyware | Collects and sells user data without consent (PUA) |
| Scareware | Fake warnings trick users into infecting their own devices |
| Fileless malware | Lives in memory; uses legitimate programs — no file on disk |
| Rootkit | Provides remote admin access; often delivered via dropper/loader |
| Botnet | Network of infected machines controlled by a "bot-herder" |
| Ransomware | Encrypts data and demands payment for restoration |

---

## SQL Injection

SQL injection inserts malicious queries into vulnerable input fields to manipulate databases.

**Three categories:**

| Category | How it works |
|----------|-------------|
| In-band | Attack and results use the same channel (most common) |
| Out-of-band | Results returned via a separate channel (rare) |
| Inferential | No direct results; attacker infers database structure from system behavior |

**Prevention techniques:**
- **Prepared statements** — Execute SQL before accepting user input
- **Input sanitization** — Strip out characters that could be interpreted as code
- **Input validation** — Ensure input matches expected format/type

---

## OSINT (Open-Source Intelligence)

**OSINT** is the collection and analysis of publicly available information to generate usable intelligence for security decisions.

**Information vs. Intelligence**: Raw data = information. Analyzed and actionable = intelligence.

**Common uses**: Identifying emerging threats, detecting data exposures, evaluating defenses, finding unknown vulnerabilities.

**Key tools:**

| Tool | Purpose |
|------|---------|
| VirusTotal | Analyze suspicious files, URLs, IPs for malware |
| MITRE ATT&CK® | Knowledge base of adversary tactics and techniques |
| OSINT Framework | Web interface for finding OSINT tools by source/platform |
| Have I Been Pwned | Check if email accounts have been involved in breaches |

---

## Threat Modeling

The process of identifying assets, vulnerabilities, and threats to proactively reduce risk — especially in application security.

**Threat modeling cycle:**
1. Define scope
2. Identify threats
3. Characterize the environment
4. Analyze threats
5. Mitigate risks
6. Evaluate findings

**Common frameworks:**

| Framework | Focus |
|-----------|-------|
| STRIDE | Microsoft framework; covers Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation of Privilege |
| PASTA | Risk-centric; 7-stage evidence-based process |
| Trike | Security permissions and privilege models |
| VAST | Automated; part of the ThreatModeler® platform |

**Key questions to ask**: What are we working on? What can go wrong? What are we doing about it? Have we addressed everything? Did we do a good job?

> Threat modeling should be performed before, during, and after application development as part of the SDLC.

---

## Software Updates & Patch Management

A **patch update** addresses security vulnerabilities (CVEs) in software or OS.

| Strategy | Advantage | Disadvantage |
|----------|-----------|--------------|
| Manual updates | Full control over deployment | Critical patches may be missed or delayed |
| Automatic updates | Always current; simplified process | Poorly tested patches can cause instability |

**End-of-life (EOL) software**: No longer supported or patched by the vendor — poses unfixable security risks. CISA recommends discontinuing use.

> Example: The 2017 WannaCry ransomware attack affected 150+ countries and caused ~$4B in damages. It exploited a vulnerability that had already been patched months earlier.
