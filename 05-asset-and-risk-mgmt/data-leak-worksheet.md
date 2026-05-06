# Data Leak Worksheet

---

## Incident Summary

A sales manager shared an internal folder — containing unannounced product information, customer analytics, and promotional materials — with their team during a meeting. After the meeting, they did not revoke access. A verbal warning was given, but no access controls were changed.

During a subsequent video call with a business partner, a sales rep intended to share a link to the promotional materials. Instead, they accidentally shared the link to the internal folder. The business partner then posted that link on their company's social media page, assuming it was the approved promotional content.

---

## Control Analysis

| Field | Details |
|---|---|
| **Control** | Least Privilege |
| **Issue** | The sales manager granted temporary access to the internal folder but never revoked it. Instead of updating permissions after the meeting, they relied on a verbal reminder. This left the internal folder accessible to team members beyond the scope of their need, which directly contributed to the accidental overshare. |
| **Relevant Framework** | NIST SP 800-53: AC-6 — Least Privilege |
| **Review** | AC-6 establishes that users should only operate at the level of privilege required to perform their specific responsibilities. The sales team's continued access to the internal folder after the meeting exceeded what was necessary for their roles. |
| **Recommendation** | Temporary access to sensitive folders should be revoked automatically after a defined time period. Activity logs should be maintained to track who has access to sensitive materials at any given time. Regular audits of user privileges would also help catch cases where access has not been properly cleaned up. |
| **Justification** | Automating access revocation removes the dependency on human follow-through. Combined with regular audits, this significantly reduces the likelihood of accidental or unauthorized data exposure. |

---

## NIST SP 800-53: AC-6 Reference

| Field | Details |
|---|---|
| **Control** | Users, processes, and roles should be granted only the minimal access required to complete their assigned functions. |
| **Discussion** | Least privilege should be enforced at the account, role, and process level to prevent users from operating above the access level their responsibilities require. |
| **Enhancements** | Restrict sensitive resource access by role; automatically revoke access after a set period; maintain provisioning logs; conduct regular privilege audits. |
