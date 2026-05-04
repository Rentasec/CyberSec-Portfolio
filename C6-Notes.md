# Sound the Alarm: Detection and Response
# Incident Response & Detection — Study Notes

---

## NIST Incident Response Lifecycle

Four phases:
1. **Preparation**
2. **Detection and Analysis**
3. **Containment, Eradication, and Recovery**
4. **Post-Incident Activity**

---

## CSIRT — Computer Security Incident Response Team

A specialized group trained in incident management. Effective response requires:
- **Command** — Appropriate leadership and direction
- **Control** — Managing technical aspects and assigning tasks
- **Communication** — Keeping stakeholders informed

**Key roles:**

| Role | Responsibilities |
|------|-----------------|
| Security Analyst | Monitor environment, triage/analyze alerts, escalate critical threats |
| Technical Lead | Manage technical response; determine root cause; lead containment, eradication, and recovery |
| Incident Coordinator | Coordinate cross-department communication; keep all personnel updated |

> CSIRTs also involve non-security professionals from HR, legal, PR, IT, and management.

---

## SOC — Security Operations Center

A unit dedicated to monitoring networks, systems, and devices for threats. Part of the **blue team** (defensive security).

**SOC structure (tiered pyramid):**

| Tier | Role | Responsibilities |
|------|------|-----------------|
| L1 | SOC Analyst | Monitor/prioritize alerts, create/close tickets, escalate to L2/L3 |
| L2 | SOC Analyst | Investigate escalated tickets, configure/refine security tools, report to SOC Lead |
| L3 | SOC Lead | Manage team operations, advanced detection (malware/forensics analysis), report to SOC Manager |
| — | SOC Manager | Hire/train/evaluate staff, create performance metrics, develop compliance reports, brief executives |

**Specialized SOC roles:**
- **Forensic investigators** (L2/L3) — Collect, preserve, and analyze digital evidence
- **Threat hunters** (L3) — Proactively detect and analyze advanced threats using threat intelligence

---

## Detection Tools: IDS, IPS, EDR

| Capability | IDS | IPS | EDR |
|------------|-----|-----|-----|
| Detects malicious activity | ✓ | ✓ | ✓ |
| Prevents intrusions | ✗ | ✓ | ✓ |
| Logs activity | ✓ | ✓ | ✓ |
| Generates alerts | ✓ | ✓ | ✓ |
| Behavioral analysis (ML/AI) | ✗ | ✗ | ✓ |

**IDS (Intrusion Detection System)**: Monitors and alerts — does NOT stop activity. Examples: Zeek, Suricata, Snort, Sagan.

**IPS (Intrusion Prevention System)**: Monitors, alerts, AND blocks activity. Many IDS tools (Suricata, Snort) also operate as IPS.

**EDR (Endpoint Detection and Response)**: Installed on endpoints; uses behavioral analysis and automation to detect and stop threats without manual intervention. Examples: Open EDR, Bitdefender EDR, FortiEDR.

**Detection categories:**

| Category | Description |
|----------|-------------|
| True Positive | Alert correctly identifies a real attack |
| True Negative | No alert; no malicious activity present |
| False Positive | Alert fires, but no real threat exists (wastes analyst time) |
| False Negative | Real attack occurs but goes undetected (most dangerous) |

---

## SIEM — Security Information & Event Management

Collects and analyzes log data to monitor critical activities across an organization.

**Advantages**: Access to real-time event data, continuous monitoring and alerting, long-term log storage for historical analysis.

**Three-step SIEM process:**

1. **Collect & Aggregate** — Ingest logs from firewalls, servers, routers, etc. into a central location. Parsing maps raw data into readable field-value pairs.
2. **Normalize** — Convert varied log formats into a single, structured, searchable format.
3. **Analyze** — Apply detection rules to normalized data; generate alerts on matches. Correlation compares multiple events to identify threat patterns.

**Common SIEM tools**: Splunk, Chronicle (Google SecOps), IBM QRadar, Elastic, Exabeam, LogRhythm, AlienVault OSSIM.

---

## Network Monitoring

**Baseline**: A reference point for normal network behavior. Deviations from the baseline can indicate suspicious activity.

**What to monitor:**

| Component | What to look for |
|-----------|-----------------|
| Flow analysis | Unusual protocols/port combinations; unexpected C2 communications |
| Packet payload | Sensitive data leaving the network (data exfiltration) |
| Temporal patterns | Traffic spikes outside normal business hours |

