# Access Control Worksheet

**Incident date:** 10/03/2023

---

## Notes

Key identifying information from the event:

- The account used belongs to Robert Taylor Jr., a contractor with Legal/Administrator-level access.
- The login originated from IP address `152.207.255.255`.
- Robert Taylor Jr.'s contract ended in 2019. His account was still active and was used to access payroll systems in 2023, four years after his departure.

---

## Issues Identified

1. A former contractor retained active system access long after their contract ended.
2. The account held Administrator-level privileges, giving it access to sensitive systems including payroll — far beyond what a contractor's role would typically require.

---

## Recommendations

1. **Set automatic account expiration for contractors.** Contractor accounts should be configured to expire within 30 days of contract end, or immediately upon offboarding — whichever comes first. Manual deactivation processes are too easy to overlook.
2. **Enforce Multi-Factor Authentication (MFA).** MFA would add a verification step that could flag or block access from an account that should no longer be active.
3. **Apply least privilege to contractor accounts.** Contractors should only have access to the specific systems their role requires. Administrator-level access should never be granted unless explicitly justified and reviewed.
