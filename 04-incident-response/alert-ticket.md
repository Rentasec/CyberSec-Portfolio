# Alert Ticket

---

## Ticket Details

| Field | Details |
|---|---|
| **Ticket ID** | A-2703 |
| **Alert Message** | SERVER-MAIL: Phishing attempt — possible malware download |
| **Severity** | Medium |
| **Status** | Escalated |

**Details:** The user may have opened a malicious email and interacted with an attachment or embedded link.

---

## Ticket Comments

The attachment was submitted to VirusTotal for hash analysis. The file was confirmed malicious. The ticket has been escalated to the incident response team for containment and further investigation.

---

## Supporting Evidence

**Known malicious file hash:**
`54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b`

**Suspicious Email:**

| Field | Value |
|---|---|
| **From** | Def Communications `<76tguyhh6tgftrt7tg.su>` — IP: 114.114.114.114 |
| **Sent** | Wednesday, July 20, 2022 at 09:30 AM |
| **To** | `hr@inergy.com` — IP: 176.157.125.93 |
| **Subject** | Re: Infrastructure Engineer role |
| **Attachment** | `bfsvc.exe` |

**Email Body:**

> Dear HR at Ingergy,
>
> I am writing to express my interest in the engineer role posted from the website.
>
> Attached is my resume and cover letter. For privacy, the file is password protected. Use the password `paradise10789` to open.
>
> Thank you,
> Clyde West

---

## Analysis Notes

Several indicators of compromise are present in this email:

- The sender domain (`.su`) is a known high-risk top-level domain historically associated with malicious activity.
- The request to use a password to open an attachment is a common social engineering technique to bypass email security scanning.
- The attachment is an `.exe` file, which should never be distributed as part of a job application.
- The misspelling of the recipient company name ("Ingergy" instead of "Inergy") is consistent with a mass phishing campaign using imperfect templates.
- VirusTotal confirmed the file hash as malicious, corroborating all behavioral indicators.
