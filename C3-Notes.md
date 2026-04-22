## Network Security & Cloud Computing — Study Notes

---

## 1. Cloud Computing & Software-Defined Networks

### On-Premise vs. Cloud

Traditional **on-premise networks** keep all devices at a physical company location. **Cloud computing** uses remote servers, applications, and network services hosted on the internet via a **Cloud Service Provider (CSP)**.

CSPs own massive global data centers and sell services through APIs or web consoles.

### CSP Service Models

| Model | Description |
|---|---|
| **SaaS** (Software as a Service) | Ready-to-use software hosted by the CSP (e.g., Gmail, Office 365) |
| **IaaS** (Infrastructure as a Service) | Virtual compute, containers, and storage configured via API |
| **PaaS** (Platform as a Service) | Tools for developers to build and deploy custom cloud applications |

### Deployment Models

- **Hybrid cloud** — Mix of on-premise and CSP resources. Most common; balances cost and control.
- **Multi-cloud** — Using more than one CSP simultaneously.

### Software-Defined Networks (SDN)

SDNs replace physical network hardware with virtual equivalents — virtual switches, routers, and firewalls — hosted on CSP servers. Physical devices increasingly also support SDN through software-based packet routing.

### Benefits of Cloud Computing

- **Reliability** — High availability with minimal interruption for employees and customers.
- **Cost** — Eliminates large upfront infrastructure investments; pay-as-you-go pricing.
- **Scalability** — Elastic model: scale up or down instantly without buying hardware. Security tools like WAFs, IDS/IPS, and L3/L4 firewalls can be deployed rapidly via CSP APIs.

---

## 2. The TCP/IP Model

The TCP/IP model organizes how data is transmitted across networks into **four layers**:

### Layer 1 — Network Access Layer
- Handles creation and physical transmission of data packets.
- Includes hubs, modems, cables, and NICs.
- **ARP (Address Resolution Protocol)** maps IP addresses to MAC addresses for local communication.

### Layer 2 — Internet Layer
- Attaches IP addresses and routes packets between networks.
- Key protocols:
  - **IP** — Routes packets to the correct destination; relies on TCP/UDP for delivery.
  - **ICMP** — Reports transmission errors and is used for troubleshooting (e.g., `ping`).

### Layer 3 — Transport Layer
- Manages data delivery between systems.
- **TCP** — Connection-oriented; uses a 3-way handshake (SYN → SYN/ACK → ACK). Reliable, retransmits lost data.
- **UDP** — Connectionless; faster but less reliable. Used for real-time applications like video streaming and DNS queries.

### Layer 4 — Application Layer
- Handles network requests directly involving users.
- Common protocols: HTTP, HTTPS, SMTP, SSH, FTP, DNS.

---

## 3. The OSI Model

The OSI model provides a more detailed 7-layer view of network communication, commonly used by security professionals to pinpoint where issues or attacks occur.

| Layer | Name | Key Functions |
|---|---|---|
| 7 | Application | User-facing protocols: HTTP, SMTP, DNS |
| 6 | Presentation | Data translation, encryption (e.g., SSL), compression |
| 5 | Session | Opens/closes sessions; handles authentication and checkpoints |
| 4 | Transport | Segmentation, flow control; TCP and UDP |
| 3 | Network | IP addressing and inter-network routing |
| 2 | Data Link | Intra-network packet delivery; switches and NICs; NCP, HDLC |
| 1 | Physical | Physical hardware: cables, hubs, modems; translates data to binary |

> **TCP/IP vs. OSI:** The TCP/IP model condenses OSI's 7 layers into 4. Both are conceptual frameworks; TCP/IP is more widely used in practice.

---

## 4. Network Layer Operations & IP Packets

### IPv4 Packet Structure

An IPv4 packet has two parts:
- **Header** (20–60 bytes) — Contains routing and control information.
- **Data** (up to 65,535 bytes total) — The payload being transmitted.

Key header fields:

| Field | Purpose |
|---|---|
| Version (VER) | IP version (IPv4 or IPv6) |
| HLEN/IHL | Where header ends and data begins |
| Type of Service (ToS) | Router prioritization for QoS |
| Total Length | Full packet size |
| Identification | Reassembly ID for fragmented packets |
| Flags | Indicates fragmentation status |
| Fragmentation Offset | Position of fragment in original packet |
| TTL | Prevents infinite routing loops; decrements at each hop |
| Protocol | Protocol used for the data portion |
| Header Checksum | Detects header corruption |
| Source IP | Sender's IPv4 address |
| Destination IP | Receiver's IPv4 address |
| Options | Additional security options (if HLEN > 5) |

