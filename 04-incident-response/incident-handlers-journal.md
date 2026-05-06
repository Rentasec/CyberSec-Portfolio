# Incident Handler's Journal

---

## Entry 1

**Date:** 26/04/2026

| Field | Details |
|---|---|
| **Description** | Ransomware attack at a small US healthcare clinic |
| **Tools used** | Incident handler's journal |
| **Who** | A group of malicious hackers |
| **What** | Ransomware deployed via phishing emails |
| **When** | Tuesday, approximately 9:00 AM |
| **Where** | Employee computers across the clinic |
| **Why** | Financial gain |
| **Additional notes** | Did any employee interact with the phishing email from a personal device? Personal devices may not have the same security controls as clinic-issued machines, which could widen the scope of the compromise. |

---

## Entry 2

**Date:** 28/04/2026

| Field | Details |
|---|---|
| **Description** | Phishing alert — an employee downloaded a suspicious file confirmed to be malicious |
| **Tools used** | SIEM tool, VirusTotal |
| **Who** | An internal employee (likely a victim, not a threat actor) |
| **What** | Phishing attack resulting in malware download |
| **When** | No timestamp recorded |
| **Where** | Employee computer |
| **Why** | To compromise the company network |
| **Additional notes** | A company-wide reminder should be issued about not clicking suspicious links or downloading unsolicited attachments. VirusTotal confirmed the file as malicious via hash lookup. |

---

## Entry 3

**Date:** 28/04/2026

| Field | Details |
|---|---|
| **Description** | Customer PII stolen — approximately 50,000 customers affected, estimated loss of $100,000 |
| **Tools used** | Wireshark, tcpdump |
| **Who** | Malicious actor |
| **What** | Customer data exfiltrated; ransom demanded |
| **When** | 28/12/2022, 7:20 PM PT |
| **Where** | Company database/network |
| **Why** | Financial gain via data ransom |
| **Additional notes** | Network traffic analysis using Wireshark and tcpdump was used to trace the exfiltration path. Ransom demand suggests this may be connected to a broader ransomware operation. |

---

## Reflections

Working through these incidents made clear that effective response requires a different kind of attention than general IT troubleshooting. You have to be deliberate about what information gets recorded and what gets set aside. Not everything in a log is relevant, and including too much noise in a report can be just as harmful as missing a key detail.

My ability to detect and trace incidents improved significantly over the course of these exercises. Reading network logs, cross-referencing tool output, and building a timeline from fragmented data are skills that only sharpen through practice. The most useful shift in mindset was learning to look for causes, not just symptoms.