**SOC vs NOC:**
- **SOC** — Focuses on security: detecting and responding to threats
- **NOC** — Focuses on performance: maintaining network uptime and availability

**Key monitoring tools:**
- **IDS** — Detects intrusions based on packet payload patterns
- **Packet sniffers / Protocol analyzers** — Capture and inspect raw network traffic (e.g., tcpdump, Wireshark)

---

## Packets & Packet Analysis

**Packet structure:**
- **Header** — Source/destination IP, protocol, packet length, TTL, and more
- **Payload** — The actual data being transmitted
- **Footer (trailer)** — Error-checking data (used by Ethernet; most protocols omit this)

**IPv4 header** (13 fields): Version, IHL, ToS, Total Length, Identification, Flags, Fragment Offset, TTL, Protocol, Header Checksum, Source Address, Destination Address, Options.

**IPv6 header** (8 fields): Version, Traffic Class, Flow Label, Payload Length, Next Header, Hop Limit, Source Address, Destination Address.

**Packet capture (p-cap)**: A file of intercepted packets for later analysis.

**P-cap file formats:**

| Format | Notes |
|--------|-------|
| Libpcap | Default for Linux/macOS tools like tcpdump |
| WinPcap | Older Windows format |
| Npcap | Windows format by Nmap |
| PCAPng | Modern; captures and stores simultaneously ("next generation") |

> Capturing packets requires root/sudo privileges. Enabling promiscuous mode on a NIC allows capturing all visible network traffic, not just traffic addressed to that device.

---

## Wireshark

Open-source GUI-based packet analyzer. Uses **display filters** to isolate specific traffic.

**Common filters:**

| Filter | Description |
|--------|-------------|
| `dns` / `http` / `ftp` | Filter by protocol |
| `ip.addr == 1.2.3.4` | Filter by IP address (source or destination) |
| `ip.src == 1.2.3.4` | Filter by source IP |
| `ip.dst == 1.2.3.4` | Filter by destination IP |
| `eth.addr == xx:xx:xx` | Filter by MAC address |
| `udp.port == 53` | Filter by UDP port |
| `tcp.port == 25` | Filter by TCP port |

**Comparison operators**: `==` (eq), `!=` (ne), `>` (gt), `<` (lt), `>=` (ge), `<=` (le).

**Special operators**:
- `contains` — Match an exact string in a packet
- `matches` — Match using a regular expression (regex)

**Follow Stream**: Reassembles and displays the full exchange between two devices for a given protocol (e.g., view an entire HTTP conversation).

---

## tcpdump

Command-line network protocol analyzer. Pre-installed on most Linux/macOS systems.

**Basic syntax:**
```
sudo tcpdump [-i interface] [option(s)] [expression(s)]
```

**Key options:**

| Flag | Description |
|------|-------------|
| `-i any` | Capture from all network interfaces |
| `-w file.pcap` | Write captured packets to a file |
| `-r file.pcap` | Read from a saved capture file |
| `-v / -vv / -vvv` | Increase verbosity (more packet detail) |
| `-c 10` | Capture only 10 packets |
| `-n` | Disable hostname resolution (best practice) |
| `-nn` | Disable both hostname and port resolution |
| `-D` | List available network interfaces |

**Filter expressions:**
```bash
sudo tcpdump -r capture.pcap -n 'ip and port 80'
sudo tcpdump -r capture.pcap -n 'ip and (port 80 or port 443)'
```

**Output format**: `Timestamp | Source IP:Port > Destination IP:Port | Protocol flags and details`

> Use `-n` to avoid triggering reverse DNS lookups that could alert attackers.

---

## Cybersecurity Incident Detection Methods

**Threat hunting**: Proactive, human-driven search for threats that automated tools miss. Useful for detecting fileless malware and other evasive threats. Threat hunters use threat intelligence, IoCs, IoAs, and machine learning.

**Threat intelligence sources:**
- Industry reports (attacker TTPs)
- Government advisories
- Threat data feeds (IP addresses, domains, file hashes of known threats)

**Threat Intelligence Platform (TIP)**: Centralizes and analyzes threat intelligence from multiple sources to help prioritize threats.

**Cyber deception — Honeypots**: Decoy systems designed to attract and trap attackers, alerting defenders when accessed.

---

## CI/CD Pipeline — Ongoing Monitoring

**Common IoCs in CI/CD pipelines:**

