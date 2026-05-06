# Parking Lot USB Exercise

**Scenario:** A USB drive belonging to Jorge, a hospital employee, is found in the parking lot. The drive contains a mix of personal and work files. This exercise analyzes the risks of the device from an attacker's perspective.

---

## Contents

The USB contains Jorge's resume, which exposes his full name, contact details, and employment history. It also holds sensitive work files including employee shift schedules and internal budget documents. Storing personal and professional data together on a single unencrypted device creates compounded risk — a single point of compromise exposes both.

---

## Attacker Mindset

An attacker who found this drive would have immediate access to Jorge's PII, which could be used for identity theft or social engineering attacks against the hospital. The shift schedules reveal the operational rhythms of the organization, including when certain staff are on-site or off-site. Budget information could expose financial vulnerabilities or be used to craft more convincing spear-phishing messages targeting finance staff or executives.

---

## Risk Analysis

The USB could be carrying malware designed to execute automatically when plugged into a hospital computer, potentially spreading to other networked systems. If Jorge's identity is assumed by a threat actor using his PII, they may be able to gain access to additional hospital systems by impersonating him to IT or administrative staff. The operational data on the drive — schedules, budgets, staffing patterns — could serve as reconnaissance for a larger attack. Information like this has both financial and tactical value to a motivated adversary.

---

## Recommended Controls

**Technical:** Enforce full-disk encryption on all USB devices approved for work use. Deploy endpoint controls that restrict or log the use of unmanaged USB devices on hospital computers.

**Operational:** Establish a clear policy that prohibits storing personal files on work devices or drives. Provide guidance on how employees should handle found devices (do not plug them in — report to IT).

**Managerial:** Include USB security awareness in annual training. Conduct periodic audits of removable media policies to ensure they are still current and enforced.