### IPv4 vs. IPv6

| Feature | IPv4 | IPv6 |
|---|---|---|
| Address format | 4 decimal octets (e.g., `198.51.100.0`) | 8 hex groups (e.g., `2002:0db8::ff21:0023:1234`) |
| Address space | ~4.3 billion | ~340 undecillion |
| Header complexity | More fields | Simplified; adds Flow Label field |
| Security | Private address collision risk | More efficient routing; eliminates collisions |

IPv6 was developed to address **IPv4 address exhaustion** as internet-connected devices multiplied.

---

## 5. Network Protocols

A **network protocol** is a set of rules governing how devices communicate — structure, order, and timing of data delivery.

### Communication Protocols

| Protocol | Layer | Port | Notes |
|---|---|---|---|
| TCP | Transport | — | Connection-oriented; 3-way handshake |
| UDP | Transport | — | Connectionless; used for speed-sensitive apps |
| HTTP | Application | 80 | Unencrypted web communication |
| HTTPS | Application | 443 | Encrypted with SSL/TLS |
| DNS | Application | 53 (UDP/TCP) | Translates domain names to IPs |

### Management Protocols

| Protocol | Layer | Notes |
|---|---|---|
| SNMP | Application | Monitor/manage network devices; can reset configs |
| ICMP | Internet | Error reporting and network diagnostics (`ping`) |

### Security Protocols

| Protocol | Layer | Port | Notes |
|---|---|---|---|
| HTTPS | Application | 443 | HTTP + SSL/TLS encryption |
| SFTP | Application | 22 (TCP) | Secure file transfer using SSH + AES encryption |

> **Note:** Security protocols encrypt content but do **not** hide source/destination IP addresses.

---

## 6. Additional Protocols & Port Reference

### Network Address Translation (NAT)
NAT allows devices with private IPs to communicate on the public internet by substituting the router's public IP. Operates at layers 2–3 of TCP/IP.

| Address Type | Assigned By | Cost | Example Ranges |
|---|---|---|---|
| Private | Router | Free | `10.x.x.x`, `172.16–31.x.x`, `192.168.x.x` |
| Public | ISP / IANA | Paid | All other assignable ranges |

### Key Protocol Port Reference

| Protocol | Port |
|---|---|
| DHCP (server) | UDP 67 |
| DHCP (client) | UDP 68 |
| ARP | None (Layer 2) |
| Telnet | TCP 23 |
| SSH | TCP 22 |
| POP3 (unencrypted) | TCP/UDP 110 |
| POP3 (encrypted) | TCP/UDP 995 |
| IMAP (unencrypted) | TCP 143 |
| IMAP (encrypted) | TCP 993 |
| SMTP (unencrypted) | TCP/UDP 25 |
| SMTPS (encrypted) | TCP/UDP 587 |

### Other Important Protocols

- **DHCP** — Automatically assigns IP addresses and provides DNS server and gateway info to devices.
- **ARP** — Maps IP addresses to MAC addresses. Maintains an ARP cache per device.
- **Telnet** — Remote system access via clear text (TCP 23). Insecure; replaced by SSH.
- **SSH** — Encrypted remote access (TCP 22). Replacement for Telnet.
- **POP3** — Downloads email locally from a mail server. Email may be deleted server-side; no multi-device sync.
- **IMAP** — Downloads email headers and keeps content on the server, enabling multi-device access.
- **SMTP** — Routes outgoing email; works with MTA software and DNS to resolve recipient addresses.

---

## 7. Wi-Fi Security Protocols

Wi-Fi is based on the **IEEE 802.11** standard family.

| Protocol | Year | Key Features | Vulnerabilities |
|---|---|---|---|
| **WEP** | 1999 | Oldest standard | Easily broken; considered high-risk |
| **WPA** | 2003 | Introduced TKIP, larger keys, message integrity check | Vulnerable to KRACK attacks |
| **WPA2** | 2004 | Uses AES + CCMP; current industry standard | Still vulnerable to KRACK |
| **WPA3** | 2018 | Uses SAE; 128-bit (or optional 192-bit) encryption | Best current standard |

