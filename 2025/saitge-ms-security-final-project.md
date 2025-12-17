# Project Title: Windows Security Management

## **Overview**  

This final hands-on reflective assignment will assess your ability to apply security concepts from OSYS 2020 in a simulated Windows environment. You will work within **GNS3** to create and secure a Windows system following best practices from each of the five course sections. Your final submission will include a **report** with screenshots, configuration details, and a reflection on the security measures you implemented.  

---  

## **Assignment Instructions**  

## **Environment Setup (Pre-requisite)**  

1. **Create a new GNS3 project** named `w#-OSYS2020-Final`.  
2. Deploy a **Windows 10 or Windows Server VM** in GNS3.  
3. Deploy an Kali Linux VM **attacker VM** (Please refer to saitge-ms-security-simulate-security incident.md)
4. Document your initial setup (VM versions, IP configurations, snapshots, etc.).  

---  

## **Section 1: Operating System Hardening**  

**Objective:** Apply fundamental hardening techniques to reduce the attack surface of the Windows OS.  

### **Tasks:**  

1. **Remove Unnecessary Services**  
   - Disable unused Windows services.
   - Justify why certain services were disabled.  

2. **Configure Windows Defender & Firewall**  
   - Enable **Windows Defender Real-time Protection** and configure a scheduled scan.  
   - Create inbound/outbound rules in **Windows Firewall** for application security.  

3. **Update & Patch Management**  
   - Install the latest Windows updates.  
   - Configure **WSUS (Windows Server Update Services)** if applicable.  

## **Reflection Prompt:**  

- How did reducing services improve security?  
- What challenges did you face configuring the firewall?  

---  

## **Section 2: Access Control & Privilege Management**  

**Objective:** Implement least privilege and control access to critical resources.  

### **Tasks:**  

1. **User & Group Management**  
   - Create multiple user accounts with appropriate roles (Admin, Standard User, Guest).  
   - Implement **Role-Based Access Control (RBAC)**.  

2. **Configure Local & Domain Group Policies**  
   - Set password policies (complexity, expiration, lockout).  
   - Restrict privilege escalation (disable local admin accounts where possible).  

3. **Enable BitLocker for Drive Encryption**  
   - Encrypt a non-system drive and test access restrictions.
   - Adding a Secondary Disk to Your GNS3 VM
        - Shutdown your VM.
        - Right-click on your VM within the project.
        - Select Configure.
        - Choose HDD.
        - Under the section HDB (Primary Slave), select Create.
        - For Binary and Format, use the default Qcow2. Click Next.
        - For Qcow2 options, use the default settings. Click Next.
        - IMPORTANT: For Size and Location, change the file name in the File Location field. Replace the default name with W#.qcow2. Keep the default size.
        - Click Finish.
        - Click Apply.
        - Start the VM.
        - The new drive D should appear in your Windows OS.
        - Format the Volume to NTFS.
        - Your new disk should now be ready for use.  

### **Reflection Prompt:**  

- How does RBAC enhance security?  
- What would happen if an administrator account was compromised?  

---  

## **Section 3: Security Policies & Threat Mitigation**  

**Objective:** Define security policies and mitigate threats through system configuration.  

### **Tasks:**  

1. **Configure Account Lockout Policy**  
   - Set up policies to mitigate brute-force attacks.  
   - Demonstrate failed login attempts leading to lockout.  

2. **Enable Windows Defender Application Control (WDAC)**  
   - Whitelist and blacklist applications.  
   - Test blocking unauthorized software execution.  

3. **Deploy Security Baselines**  
   - Apply **Microsoft Security Baseline** policies via Group Policy.  

### **Reflection Prompt:**  

- How does enforcing security baselines standardize security?  
- What weaknesses remain even after configuring these policies?  

---  

## **Section 4: Network Security & Automation**  

**Objective:** Secure network access and implement automation to enforce security policies.  

### **Tasks:**  

1. **Secure RDP Access**  
   - Change default RDP port.  
   - Implement **Network Level Authentication (NLA)**.  

2. **Deploy PowerShell Scripts for Security Automation**  
   - Write a PowerShell script to enforce firewall rules.  
   - Create a script to detect unauthorized admin logins.  

3. **Configure VPN for Secure Remote Access**  
   - Set up a **Windows VPN Server** with PPTP or L2TP/IPsec.  
   - Test client connectivity.  

### **Reflection Prompt:**  

- How did automation improve security management?  
- What security concerns exist with RDP access?  

---  

## **Section 5: Incident Response & Log Analysis**  

**Objective:** Monitor system events and respond to security incidents.  

### **Tasks:**  

1. **Configure Windows Event Logging**  
   - Enable **Auditing for Logon Events, Policy Changes, and Privilege Escalation**.  
   - Use **Event Viewer** to analyze security logs.  

2. **Use PowerShell to Extract Security Logs**  
   - Write a script to filter logs for **failed login attempts**.  
   - Analyze patterns in the logs and document suspicious activity.  

3. **Simulate a Security Incident**  
   - Please refer to saitge-ms-security-simulate-security incident.md
   - Conduct a brute-force attack from the attacker VM.  
   - Detect and mitigate the attack using logs and security tools.  

### **Reflection Prompt:**  

- What indicators helped you identify the security incident?  
- How would an organization respond to such an attack?  

---  

## **Final Deliverable & Submission Guidelines**  

- **Report Format:**  
  - **Title Page** (Student Name, ID, Course Code)  
  - **Introduction** (Explain your approach)  
  - **Screenshots & Explanations for Each Section**  
  - **Reflection Responses**  
  - **Conclusion** (Lessons learned and recommendations)  

- **Submission:** Upload your **final report** and **GNS3 project file** to the designated course platform (Brightspace).  

---  

### **Grading Rubric (100 Points Total)**  

| Section | Criteria | Points |  
|---------|----------|--------|  
| **OS Hardening** | Properly configured services, firewall, and updates | 20 |  
| **Access Control** | User roles, policies, and encryption correctly implemented | 20 |  
| **Security Policies** | Enforced policies and threat mitigation strategies | 20 |  
| **Network Security** | Secured RDP, VPN setup, PowerShell automation | 20 |  
| **Incident Response** | Log analysis, detection, and response actions | 20 |  

---  

### **Conclusion**  

This assignment is designed to integrate all course concepts into a practical, real-world scenario. Your ability to apply, reflect, and document your security implementations will demonstrate your competency in securing Windows environments. **Good luck!**
