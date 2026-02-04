You’re absolutely right — once students have the **top 10**, expanding to **top 15** is the sweet spot:
it adds *real depth* without turning the exercise into noise.

Below is a **carefully curated Top 15 Security Baseline Settings** list for **Windows Clients** and **Windows Servers (Domain Controllers)**, expanded **intentionally** (not padded), and still fully aligned with:

* Workshop 00 (Domain foundations)
* Workshop 02 (Patch management / WSUS thinking)
* Workshop 03 (Baselines before enforcement)
* Upcoming GPO labs

This is **student-facing**, but solid enough to double as an **instructor reference**.

---

# **Top 15 Security Baseline Settings**

## **Windows Clients vs. Windows Servers**

> These settings represent the **highest security impact per configuration change** in real Windows environments.

---

# **A. Top 15 Security Settings – Windows Client (Windows 11)**

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

# **B. Top 15 Security Settings – Windows Server (Domain Controller)**

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

## **How Students Should Use the Top 15 Lists**

For the **Baseline Comparison Worksheet**:

* Choose **5–7 settings**
* Mix **credential**, **privilege**, and **audit** controls
* Prefer settings that:

  * protect identity
  * limit admin power
  * provide visibility
* Ask:

  > “Would I enforce this via Group Policy, and why?”

---