| Category | Examples |
|----------|---------|
| Unauthorized code changes | Changes from unexpected users, unusual times, suspicious content |
| Suspicious deployments | Deployments outside planned windows, to unapproved systems |
| Compromised dependencies | Known CVEs found in builds, new unexpected dependencies |
| Unusual pipeline execution | Unexpected failures, abnormal execution times, altered step order |
| Secrets exposure | Hardcoded credentials found in commits, unauthorized secret access |

**Monitoring approaches:**
- **Pipeline execution logs** — Baseline normal durations/success rates; flag deviations
- **Code commit logs** — Track suspicious changes (off-hours, large deletions, unusual authors)
- **Access logs** — Detect unusual logins or unauthorized access to pipeline settings
- **SIEM integration** — Automated anomaly detection using ML and custom rules for known CI/CD IoCs
- **Real-time alerting** — Immediate notification for build failures, secret exposure attempts, unusual network traffic
- **Continuous vulnerability scanning** — Identify CVEs in CI/CD tools, plugins, and containers

---

## Indicators of Compromise (IoC) & Indicators of Attack (IoA)

- **IoC**: Observable evidence that a security incident *has occurred* (the "who" and "what")
- **IoA**: Observed events indicating an *ongoing* incident (the "why" and "how")

> Example: A process making a network connection = IoA. The process filename and destination IP = IoCs.

**Pyramid of Pain** (David J. Bianco): Describes the difficulty for attackers when each IoC type is blocked.

| Level | IoC Type | Attacker Pain |
|-------|----------|---------------|
| Lowest | Hash values | Easy — attacker recompiles malware |
| ↑ | IP addresses | Easy — attacker changes IPs |
| ↑ | Domain names | Slightly harder |
| ↑ | Network artifacts | Annoying |
| ↑ | Host artifacts | Annoying |
| ↑ | Tools | Challenging — must find/build new tools |
| Highest | TTPs (Tactics, Techniques, Procedures) | Hardest — requires completely new attack approach |

---

## Investigative Tools for IoC Analysis

**VirusTotal**: Analyze suspicious files, domains, URLs, and IP addresses for malicious content. Community-sourced threat intelligence.

*VirusTotal report tabs:*
- **Detection** — Vendor verdicts (malicious, suspicious, safe)
- **Details** — Static analysis: hashes, file type, size, timestamps
- **Relations** — Connected IoCs: URLs, domains, IPs, dropped files
- **Behavior** — Sandbox execution results: network activity, registry changes, processes
- **Community** — Analyst comments and insights

**Other tools:**

| Tool | Purpose |
|------|---------|
| Jotti | Scan suspicious files with multiple AV engines |
| Urlscan.io | Scan and analyze URLs |
| MalwareBazaar | Repository of malware samples for research |

**Crowdsourcing**: Sharing threat intelligence across the global security community enables faster detection and response. ISACs (Information Sharing and Analysis Centers) provide sector-specific threat sharing.

---

## Documentation Best Practices

**Three key benefits of documentation**: Transparency, Standardization, Clarity.

- **Transparency** — Supports compliance, legal proceedings, and audit trails (e.g., chain of custody)
- **Standardization** — Repeatable processes aid knowledge transfer and onboarding (e.g., incident response plans)
- **Clarity** — Helps teams act quickly; analysts must document reasoning for all decisions

**Best practices:**
- **Know your audience** — Tailor language to the reader (SOC analyst vs. executive)
- **Be concise** — State the purpose immediately; avoid unnecessary length
- **Update regularly** — Revise after incidents and when threats evolve

---

## Triage Process

Triage prioritizes security alerts so the most critical incidents are handled first.

**Three steps:**

1. **Receive and assess** — Verify the alert's validity. Ask: Is it a false positive? Has it triggered before? Is it linked to a known vulnerability? How severe is it?
2. **Assign priority** — Evaluate based on:
   - *Functional impact* — Effect on business operations
   - *Information impact* — Data confidentiality/integrity/availability risks
   - *Recoverability* — Whether full recovery is possible and worth the effort
3. **Collect and analyze** — Gather evidence, conduct research, document the process. Escalate to L2/manager if needed.

**Benefits**: Efficient resource use, standardized process, faster response to critical threats.

---

## Business Continuity Planning (BCP)

A **BCP** outlines procedures to sustain operations during and after a major disruption. Distinct from a **Disaster Recovery Plan** (DRP), which focuses on restoring IT systems after a disaster.

**Site resilience types:**

