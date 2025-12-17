**OSYS2020: Windows Security**  
**Practical Assignment: Automating Windows Security Audits with Powershell**  
---

### **Overview**
In this assignment, you will develop PowerShell scripts to automate security configurations and audits on a Windows Server deployed in Microsoft Azure Cloud Services. 

This will provide hands-on experience in analyzing system security settings, and generating a comprehensive security report.

You will complete the following tasks:
1. **Enable Remote Desktop Connection (RDC) for the user "itadmin".**
2. **Generate a detailed Windows Server Security Audit Report.**

You must submit both PowerShell scripts via the LMS (Brightspace).

---

## **Task 1: Enabling Remote Desktop for "itadmin"**
### **Instructions:**
- Write a PowerShell script named **w#_allow_RDC_for_itadmin.ps1** that grants the user "itadmin" permission to access the system via Remote Desktop.
- Ensure the script:
  - Adds "itadmin" to the "Remote Desktop Users" group.
  - Adjusts firewall settings to allow Remote Desktop Protocol (RDP) connections.
  - Enables Remote Desktop if it is disabled.
  - Includes error handling to prevent failures during execution.
- **Submission:** Upload **w#_allow_RDC_for_itadmin.ps1** to Brightspace.

---

## **Task 2: Windows Server Security Audit Report**
### **Instructions:**
- Write a PowerShell script named **w#_win_srv_security_audit.ps1** that gathers security-related system information and outputs a structured security report.
- The script should:
  - Run security checks on the system.
  - Format the results for readability.
  - Implement error handling for reliability.
  - Log findings to a file for further analysis.
- **Submission:** Upload **w#_win_srv_security_audit.ps1** to Brightspace.

### **Security Report Structure & Required Checks**
The security report should include the following sections and checks:

#### **1. System Information & Security Overview**
   - Check Windows Version & Build.
   - Check if the system has pending security updates.
   - Get the system’s patch level.

#### **2. Windows Defender Security Status**
   - Retrieve Windows Defender’s overall security status.
   - Check if Real-Time Protection is enabled.
   - Identify the last update time for Windows Defender.

#### **3. Windows Firewall Configuration**
   - Check the status of all firewall profiles.
   - List all active firewall rules.
   - Verify if Remote Desktop Connection (RDC) is allowed through the firewall.

#### **4. User & Account Security**
   - Determine if User Account Control (UAC) is enabled.
   - List all users with administrative privileges.
   - List all local user accounts.
   - Check if the built-in Administrator account is enabled.

#### **5. Security Policies & Password Settings**
   - Check password policy settings (minimum/maximum age, complexity, etc.).
   - Verify if the guest account is disabled.
   - Check the status of Remote Desktop (RDP).

#### **6. Windows Security Event Logs**
   - Retrieve recent security events, including login attempts and access violations.
   - Identify failed login attempts.
   - Check if audit logging is enabled.

---

## **Evaluation Criteria**
| Criteria | Description | Points |
|----------|------------|--------|
| **Script Functionality** | Correct implementation of tasks and security checks. | 40 |
| **Error Handling** | Implementation of `try`/`catch` statements to handle errors gracefully. | 20 |
| **Script Readability & Formatting** | Clear comments, structured output, and proper indentation. | 20 |
| **Completeness of Security Audit** | All required checks are included in the report. | 20 |
| **Total** | | **100** |

---

## **Submission Guidelines**
- Name your scripts using the format **w#_allow_RDC_for_itadmin.ps1** and **w#_win_srv_security_audit.ps1**, replacing "w#" with your student ID.
- Submit both scripts via Brightspace before the deadline.
- Ensure your scripts run without errors on a Windows Server environment.

---

## **Resources**
- saitge-ms-security-powershell-cheatsheet.md
- Microsoft PowerShell Documentation: [https://docs.microsoft.com/en-us/powershell/](https://docs.microsoft.com/en-us/powershell/)
- Windows Security Best Practices: [https://docs.microsoft.com/en-us/windows/security/](https://docs.microsoft.com/en-us/windows/security/)

---

## **Conclusion**
This assignment provides practical experience in using PowerShell for security automation. By writing and executing these scripts, you will gain insights into securing Windows environments, improving system monitoring, and mitigating security risks efficiently.