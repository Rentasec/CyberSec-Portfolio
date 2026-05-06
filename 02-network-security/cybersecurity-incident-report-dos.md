# Cybersecurity Incident Report: SYN Flood DoS Attack

---

## Section 1: Attack Identification

The web server began returning connection timeout errors to visitors. Log analysis revealed a high volume of SYN requests originating from the same IP address within a very short window. This pattern is consistent with a SYN flood — a type of Denial of Service (DoS) attack.

---

## Section 2: How the Attack Caused the Malfunction

When a user initiates a connection to a web server, the TCP protocol performs a three-way handshake:

1. The client sends a **SYN** (synchronize) request to the server.
2. The server replies with a **SYN-ACK** (synchronize-acknowledge) message.
3. The client sends an **ACK** (acknowledge) to confirm and complete the connection.

In a SYN flood attack, a malicious actor sends a large number of SYN packets in rapid succession without completing the handshake. The server allocates resources for each half-open connection and waits for the final ACK that never arrives. As these incomplete connections accumulate, the server exhausts its capacity to handle legitimate traffic.

The logs confirm this pattern: repeated SYN packets from a single IP were flooding the server, consuming its connection queue and causing legitimate visitors to receive timeout errors. The attack effectively prevented the website from being accessible during the attack window.