| Type | Description |
|------|-------------|
| Hot site | Fully operational duplicate of the primary environment; activates immediately |
| Warm site | Fully configured but not live; can be made operational quickly |
| Cold site | Basic infrastructure only; requires significant setup before use |

> Ransomware attacks on critical infrastructure (e.g., healthcare) can block access to medical records, disrupt services, and threaten public safety — making BCP essential.

---

## Post-Incident Activity

**Lessons learned meeting** (post-mortem): Held within two weeks of incident resolution. Reviews the full incident, evaluates response actions, and identifies improvements — not to assign blame.

Key questions:
- What happened and when?
- Who discovered it?
- How was it contained and recovered?
- What could have been done differently?

**Final report components:**

| Section | Description |
|---------|-------------|
| Executive summary | High-level overview of key findings for non-technical readers |
| Timeline | Chronological sequence of events with timestamps |
| Investigation | Actions taken during detection and analysis |
| Recommendations | Suggested improvements to prevent recurrence |

> Always tailor the final report to your audience — executives need plain language, not technical jargon.

---

## Log Management

**Log types:**

| Type | Source |
|------|--------|
| Network | Firewalls, routers, switches |
| System | Operating systems (Windows, Linux, macOS) |
| Application | Software applications |
| Security | Antivirus, IDS tools |
| Authentication | Login events |

**Verbose logging**: Records additional detail beyond default log settings.

**Log management best practices:**
- Log only what's necessary — overlogging increases storage costs and slows searches
- Follow regulatory retention requirements (HIPAA, PCI DSS, FISMA, SOX, GLBA)
- Store logs on a **centralized log server** to protect integrity and prevent tampering by attackers
- Avoid logging PII unless required and legally permitted

---

## Log File Formats

| Format | Key Features |
|--------|-------------|
| **JSON** | Key-value pairs, curly brackets for objects, square brackets for arrays; lightweight; used in web/cloud |
| **Syslog** | Standard protocol/service/format; three components: header, structured-data, message; port 514 (plain), 6514 (encrypted) |
| **XML** | Tag-based; uses root and child elements; native to Windows; supports attributes |
| **CSV** | Comma-separated values; field position matters; no field names included in log |
| **CEF** | Pipe-delimited fields + key-value extension; commonly transported via Syslog |

**CEF format:**
```
CEF:Version|Vendor|Product|DeviceVersion|SignatureID|Name|Severity|Extension
```

---

## Suricata

Open-source IDS/IPS and network analysis tool.

**Three operating modes:**
- **IDS** — Detects and alerts on suspicious network or host activity
- **IPS** — Detects and blocks malicious traffic (requires additional configuration)
- **NSM (Network Security Monitoring)** — Produces and saves network logs for forensics and analysis

**Signature structure:**
```
action header (rule options)
```

| Component | Description |
|-----------|-------------|
| Action | What to do: `alert`, `pass`, `drop`, or `reject` |
| Header | Source/destination IPs, ports, protocol, traffic direction |
| Rule options | Customization: keywords, thresholds, content matches, metadata |

> Rule order matters. Default processing order: pass → drop → reject → alert.

**Log files:**

| File | Description |
|------|-------------|
| `eve.json` | Detailed JSON log with metadata; preferred for SIEM ingestion and deep analysis |
| `fast.log` | Minimal alert info (IP/port); legacy format; not suitable for incident response |

**Configuration**: Managed via `suricata.yaml`. Custom rules should be tailored to each organization's environment to minimize false positives.

---

## SIEM Search Methods

### Splunk — SPL (Search Processing Language)

**Basic search:**
```spl
index=main fail
```

**Piped commands:**
```spl
index=main fail | chart count by host
```

**Wildcard:**
```spl
index=main fail*    # matches "failed", "failure", etc.
```

**Exact phrase:**
```spl
index=main "login failure"
```

### Google SecOps (Chronicle)

**Two search types:**

| Type | Description |
|------|-------------|
| UDM Search | Default; searches normalized/indexed data — faster |
| Raw Log Search | Searches unparsed raw logs — slower; supports regex |

**Common UDM fields:**
- `metadata.event_type` — Type of event (e.g., `"USER_LOGIN"`)
- `entities` — Device, user, or process details
- `network metadata` — Protocol and connection info
- `security results` — Outcome of security events (e.g., quarantine result)

**Example UDM query:**
```
metadata.event_type = "USER_LOGIN"
```

> Use **Procedural Filtering** in Chronicle to include/exclude results by event type or log source.
