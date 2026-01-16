# **OSYS2020 – Week 1 Presentation**

## **Windows Security Goals & Common Threat Types**

---

## **Slide 1 – Welcome & Why This Course Matters**

### **Course:** OSYS2020 – Windows Security

### **Week 1:** Windows Security Goals & Threat Landscape

**Why this course matters**

* Windows systems run the majority of business environments
* Security failures are rarely “technical accidents” — they are **design, configuration, or policy failures**
* This course prepares you to **secure real systems**, not just pass exams

> **Key Message:**
> You are not learning “Windows features” — you are learning how to **defend systems people rely on**

---

## **Slide 2 – Learning Outcomes for Today**

By the end of this week, you will be able to:

* Explain the **core goals of Windows security**
* Identify **common threat types** that affect Windows systems
* Connect **security goals to real-world attacks**
* Describe how **misconfiguration** creates security risk

These outcomes support:

* **LO1:** OS hardening
* **LO2:** Understanding Windows security components

---

## **Slide 3 – Engagement Hook: Real-World Scenario**

### **Scenario: Small Business Breach**

A small company:

* Uses Windows Server
* Has Active Directory
* Shares files internally
* Applies updates “when there’s time”

**What happened:**

* One phishing email
* One compromised workstation
* Entire domain encrypted in under 2 hours

💡 **Discussion Prompt**

* What do you think failed first?
* Technology? People? Configuration?

---

## **Slide 4 – What Is “Windows Security”?**

Windows security is **not one feature**.

It is:

* Policies
* Configurations
* Services
* User behavior
* Administrative decisions

> **Security is a system**, not a checkbox

Windows security exists to:

* Protect **data**
* Control **access**
* Maintain **system integrity**
* Support **business operations**

---

## **Slide 5 – Core Windows Security Goals**

Windows security is built around **four core goals**:

### 1. **Confidentiality**

* Only authorized users access data
* Examples:

  * File permissions
  * User authentication
  * Encryption

### 2. **Integrity**

* Data and systems are not altered improperly
* Examples:

  * Patch management
  * Malware protection
  * Change control

### 3. **Availability**

* Systems remain accessible when needed
* Examples:

  * Updates without downtime
  * Protection from ransomware
  * Backup strategies

### 4. **Accountability**

* Actions can be traced to users
* Examples:

  * Logging
  * Auditing
  * Event logs

---

## **Slide 6 – Security Is Always a Trade-Off**

Every security decision balances:

* **Security**
* **Usability**
* **Cost**
* **Performance**

Example:

* Strong passwords improve security
* But increase helpdesk calls

> **Key Skill You’ll Develop:**
> Making **informed security decisions**, not blindly locking everything down

---

## **Slide 7 – Common Threat Types (High-Level)**

Threats to Windows systems typically fall into these categories:

* **Malware**
* **Credential Attacks**
* **Misconfiguration**
* **Privilege Abuse**
* **Network-Based Attacks**
* **Insider Threats**

We will revisit these threats **every week**, from different angles.

---

## **Slide 8 – Malware Threats**

### What is malware?

Malicious software designed to:

* Steal data
* Damage systems
* Gain unauthorized access

Common Windows malware:

* Viruses
* Trojans
* Ransomware
* Keyloggers

💡 **Important Insight**
Malware often succeeds **after** a configuration failure — not because antivirus was missing.

---

## **Slide 9 – Credential-Based Attacks**

Attackers often target **accounts**, not systems.

Examples:

* Weak passwords
* Password reuse
* Phishing
* Pass-the-hash attacks

Why this matters in Windows:

* Active Directory centralizes access
* One compromised account can affect many systems

> **Security Rule:**
> If credentials fall, everything falls

---

## **Slide 10 – Misconfiguration: The #1 Threat**

Most Windows breaches happen because of:

* Excessive permissions
* Disabled security features
* Default settings left unchanged
* Unpatched systems

Examples:

* Users running as administrators
* Open file shares
* Old protocols still enabled

💡 **Key Course Theme:**

> Secure configuration is more important than advanced tools

---

## **Slide 11 – Privilege Abuse**

### What is privilege?

* Rights and permissions granted to users or processes

Problems arise when:

* Users have more access than needed
* Admin rights are used for daily tasks

This violates:

* **Principle of Least Privilege**

You will:

* Identify privilege misuse
* Correct it using policies and permissions

---

## **Slide 12 – Network-Based Threats**

Windows systems are networked systems.

Threats include:

* Unauthorized access
* Lateral movement
* Exploiting open services

Why firewalls matter:

* Control what can talk to what
* Limit attack paths

> **Later in the course:**
> You will break and then fix network access in a Windows domain

---

## **Slide 13 – Insider Threats**

Not all threats come from outside.

Examples:

* Employees
* Contractors
* Former staff

Insider threats often involve:

* Legitimate credentials
* Excessive access
* Poor monitoring

This is why:

* Logging
* Auditing
* Accountability
  are critical security goals

---

## **Slide 14 – Activity: Threat Mapping (Assessment)**

### In Small Groups:

Match each threat to a failed security goal:

| Threat                   | Security Goal Impacted |
| ------------------------ | ---------------------- |
| Ransomware               | Availability           |
| Unauthorized file access | Confidentiality        |
| Malware modification     | Integrity              |
| Unlogged admin actions   | Accountability         |

📌 This activity prepares you for:

* Quizzes
* Labs
* Real-world troubleshooting

---

## **Slide 15 – Re-Assessment: Quick Check**

**Answer silently:**

1. Which security goal is hardest to maintain?
2. Which threat seems most likely in a small business?
3. Which failures are technical vs human?

These reflections help you identify:

* Knowledge gaps early
* Areas to focus on in labs

---

## **Slide 16 – Closure: 3-2-1 Reflection**

Before next class, write:

* **3 things** you learned about Windows security
* **2 threats** you didn’t realize were so common
* **1 question** you have about securing Windows systems

This reflection:

* Feeds your portfolio
* Prepares you for hands-on labs

---

## **Slide 17 – Looking Ahead to Week 2**

### Next Week:

**OS Hardening & Patch Management**

You will:

* Harden a Windows system
* Apply updates strategically
* See how patching prevents real attacks

> **Key Transition:**
> Now that you understand *why* systems fail, we move into *how to prevent it*

---
