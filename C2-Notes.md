# Security Domains Security Analysts Need To Know

## Domain one: Security and risk management

All organizations must develop their security posture. Security posture is an organization’s ability to manage its defense of critical assets and data and react to change. Elements of the security and risk management domain that impact an organization's security posture include:

* Security goals and objectives
* Risk mitigation processes
* Compliance
* Business continuity plans
* Legal regulations
* Professional and organizational ethics

Information security, or InfoSec, is also related to this domain and refers to a set of processes established to secure information. An organization may use playbooks and implement training as a part of their security and risk management program, based on their needs and perceived risk. There are many InfoSec design processes, such as:

* Incident response
* Vulnerability management
* Application security
* Cloud security
* Infrastructure security

As an example, a security team may need to alter how personally identifiable information (PII) is treated in order to adhere to the European Union's General Data Protection Regulation (GDPR).

## Domain two: Asset security

Asset security involves managing the cybersecurity processes of organizational assets, including the storage, maintenance, retention, and destruction of physical and virtual data. Because the loss or theft of assets can expose an organization and increase the level of risk, keeping track of assets and the data they hold is essential. Conducting a security impact analysis, establishing a recovery plan, and managing data exposure will depend on the level of risk associated with each asset. Security analysts may need to store, maintain, and retain data by creating backups to ensure they are able to restore the environment if a security incident places the organization’s data at risk.

## Domain three: Security architecture and engineering	

This domain focuses on managing data security. Ensuring effective tools, systems, and processes are in place helps protect an organization’s assets and data. Security architects and engineers create these processes.

One important aspect of this domain is the concept of shared responsibility. Shared responsibility means all individuals involved take an active role in lowering risk during the design of a security system. Additional design principles related to this domain, which are discussed later in the program, include:

* Threat modeling
* Least privilege
* Defense in depth
* Fail securely
* Separation of duties
* Keep it simple
* Zero trust
* Trust but verify

An example of managing data is the use of a security information and event management (SIEM) tool to monitor for flags related to unusual login or user activity that could indicate a threat actor is attempting to access private data.

## Domain four: Communication and network security

This domain focuses on managing and securing physical networks and wireless communications. This includes on-site, remote, and cloud communications. 

Organizations with remote, hybrid, and on-site work environments must ensure data remains secure, but managing external connections to make certain that remote workers are securely accessing an organization’s networks is a challenge. Designing network security controls—such as restricted network access—can help protect users and ensure an organization’s network remains secure when employees travel or work outside of the main office. 

## Domain five: Identity and access management

The identity and access management (IAM) domain focuses on keeping data secure. It does this by ensuring user identities are trusted and authenticated and that access to physical and logical assets is authorized. This helps prevent unauthorized users, while allowing authorized users to perform their tasks.

Essentially, IAM uses what is referred to as the principle of least privilege, which is the concept of granting only the minimal access and authorization required to complete a task. As an example, a cybersecurity analyst might be asked to ensure that customer service representatives can only view the private data of a customer, such as their phone number, while working to resolve the customer's issue; then remove access when the customer's issue is resolved.
Domain six: Security assessment and testing 

The security assessment and testing domain focuses on identifying and mitigating risks, threats, and vulnerabilities. Security assessments help organizations determine whether their internal systems are secure or at risk. Organizations might employ penetration testers, often referred to as “pen testers,” to find vulnerabilities that could be exploited by a threat actor. 

This domain suggests that organizations conduct security control testing, as well as collect and analyze data. Additionally, it emphasizes the importance of conducting security audits to monitor for and reduce the probability of a data breach. To contribute to these types of tasks, cybersecurity professionals may be tasked with auditing user permissions to validate that users have the correct levels of access to internal systems.

## Domain seven: Security operations 

The security operations domain focuses on the investigation of a potential data breach and the implementation of preventative measures after a security incident has occurred. This includes using strategies, processes, and tools such as:

* Training and awareness
* Reporting and documentation
* Intrusion detection and prevention
* SIEM tools   
* Log management
* Incident management
* Playbooks
* Post-breach forensics
* Reflecting on lessons learned

