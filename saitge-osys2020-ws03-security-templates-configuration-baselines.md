# **OSYS2020 – Windows Security**

## **Workshop 03: Security Templates, Configuration Baselines, and System Hardening Standards**

---

## **1. Assignment Details**

| Field                | Information                                                |
| -------------------- | ---------------------------------------------------------- |
| **Workshop Title**   | Workshop 03 – Security Templates & Configuration Baselines |
| **Course Code**      | OSYS2020                                                   |
| **Course Title**     | Windows Security                                           |
| **Assignment Type**  | Guided Hands-On + Analytical Workshop                      |
| **Weight**           | Not Graded (Formative – Prepares for GPO Enforcement)      |
| **Estimated Effort** | 2–3 hours                                                  |
| **Delivery Mode**    | In-class / Remote (GNS3 + VPN)                             |
| **Prerequisite**     | Workshop 00, Workshop 02                                   |
| **Due**              | End of Week 3                                              |

---

## **2. Overview / Purpose / Objectives**

### **Overview**

In this workshop, you will examine **security templates**, **configuration baselines**, and **system hardening standards** to understand how organizations define and measure security at scale.

Rather than applying controls immediately, you will:

* Explore industry security standards
* Compare baseline recommendations to your domain systems
* Identify gaps between *default*, *patched*, and *hardened* configurations

This workshop emphasizes **analysis before enforcement**, a critical principle in professional security administration.

---

### **Purpose**

The purpose of this workshop is to help you move beyond individual configuration changes and begin thinking in terms of:

* **standards**
* **consistency**
* **measurable security posture**

Most real-world security failures occur not because controls do not exist, but because **standards were never clearly defined or enforced**.

---

### **Objectives**

By the end of this workshop, you will be able to:

* Explain the purpose of security templates and baselines
* Identify reputable system hardening standards
* Compare a Windows system against a baseline
* Identify configuration drift and security gaps
* Relate baseline compliance to security goals

---

## **3. Learning Outcomes Addressed**

This workshop supports the following course learning outcomes:

* **LO1:** Describe steps required to harden an operating system
* **LO2:** Interpret and manipulate Windows security components
* **LO3:** Implement Windows security administration practices

---

## **4. Assignment Description / Use Case**

### **Use Case**

Your organization now has:

* A working Windows domain (Workshop 00)
* Fully patched systems (Workshop 02)

Management asks a new question:

> “How do we know our systems are *secure enough* — and how do we prove it?”

Your task is to **analyze security baselines** and compare them to your current environment in order to:

* identify risk
* support future policy decisions
* prepare for compliance and audits

---

## **5. Tasks / Instructions**

You will analyze the following systems:

* **OSYS-DC01** (Windows Server – Domain Controller)
* **OSYS-W11-01** (Domain-joined Windows 11 client)

---

### **Part A – Understand Security Baselines (Conceptual)**

Answer the following:

1. What is a **security template**?
2. What is a **configuration baseline**?
3. How do templates and baselines differ?
4. Why do organizations define hardening standards before enforcement?

Use examples from:

* Patch management (Workshop 02)
* Domain configuration (Workshop 00)

---

### **Part B – Explore Industry Hardening Standards**

Review **one** of the following baseline sources (as directed by your instructor):

* Microsoft Security Baselines
* CIS Windows Benchmarks
* Instructor-provided baseline excerpts

Identify recommendations related to:

* Password policies
* Account lockout
* Auditing
* User rights and privileges
* Security options

📌 You are not expected to read the entire document.

---

### **Part C – Baseline Comparison (Hands-On Analysis)**

On **each system**, explore:

### **Top 15 Security Settings – Windows Client (Windows 11)**

Windows clients are the **primary entry point** for attackers.
The focus here is **credential protection, privilege control, visibility, and attack surface reduction**.

---

### **1. Minimum Password Length**

* **Baseline:** 12–14 characters
* **Why it matters:** Prevents brute-force and password-spraying attacks
* **Security goal:** Confidentiality

---

### **2. Password Complexity Requirements**

* Mixed character sets
* Blocks dictionary-based attacks
* **Security goal:** Confidentiality

---

### **3. Maximum Password Age**

* **Baseline:** 60–90 days
* Prevents long-term credential reuse
* **Security goal:** Confidentiality

---

### **4. Account Lockout Threshold**

* **Baseline:** 5–10 failed attempts
* Limits automated login attacks
* **Security goal:** Availability + Confidentiality

---

### **5. Account Lockout Duration**

* **Baseline:** 15+ minutes
* Slows attackers without permanently locking users
* **Security goal:** Availability

---

### **6. User Account Control (UAC) Enforcement**

* High or “Always Notify”
* Blocks silent privilege escalation
* **Security goal:** Integrity

---

### **7. Local Administrators Group Membership**

* Minimal, tightly controlled
* Avoid daily-use admin accounts
* **Security goal:** Integrity

---

### **8. Audit Logon Events (Success & Failure)**

* Required for intrusion detection
* **Security goal:** Accountability

---

### **9. Audit Account Management**

* Tracks user and group changes
* Detects persistence attempts
* **Security goal:** Accountability

---

### **10. Disable Guest Account**

* Guest = unauthenticated access
* **Security goal:** Confidentiality

---

### **11. Do Not Display Last Signed-In User**

* Prevents username harvesting
* **Security goal:** Confidentiality

---

### **12. LAN Manager Authentication Level**

