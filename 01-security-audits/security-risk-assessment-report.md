# Security Risk Assessment Report

---

## Part 1: Selected Hardening Tools and Methods

1. Password policies
2. Multi-Factor Authentication (MFA)
3. Port filtering

---

## Part 2: Recommendations and Justification

### Password Policies

Strong, unique passwords for every employee account are a fundamental defense against unauthorized access. When employees use weak or reused passwords, threat actors can gain entry through brute force or credential stuffing attacks. Enforcing minimum length, complexity requirements, and regular rotation significantly raises the cost of a successful attack.

### Multi-Factor Authentication (MFA)

MFA adds a second layer of verification beyond the password. Even if a password is compromised, an attacker still cannot access the account without the second factor. MFA also discourages password sharing among employees, since each login session requires a personal authentication token tied to the individual user. Given that credential-based attacks are one of the most common initial access vectors, MFA is one of the highest-impact controls available.

### Port Filtering

Network firewalls configured with port filtering can block or limit communication on ports that are not needed for business operations. This reduces the attack surface by preventing threat actors from exploiting unused services and limits the blast radius if a device on the network is compromised. Port filtering is a low-overhead control that provides meaningful protection across the entire network perimeter.
