# Security Incident Report

---

## Section 1: Network Protocol Involved

The **Hypertext Transfer Protocol (HTTP)** was the primary protocol involved in this incident.

---

## Section 2: Incident Documentation

A former disgruntled employee carried out a brute force attack against the website's admin account. Once inside, they embedded a malicious script in the website's source code. The script redirected visitors to a different domain and triggered an automatic file download containing malware.

The issue was initially flagged by multiple users who reported their devices running slower after downloading the file. The security team reproduced the behavior in a sandbox environment and confirmed the malware. The reconstructed traffic log from the sandbox test showed the following sequence:

1. The browser sends a DNS request for `yummyrecipesforme.com` and receives the correct IP address.
2. The browser sends an HTTP request to load the webpage.
3. The malicious script triggers a malware file download.
4. The browser sends a DNS request for `greatrecipesforme.com` (the redirect destination).
5. The DNS server returns the IP address for `greatrecipesforme.com`.
6. The browser sends an HTTP request to the redirect domain.

---

## Section 3: Recommended Remediation

The brute force attack succeeded because the admin account lacked sufficient login security. **Multi-Factor Authentication (MFA)** should be implemented on all administrative accounts immediately. MFA requires a second form of verification at login, making brute force attacks ineffective even when the correct password is eventually guessed. Additional controls such as account lockout policies and login attempt rate limiting would further reduce the risk of this type of attack recurring.