* **Baseline:** NTLMv2 only
* Disables legacy authentication
* **Security goal:** Integrity

---

### **13. Windows Defender Real-Time Protection**

* Must be enabled and updated
* Detects commodity malware
* **Security goal:** Integrity

---

### **14. Windows Firewall Enabled (All Profiles)**

* Blocks unsolicited inbound traffic
* **Security goal:** Availability + Integrity

---

### **15. Removable Storage Access Control**

* Restrict or audit USB storage
* Reduces malware and data exfiltration risk
* **Security goal:** Confidentiality + Integrity

---

### **Top 15 Security Settings – Windows Server (Domain Controller)**

Domain controllers protect **identity, authentication, and trust**.
These settings emphasize **containment, monitoring, and blast-radius reduction**.

---

### **1. Minimum Password Length (Stricter Than Clients)**

* **Baseline:** 14–16 characters
* Protects high-value credentials
* **Security goal:** Confidentiality

---

### **2. Account Lockout Threshold (Carefully Tuned)**

* Prevents brute-force attacks
* Avoids administrative lockout
* **Security goal:** Availability + Confidentiality

---

### **3. Limit “Log on Locally” Rights**

* DCs should not be used interactively
* **Security goal:** Integrity

---

### **4. Restrict Remote Desktop Access**

* RDP is a top attack vector
* Limit to approved admins
* **Security goal:** Integrity

---

### **5. Expanded Audit Policies**

* Log:

  * Logon events
  * Account management
  * Privilege use
  * Policy changes
* **Security goal:** Accountability

---

### **6. Audit Directory Service Access**

* Tracks changes to AD objects
* Critical for incident response
* **Security goal:** Accountability

---

### **7. User Rights: “Debug Programs”**

* Allows deep system access
* **Baseline:** Administrators only
* **Security goal:** Integrity

---

### **8. Disable Legacy Authentication Protocols**

* Disable LM
* Restrict NTLM
* Prefer Kerberos
* **Security goal:** Integrity

---

### **9. User Account Control for Built-in Administrator**

* Prevents unrestricted admin execution
* **Security goal:** Integrity

---

### **10. Service Account Privilege Restrictions**

* No interactive logon
* Least privilege only
* **Security goal:** Integrity

---

### **11. Windows Defender / AV Enabled**

* DCs are not exempt from malware
* **Security goal:** Integrity

---

### **12. Windows Firewall Enabled**

* Restrict unnecessary inbound access
* **Security goal:** Availability + Integrity

---

### **13. Secure Boot (Where Supported)**

* Prevents boot-level tampering
* **Security goal:** Integrity

---

### **14. Patch Compliance (Zero Critical Outstanding)**

* DCs must be prioritized
* **Security goal:** Integrity + Availability

---

### **15. Limit Membership of Domain Admins**

* Smaller admin group = lower risk
* **Security goal:** Integrity + Accountability

---

### **Part D – Configuration Drift and Risk Analysis**

For **three (3)** non-compliant settings:

1. Explain why the baseline exists
2. Identify the risk created by non-compliance
3. Identify the affected security goal:

   * Confidentiality
   * Integrity
   * Availability
   * Accountability

Explain how **configuration drift** could cause these settings to change over time.

---

### **Part E – Domain Perspective**

Answer the following:

* Why is enforcing baselines more important in a **domain** than on standalone systems?
* Why should domain controllers have stricter baselines than clients?
* How do baselines support centralized security management?

Relate your answers to **future GPO enforcement**.

---

### **Part F – Reflection**

Write short reflective responses:

* Were you surprised by how many default settings differ from baselines?
* Why do vendors ship systems with permissive defaults?
* What could go wrong if baselines are enforced without testing?

---

## **6. Deliverables**

Submit **one document** (PDF or Word) containing:

* Baseline source used
* Comparison table
* Risk analysis
* Domain perspective responses
* Reflection responses

**File name format:**
`StudentID_OSYS2020_Workshop03_BaselineAnalysis`

---

## **7. Reflection Questions**

Include responses to:

* Why are baselines critical to enterprise security?
* How do baselines support audits and compliance?
* How does baseline analysis prepare you for GPO enforcement?

---

## **8. Assessment & Rubric**

### **Assessment Type**

* **Formative (Not Graded)**

### **Success Criteria**

* Accurate baseline comparison
* Logical risk reasoning
* Correct mapping to security goals
* Thoughtful reflection and analysis

Instructor feedback prepares you for:

* Group Policy enforcement
* User rights management
* Midterm domain hardening

---

## **9. Submission Guidelines**

* Submit via **Brightspace**
* One document per student
* Screenshots optional but encouraged
* Partial submissions accepted with documented blockers

---

## **10. Resources / Equipment**

* OSYS2020 Windows Domain (Workshop 00)
* Patched systems (Workshop 02)
* Local Security Policy tools
* Baseline documentation (as assigned)

---

## **11. Academic Policies**

* Collaboration encouraged for discussion
* Work must reflect your own analysis
* Academic integrity policies apply

---

## **12. Copyright Notice**

© Nova Scotia Community College
For educational use within OSYS2020 only.

---

## **Looking Ahead**

This workshop sets the stage for:

* **Workshop 04:** Local Security Policies, Users, and Privileges
* **Later Workshops:** Group Policy enforcement and compliance monitoring

You are now moving from:

> *“Is the system working?”*
> → *“Is the system consistently secure?”*

---
