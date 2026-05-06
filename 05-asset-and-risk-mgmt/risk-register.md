# Risk Register

**Organization:** Coastal bank  
**Environment:** 100 on-premise employees, 20 remote employees, 2,000 individual accounts, 200 commercial accounts. Operates under strict financial regulations including Federal Reserve reserve requirements.

**Scoring:** Likelihood (1–3) × Severity (1–3) = Priority

---

## Risk Register

| Asset | Risk | Description | Likelihood | Severity | Priority |
|---|---|---|---|---|---|
| Funds | Business email compromise | An employee is tricked into sharing confidential information. | 2 | 2 | 4 |
| Funds | Compromised user database | Customer data is poorly encrypted. | 1 | 3 | 3 |
| Funds | Financial records leak | A backup database server is publicly accessible. | 2 | 2 | 4 |
| Funds | Theft | The bank's safe is left unlocked. | 1 | 3 | 3 |
| Funds | Supply chain disruption | Delivery delays caused by natural disasters. | 1 | 1 | 1 |

---

## Scoring Reference

| | Low (1) | Moderate (2) | Catastrophic (3) |
|---|---|---|---|
| **Certain (3)** | 3 | 6 | 9 |
| **Likely (2)** | 2 | 4 | 6 |
| **Rare (1)** | 1 | 2 | 3 |

---

## Notes

Business email compromise and financial records leaks score higher on likelihood because they rely on human error or negligence, which is harder to fully eliminate through technical controls alone. Theft scores lower on likelihood despite high severity because physical security measures (CCTV, sensors, access controls) are already in place and are effective deterrents.

A compromised user database would require an attacker to first find and exploit an existing software vulnerability, which lowers the likelihood score without reducing severity. Natural disasters are inherently unpredictable and difficult to mitigate beyond maintaining offsite backups and business continuity plans.
