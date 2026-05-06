# Controls and Compliance Checklist

**Organization:** Botium Toys  
**Purpose:** Internal security audit — assess current controls and evaluate compliance with PCI DSS, GDPR, and SOC standards.

---

## Controls Assessment

| Yes | No | Control |
|---|---|---|
|  | ✗ | Least Privilege |
|  | ✗ | Disaster recovery plans |
|  | ✗ | Password policies |
|  | ✗ | Separation of duties |
| ✓ |  | Firewall |
|  | ✗ | Intrusion detection system (IDS) |
|  | ✗ | Backups |
| ✓ |  | Antivirus software |
|  | ✗ | Manual monitoring, maintenance, and intervention for legacy systems |
|  | ✗ | Encryption |
|  | ✗ | Password management system |
| ✓ |  | Locks (offices, storefront, warehouse) |
| ✓ |  | Closed-circuit television (CCTV) surveillance |
| ✓ |  | Fire detection/prevention (fire alarm, sprinkler system, etc.) |

---

## Compliance Checklist

### Payment Card Industry Data Security Standard (PCI DSS)

| Yes | No | Best Practice |
|---|---|---|
|  | ✗ | Only authorized users have access to customers' credit card information. |
|  | ✗ | Credit card information is stored, accepted, processed, and transmitted internally in a secure environment. |
|  | ✗ | Data encryption procedures are implemented to secure credit card transaction touchpoints and data. |
|  | ✗ | Secure password management policies are adopted. |

### General Data Protection Regulation (GDPR)

| Yes | No | Best Practice |
|---|---|---|
|  | ✗ | E.U. customers' data is kept private and secured. |
|  | ✗ | A plan is in place to notify E.U. customers within 72 hours if their data is compromised. |
|  | ✗ | Data is properly classified and inventoried. |
|  | ✗ | Privacy policies, procedures, and processes are enforced and documented. |

### System and Organizations Controls (SOC Type 1 & 2)

| Yes | No | Best Practice |
|---|---|---|
|  | ✗ | User access policies are established. |
|  | ✗ | Sensitive data (PII/SPII) is confidential and private. |
| ✓ |  | Data integrity ensures data is consistent, complete, accurate, and validated. |
|  | ✗ | Data is available to individuals authorized to access it. |

---

## Recommendations

Botium Toys has significant gaps across all three compliance frameworks. The most urgent priorities are:

1. **Implement least privilege and separation of duties** — no single employee should have unchecked access to sensitive systems.
2. **Encrypt all sensitive data at rest and in transit** — this is a requirement under both PCI DSS and GDPR.
3. **Establish a disaster recovery and backup plan** — the current lack of backups puts business continuity at serious risk.
4. **Deploy an IDS and formalize password management** — these close two of the most exploited technical attack vectors.
5. **Draft and publish user access policies** — the absence of documented access policies makes SOC compliance impossible to demonstrate.