The cybersecurity professionals involved in this domain work as a team to manage, prevent, and investigate threats, risks, and vulnerabilities. These individuals are trained to handle active attacks, such as large amounts of data being accessed from an organization's internal network, outside of normal working hours. Once a threat is identified, the team works diligently to keep private data and information safe from threat actors.  
Domain eight: Software development security

The software development security domain is focused on using secure programming practices and guidelines to create secure applications. Having secure applications helps deliver secure and reliable services, which helps protect organizations and their users.

Security must be incorporated into each element of the software development life cycle, from design and development to testing and release. To achieve security, the software development process must have security in mind at each step. Security cannot be an afterthought.

Performing application security tests can help ensure vulnerabilities are identified and mitigated accordingly. Having a system in place to test the programming conventions, software executables, and security measures embedded in the software is necessary. Having quality assurance and pen tester professionals ensure the software has met security and performance standards is also an essential part of the software development process. For example, an entry-level analyst working for a pharmaceutical company might be asked to make sure encryption is properly configured for a new medical device that will store private patient data. 

## Key takeaways

In this reading, you learned more about the focus areas of the eight CISSP security domains. In addition, you learned about InfoSec and the principle of least privilege. Being familiar with these security domains and related concepts will help you gain insight into the field of cybersecurity.

# Managing Common Threats, Risks, and Vulnerabilities

*Previously, you learned that security involves protecting organizations and people from threats, risks, and vulnerabilities. Understanding the current threat landscapes gives organizations the ability to create policies and processes designed to help prevent and mitigate these types of security issues. In this reading, you will further explore how to manage risk and some common threat actor tactics and techniques, so you are better prepared to protect organizations and the people they serve when you enter the cybersecurity field.*

## Risk management

A primary goal of organizations is to protect assets. An asset is an item perceived as having value to an organization. Assets can be digital or physical. Examples of digital assets include the personal information of employees, clients, or vendors, such as: 

* Social Security Numbers (SSNs), or unique national identification numbers assigned to individuals 
* Dates of birth
* Bank account numbers
* Mailing addresses

Examples of physical assets include:

* Payment kiosks
* Servers
* Desktop computers
* Office spaces

Some common strategies used to manage risks include:

* Acceptance: Accepting a risk to avoid disrupting business continuity
* Avoidance: Creating a plan to avoid the risk altogether
* Transference: Transferring risk to a third party to manage
* Mitigation: Lessening the impact of a known risk