**WPA2/WPA3 Modes:**
- **Personal** — Single shared passphrase; suitable for home networks.
- **Enterprise** — Centralized, individualized access control; suitable for organizations.

---

## 8. Subnetting & CIDR

**Subnetting** divides a large network into smaller, organized sub-networks to improve performance and security. Each subnet is defined by a unique IP + subnet mask combination.

**CIDR (Classless Inter-Domain Routing)** replaced the older classful addressing system. CIDR addresses include a network prefix (e.g., `198.51.100.0/24`), which represents all IPs from `198.51.100.0` to `198.51.100.255`.

Benefits of subnetting:
- More efficient bandwidth usage.
- Enables creation of isolated security zones.
- No need for additional public IPs from an ISP.

---

## 9. Virtual Networks & Privacy

### Firewalls

Firewalls filter traffic based on port numbers and IP addresses.

| Type | Behavior |
|---|---|
| **Stateless** | Applies fixed rules; does not track connections |
| **Stateful** | Tracks connection state; only needs rules in one direction |
| **NGFW** | Deep packet inspection, app-layer awareness, IDS/IPS features, URL/DNS filtering |

### Proxy Servers

Use NAT to act as a barrier between internal clients and external threats.
- **Forward proxy** — Handles outbound requests from internal clients.
- **Reverse proxy** — Handles inbound requests from external systems to internal services.
- Can also filter traffic, e.g., blocking known malware sites.

### VPNs (Virtual Private Networks)

VPNs encrypt traffic and disguise IP addresses using **encapsulation** — wrapping unencrypted data in an encrypted packet.

| Type | Use Case |
|---|---|
| **Remote access VPN** | Individual devices connecting to a VPN server over the internet |
| **Site-to-site VPN** | Connecting entire networks/offices; typically uses IPSec |

### WireGuard vs. IPSec

| Feature | WireGuard | IPSec |
|---|---|---|
| Speed | Faster (fewer lines of code) | Slower but more established |
| Complexity | Simpler setup | More complex |
| Open source | Yes | No |
| Use cases | Site-to-site and remote access | Primarily site-to-site |

---

## 10. Network Attacks

### Network Interception Attacks

- **Packet sniffing** — Capturing data packets using hardware/software tools. Can be passive (observation) or active (altering traffic). Tools include Wireshark.
- A NIC in **promiscuous mode** accepts all traffic on the network, not just addressed packets.

### IP Spoofing Attacks

After sniffing packets, attackers can impersonate authorized devices.

| Attack | Description | Prevention |
|---|---|---|
| **On-path (MITM)** | Intercepts communication between two trusted parties; can redirect DNS | Encrypt data in transit (TLS) |
| **Smurf attack** | Floods a network by spoofing an authorized IP and sending ICMP pings to broadcast address | Advanced firewall / NGFW with anomaly detection |
| **DoS (via spoofing)** | Floods target with spoofed IP packets until server crashes | Defense-in-depth; industry-standard encryption |

### Backdoor Attacks

Backdoors are intentional or attacker-installed weaknesses that bypass normal access controls. Once inside, attackers can: install malware, launch DoS attacks, steal data, or modify security settings.

### DDoS — Real-World Example (2016 Dyn Attack)

- University students created a **botnet** targeting gaming servers, then posted the code online.
- Cybercriminals used the botnet to send tens of millions of DNS requests to a major DNS provider on October 21, 2016.
- Result: Widespread outages across North America and Europe for ~2 hours.
- Lesson: DDoS attacks on DNS infrastructure can cascade to hundreds of dependent services.

### Impacts of Network Attacks

- **Financial** — Revenue loss, ransomware costs, legal settlements.
- **Reputation** — Loss of customer trust; competitive disadvantage.
- **Public safety** — Attacks on government/utility infrastructure can cause physical harm.

---

## 11. Brute Force Attacks & OS Hardening

### Brute Force Methods

- **Simple brute force** — Manually trying all username/password combinations.
- **Dictionary attack** — Using lists of common passwords or previously leaked credentials.

### Testing Environments

- **Virtual Machines (VMs)** — Isolated software environments for running suspicious code. Can be reverted or deleted. Small risk of VM escape exists.
- **Sandboxes** — Isolated environments for testing patches, malware, or attack simulations. Malware authors may detect sandbox environments.

