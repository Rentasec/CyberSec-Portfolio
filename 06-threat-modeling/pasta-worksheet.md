# PASTA Threat Model Worksheet

**Application:** Sneaker e-commerce platform  
**Framework:** PASTA (Process for Attack Simulation and Threat Analysis)

---

## Stage I: Define Business and Security Objectives

The application is a consumer-facing e-commerce platform where buyers can browse products and contact sellers directly. The platform handles personally identifiable information (PII) and payment data, making data privacy a core business requirement. The platform must comply with PCI DSS for payment processing and maintain user trust to sustain its business model.

---

## Stage II: Define the Technical Scope

Technologies in use:

- **API** — Facilitates communication between buyers, sellers, and backend services.
- **Public Key Infrastructure (PKI)** — Manages digital certificates and encryption keys.
- **SHA-256** — Used for hashing sensitive data.
- **SQL** — Powers the backend database.

APIs and SQL are critical to the user experience, but from a security standpoint, PKI and SHA-256 deserve the most focus. They provide the cryptographic foundation for securing payment data and user credentials. A compromise in either would expose sensitive information at scale.

---

## Stage III: Decompose Application

The application data flow includes user registration, login, product browsing, seller messaging, checkout, and payment processing. Each step involves data moving between the client, application servers, and database. See the data flow diagram for a visual representation of these interactions.

---

## Stage IV: Threat Analysis

Two primary threat types relevant to this platform:

1. **Phishing attacks** — Targeting users or employees to steal credentials or payment information.
2. **SQL injection** — Exploiting input fields to manipulate or extract database contents.

---

## Stage V: Vulnerability Analysis

Two vulnerabilities that could be exploited:

1. **Weak password policies** — Accounts with simple or reused passwords are susceptible to brute force and credential stuffing attacks. An admin account compromise could give an attacker access to the entire platform.
2. **Lack of rate limiting / DoS protection** — Without controls on request volume, the application is vulnerable to a DoS attack that could take the platform offline, directly impacting revenue and user trust.

---

## Stage VI: Attack Modeling

Attack trees were used to map potential attack paths for each identified threat. The SQL injection tree shows how an attacker could move from a vulnerable input field to full database access. The phishing tree shows how credential theft could escalate to account takeover and fraudulent transactions.

---

## Stage VII: Risk Analysis and Impact

Based on the threats and vulnerabilities identified, the following controls are recommended in order of priority:

1. **Security patches and updates** — Keep all dependencies and server software current to eliminate known vulnerabilities.
2. **Employee security training** — Educate staff on phishing recognition to reduce the risk of credential compromise through social engineering.
3. **Strong password policies with MFA** — Enforce complexity requirements and multi-factor authentication on all user and admin accounts.
4. **Data encryption** — Encrypt all sensitive data at rest and in transit using modern standards (TLS, AES-256) to protect payment and PII data even if a breach occurs.