Additionally, organizations implement risk management processes based on widely accepted frameworks to help protect digital and physical assets from various threats, risks, and vulnerabilities. Examples of frameworks commonly used in the cybersecurity industry include the National Institute of Standards and Technology Risk Management Framework ([NIST RMF](https://csrc.nist.gov/projects/risk-management/about-rmf)) and Health Information Trust Alliance ([HITRUST](https://hitrustalliance.net/product-tool/hitrust-csf/?utm_term=&utm_campaign=HITRUST_i1_PaidSearch&utm_source=adwords&utm_medium=ppc&hsa_acc=2724012343&hsa_cam=16641331914&hsa_grp=136906352837&hsa_ad=598980848547&hsa_src=g&hsa_tgt=dsa-1659695676388&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQiAorKfBhC0ARIsAHDzsluRN5tSpCQal-rYnZLo2wUNppQdUHUba82LMX3JMGOoRPEJ6wG6-LgaAryYEALw_wcB)).

Following are some common types of threats, risks, and vulnerabilities you’ll help organizations manage as a security professional.

## Today’s most common threats, risks, and vulnerabilities
### Threats

A threat is any circumstance or event that can negatively impact assets. As an entry-level security analyst, your job is to help defend the organization’s assets from inside and outside threats. Therefore, understanding common types of threats is important to an analyst’s daily work. As a reminder, common threats include:

* Insider threats: Staff members or vendors abuse their authorized access to obtain data that may harm an organization.
* Advanced persistent threats (APTs): A threat actor maintains unauthorized access to a system for an extended period of time.

### Risks

A risk is anything that can impact the confidentiality, integrity, or availability of an asset. A basic formula for determining the level of risk is that risk equals the likelihood of a threat. One way to think about this is that a risk is being late to work and threats are traffic, an accident, a flat tire, etc. 

There are different factors that can affect the likelihood of a risk to an organization’s assets, including:

* External risk: Anything outside the organization that has the potential to harm organizational assets, such as threat actors attempting to gain access to private information
* Internal risk: A current or former employee, vendor, or trusted partner who poses a security risk
* Legacy systems: Old systems that might not be accounted for or updated, but can still impact assets, such as workstations or old mainframe systems. For example, an organization might have an old vending machine that takes credit card payments or a workstation that is still connected to the legacy accounting system.
* Multiparty risk: Outsourcing work to third-party vendors can give them access to intellectual property, such as trade secrets, software designs, and inventions.
* Software compliance/licensing: Software that is not updated or in compliance, or patches that are not installed in a timely manner

There are many resources, such as the NIST, that provide lists of [cybersecurity risks](https://www.nist.gov/itl/smallbusinesscyber/cybersecurity-basics/cybersecurity-risks). Additionally, the Open Web Application Security Project (OWASP) publishes a standard awareness document about the [top 10 most critical security risks](https://owasp.org/www-project-top-ten/) to web applications, which is updated regularly. 

> Note: The OWASP’s common attack types list contains three new risks for the years 2017 to 2021: insecure design, software and data integrity failures, and server-side request forgery. This update emphasizes the fact that security is a constantly evolving field. It also demonstrates the importance of staying up to date on current threat actor tactics and techniques, so you can be better prepared to manage these types of risks.
Lists that compare the top 10 most common attack types between 2017 and 2021

### Vulnerabilities

A vulnerability is a weakness that can be exploited by a threat. Therefore, organizations need to regularly inspect for vulnerabilities within their systems. Some vulnerabilities include:

* **ProxyLogon:** A pre-authenticated vulnerability that affects the Microsoft Exchange server. This means a threat actor can complete a user authentication process to deploy malicious code from a remote location.
* **ZeroLogon:** A vulnerability in Microsoft’s Netlogon authentication protocol. An authentication protocol is a way to verify a person's identity. Netlogon is a service that ensures a user’s identity before allowing access to a website's location.
* **Log4Shell:** Allows attackers to run Java code on someone else’s computer or leak sensitive information. It does this by enabling a remote attacker to take control of devices connected to the internet and run malicious code.
* **PetitPotam:** Affects Windows New Technology Local Area Network (LAN) Manager (NTLM). It is a theft technique that allows a LAN-based attacker to initiate an authentication request.
* **Security logging and monitoring failures:** Insufficient logging and monitoring capabilities that result in attackers exploiting vulnerabilities without the organization knowing it
* **Server-side request forgery:** Allows attackers to manipulate a server-side application into accessing and updating backend resources. It can also allow threat actors to steal data.

As an entry-level security analyst, you might work in vulnerability management, which is monitoring a system to identify and mitigate vulnerabilities. Although patches and updates may exist, if they are not applied, intrusions can still occur. For this reason, constant monitoring is important. The sooner an organization identifies a vulnerability and addresses it by patching it or updating their systems, the sooner it can be mitigated, reducing the organization’s exposure to the vulnerability. 

To learn more about the vulnerabilities explained in this section of the reading, as well as other vulnerabilities, explore the [NIST National Vulnerability Database](https://nvd.nist.gov/vuln)and [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).

## Key takeaways

In this reading, you learned about some risk management strategies and frameworks that can be used to develop organization-wide policies and processes to mitigate threats, risks, and vulnerabilities. You also learned about some of today’s most common threats, risks, and vulnerabilities to business operations. Understanding these concepts can better prepare you to not only protect against, but also mitigate, the types of security-related issues that can harm organizations and people alike.