### Prevention Measures

| Measure | Description |
|---|---|
| **Hashing + Salting** | One-way hash + random characters added to passwords; increases complexity |
| **MFA / 2FA** | Requires 2+ identity verification factors (password + biometric/OTP) |
| **CAPTCHA / reCAPTCHA** | Distinguishes humans from bots to prevent automated attacks |
| **Password policies** | Enforce complexity, expiration, reuse restrictions, and lockout thresholds |

---

## 12. Network Security Applications

Defense-in-depth adds multiple security layers. Key tools:

| Tool | Function | Limitation |
|---|---|---|
| **Firewall** | Allows/blocks traffic based on port and IP rules | Only inspects packet headers (except NGFW) |
| **IDS** (Intrusion Detection System) | Monitors traffic; alerts on known attack signatures or anomalies | Passive only — does not stop attacks; may miss novel threats |
| **IPS** (Intrusion Prevention System) | Monitors and actively blocks suspicious traffic | Inline — failure breaks network connection; false positives can drop legitimate traffic |
| **Full packet capture** | Records all network traffic for analysis and IDS alert investigation | Storage-intensive |
| **SIEM** | Aggregates logs from IDS, IPS, firewalls, VPNs, DNS into a central dashboard | Requires human analysts to interpret and act; no automatic blocking |

> Common SIEM tools: **Google Chronicle** (cloud-native), **Splunk Enterprise / Splunk Cloud**.

---

## 13. Cloud Security

### Key Security Considerations

| Risk | Description |
|---|---|
| **IAM misconfigurations** | Loose user roles can grant unauthorized access to cloud resources |
| **Configuration errors** | Misconfigured services are among the most common causes of cloud breaches |
| **Expanded attack surface** | Each added cloud service introduces new potential entry points |
| **Zero-day attacks** | CSPs can patch and migrate workloads faster than traditional IT in response to unknown exploits |
| **Visibility limitations** | CSPs don't allow customers to monitor traffic on CSP servers directly; flow logs and packet mirroring provide partial visibility |
| **Rapid CSP changes** | Cloud updates can affect an organization's security configurations and require process adaptation |

### Shared Responsibility Model

| Responsibility | CSP | Customer |
|---|---|---|
| Physical data centers | ✓ | |
| Hypervisors & host OS | ✓ | |
| Cloud infrastructure security | ✓ | |
| Service configuration | | ✓ |
| Data and application security | | ✓ |
| Access management | | ✓ |

> Organizations must not assume the CSP covers their configuration responsibilities. Misunderstanding this boundary is a common source of security failures.

---

## 14. Cloud Security Hardening & Cryptography

### Hardening Techniques

- **IAM** — Manage digital identities and control which cloud resources each user can access.
- **Hypervisors** — Virtualize hardware from OS. CSPs use **Type 1** (bare-metal, e.g., VMware ESXi). Type 2 runs on top of an OS (e.g., VirtualBox). Misconfigured hypervisors risk **VM escapes**.
- **Baselining** — Establish a fixed security configuration to compare against future changes (e.g., restricting admin portal access, enabling encryption, enabling threat detection for databases).

### Cryptography in the Cloud

- **Encryption** converts data to ciphertext; only reversible with the correct key.
- Security is based on the secrecy of the **key**, not the algorithm.
- Protects data at rest and in transit.

**Cryptographic erasure (Crypto-shredding):** Destroy encryption keys to render data permanently unreadable — all copies of the key must be destroyed.

### Key Management

| Tool | Description |
|---|---|
| **TPM** (Trusted Platform Module) | Chip that securely stores passwords, certificates, and encryption keys |
| **CloudHSM** | Hardware security module for storing cryptographic keys and performing encryption/decryption operations |

- Customers can provide their own encryption keys for most CSP services.
- The customer is fully responsible for protecting those keys — CSPs have limited ability to help if keys are lost or compromised.
- Federal contractors should refer to **FedRAMP** for a list of verified CSPs.

---

## 15. tcpdump — Network Protocol Analyzer

**tcpdump** is a lightweight, command-line packet analyzer pre-installed on most Linux distributions.

### Output Fields

| Field | Description |
|---|---|
| Timestamp | Hours:minutes:seconds.fractions |
| Source IP | Origin of the packet |
| Source port | Port the packet originated from |
| Destination IP | Where the packet is going |
| Destination port | Target port at the destination |

