# Incident Report Analysis

**Framework:** NIST Cybersecurity Framework (CSF)

---

## Summary

The organization's network was hit by a Denial of Service (DoS) attack that flooded the network with ICMP packets, halting all network services for approximately two hours. The cybersecurity team contained the attack by blocking all incoming ICMP packets and stopping non-critical services so that critical ones could be restored. Business operations were disrupted for the duration of the recovery period.

---

## Identify

The attack was a DoS flood targeting the internal network. ICMP packets were used to overwhelm network infrastructure, rendering all services unavailable. The affected scope covered the entire internal network.

---

## Protect

To guard against future attacks, the security team implemented two new firewall rules: one to limit the rate of incoming ICMP packets, and another to verify source IP addresses and detect spoofed packets. These controls reduce the network's exposure to volumetric attacks.

---

## Detect

New network monitoring software was deployed to flag abnormal traffic patterns in real time. An IDS/IPS system was also configured to filter suspicious ICMP traffic based on behavioral signatures. Together, these tools should significantly shorten the time between attack onset and detection.

---

## Respond

The immediate response plan for future similar attacks is:

1. Block all incoming ICMP packets as quickly as possible to stop the flood.
2. Use the firewall to filter the attacker's IP address and cap inbound ICMP volume.
3. Apply network segmentation to isolate non-critical infrastructure from critical systems, preventing a single attack from shutting down all operations.
4. Use SIEM tools to monitor log data continuously and enable a faster, more informed response.

---

## Recover

Recovery from a DoS attack centers on restoring service as quickly as possible while minimizing further damage. Continuous monitoring of logs during and after an incident helps the team identify when it is safe to bring services back online. Clear runbooks for critical service restoration will reduce recovery time in future incidents.

---

## Reflection

For DoS attacks, the speed of detection directly determines the scale of damage. Monitoring logs proactively rather than reactively is the most effective habit to develop. This exercise reinforced that a well-documented response plan is just as important as the technical controls themselves.