> By default, tcpdump resolves IPs to hostnames and ports to service names.

### Common Uses

- Establish network traffic baselines.
- Detect and identify malicious traffic.
- Locate unauthorized IM traffic or rogue wireless access points.
- Create custom alerts for network anomalies.
- Assist in investigating IDS alerts.

> ⚠️ Attackers can also use tcpdump or Wireshark to capture credentials and sensitive data on a network.

### Other Common Protocol Analyzers
SolarWinds NetFlow, ManageEngine OpManager, Azure Network Watcher, Wireshark.# C3-Notes: Connect and Protect: Networks and Network Security

## Network components, devices, and diagrams

### Network devices

Network devices maintain information and services for users of a network. These devices connect over wired and wireless connections. After establishing a connection to the network, the devices send data packets. The data packets provide information about the source and the destination of the data.  This is how the information is sent and received via different devices on a network. 

The network is the overall infrastructure that allows devices to communicate with each other. Network devices are specialized vehicles like routers and switches that manage what is being sent and received over the network. Additionally, devices like computers and phones connect to the network via network devices. 
![alt](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/s-oBYPbLT42rx92K21cvxQ_611ef444b75147a5a6e61d82c34b0df1_9i07czTUt71fHdJt2WJV-5cS3YvI7Y1YQdOBF4c19c2wYkhrIu_6f5gYEgtzAKr8DArrVLx6QY6AQNHpMTmD410f6kyDVYNdP1x36o6lrmsv_CRG8iTBfcIZz4FA-g01ceMoYuXTJjCbvwf38YBSWVwB?expiry=1776764481417&hmac=WF6pfFXDr5mBxPlLEAhs8Xi6MYUiB1CvRmY5HUnHg7U)

> Note: In this diagram, a router connects to the internet through a modem, which is provided by your internet service provider (ISP). The firewall is a security device that monitors incoming and outgoing traffic on your network. The router then directs traffic to the devices on your home network, which can include computers, laptops, smartphones, tablets, printers, and other devices. You can imagine here that the server is a file server. All devices on this network can access the files in this server. This diagram also includes a switch which is an optional device that can be used to connect more devices to your network by providing additional ports and Ethernet connections. Additionally, there are 2 routers connected to the switch here for load balancing purposes which will improve the performance of the network. 

### Devices and desktop computers 

Most internet users are familiar with everyday devices, such as personal computers, laptops, mobile phones, and tablets. Each device and desktop computer has a unique MAC address and IP address, which identify it on the network. They also have a network interface that sends and receives data packets. These devices can connect to the network via a hard wire or a wireless connection.

### Firewalls

A **firewall** is a network security device that monitors traffic to or from your network. It is like your first line of defense. Firewalls can also restrict specific incoming and outgoing network traffic. The organization configures the security rules of the firewall. Firewalls often reside between the secured and controlled internal network and the untrusted network resources outside the organization, such as the internet. Remember, though, firewalls are just one line of defense in the cybersecurity landscape. 

### Servers 

**Servers** provide information and services for devices like computers, smart home devices, and smartphones on the network. The devices that connect to a server are called clients. The following graphic outlines this model, which is called the client-server model. In this model, clients send requests to the server for information and services. The server performs the requests for the clients. Common examples include DNS servers that perform domain name lookups for internet sites, file servers that store and retrieve files from a database, and corporate mail servers that organize mail for a company. 

![alt](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/yEzpFYBkSWChuqHQuw5-SA_47876296b9c140229777d37bc916bff1_DVEYhkRb2cM57vspz3iQIbbBaOfDTWTukQLteY2SDv_MAofv-SbuGazdECwDkbJneVXdDvAW6-CuMSMbYLZJVdkUm5b9k0YJd7m9NVDbEZzLgBhO7_0eq30pRJkkUl-QHu97fSitfr2Lva1bPsTd431k?expiry=1776764481417&hmac=9SMH9B7cthJlYXa0CqG9PfLw3XeSrq8Pvh0MPvfW4Dg)

### Hubs and switches

Hubs and switches both direct traffic on a local network. A hub is a device that provides a common point of connection for all devices directly connected to it. Hubs additionally repeat all information out to all ports. From a security perspective, this makes hubs vulnerable to eavesdropping. For this reason, hubs are not used as often on modern networks; most organizations use switches instead. Hubs are more commonly used for a limited network setup like a home office. 

Switches are the preferred choice for most networks. A switch forwards packets between devices directly connected to it. They analyze the destination address of each data packet and send it to the intended device. Switches maintain a MAC address table that matches MAC addresses of devices on the network to port numbers on the switch and forwards incoming data packets according to the destination MAC address. Switches are a part of the data link layer in the TCP/IP model. Overall, switches improve performance and security.

### Routers

Routers connect networks and direct traffic, based on the IP address of the destination network. Routers allow devices on different networks to communicate with each other. In the TCP/IP model, routers are a part of the network layer. The IP address of the destination network is contained in the IP header. The router reads the IP header information and forwards the packet to the next router on the path to the destination. This continues until the packet reaches the destination network. Routers can also include a firewall feature that allows or blocks incoming traffic based on information in the transmission. This stops malicious traffic from entering the private network and damaging the local area network.

### Modems and wireless access points

**Modems** usually connect your home or office with an internet service provider (ISP). ISPs provide internet connectivity via telephone lines, coaxial cables, or fiber optic cables. Modems receive transmissions or digital signals from the internet and convert them into a digital format compatible with the physical connection provided by your ISP. Usually, modems connect to a router that takes the decoded transmissions and sends them on to the local network.
> Note: Enterprise networks used by large organizations to connect their users and devices often use other broadband technologies to handle high-volume traffic, instead of using a modem. 

![alt](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/6gFK3i1wRCyopAF5k1j0HQ_c8d352d18c8e4474941916da8fed74f1_GGmNcX8TiMojwILA_9er2cddFq573EvzkLIBJWj8Bpx5asAiGYLNe-aPI6ZluB_5ub9YgBHeHF5xMvQ52k5VknA8RtTVa033ZN5juPaHECodnA1W0ZhlbBJmWbgXrpomHeRypDrDT36bR8LFLRUN4Kxd?expiry=1776764481417&hmac=okG5j_tYz3bwffRc3f1AXIMvmYYk0iaFJCfRtbhGuds)


### Wireless access point

A **wireless access** point sends and receives digital signals over radio waves creating a wireless network. Devices with wireless adapters connect to the access point using Wi-Fi. Wi-Fi refers to a set of standards that are used by network devices to communicate wirelessly. Wireless access points and the devices connected to them use Wi-Fi protocols to send data through radio waves where they are sent to routers and switches and directed along the path to their final destination.

![alt txt](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/8vl7L2RlSvGkk3LvXaMeKg_6a15bfb726f541d38671388c13b052f1_XU9XxDWBAwQu9gCYs4ZbRB4Do3xxXScibznS8UvafzSyYJoW9JpmUjL8VNbhYvmNmvmgP9x6AwGltYH7SnkcuyJjEGQNsFLvyeyun2-GdCqjHnXbExJgx67JoFd9KMohmA2xv462hh3O2xkvqhl1kX-z?expiry=1776764481417&hmac=bBCZI3cwNlk6ktA3Y1fOfWkd8SDrPW2J4A8a0KWUKdg)

### Using network diagrams as a security analyst

Network diagrams allow network administrators and security personnel to imagine the architecture and design of their organization’s private network.

**Network diagrams** are maps that show the devices on the network and how they connect. Network diagrams use small representative graphics to portray each network device and dotted lines to show how each device connects to the other. By studying network diagrams, security analysts develop and refine their strategies for securing network architectures.

![image alt text](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/v540rACBSUepbsQcE4s3PQ_3b799a13034d42938c980d7c473725f1_2SOA6jNuKUowAynp64ms-agTTUcxt1xas4SFTTAcKU-JfqJHyG2vzmM7qgqMh4J_Euwmri_t3G_CUXydGZRlmV4EZABYDusKE7pBnNWi5gZ_fUbiAetmRiQWL3cMO2iRWDtjtAPMazNxnmT-i5pWmPAe?expiry=1776764481417&hmac=kkaB62foY2dM7wgp1M1wwCLSyDgeHkzK3wtARH8v2D4)

### Key takeaways

In the client-server model, the client requests information and services from the server, and the server performs the requests for the clients. Network devices include routers, workstations, servers, hubs, switches, and modems. Security analysts use network diagrams to visualize network architecture.

## Cloud computing and software-definede networks
