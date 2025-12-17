# **OSYS2020: Windows Security**  
## **Lab: Configuring and Managing Windows Defender**  

### **Lab Overview**  
Windows Defender is the built-in antivirus and security solution in Windows. It includes real-time protection, firewall controls, ransomware protection, and advanced threat defense mechanisms. In this lab, students will configure and manage Windows Defender through the Windows Security app, Group Policy, PowerShell, and Windows Defender Firewall.  

By completing this lab, students will:  
- Understand the components of Windows Defender.  
- Configure and manage real-time protection.  
- Customize scanning options.  
- Implement exclusions and exceptions.  
- Use PowerShell to automate Defender configurations.  
- Configure Windows Defender Firewall rules.  
- Respond to and analyze security threats.  

### **Lab Requirements**  
- Windows 10 or Windows 11 (or a virtual machine with Windows installed).  
- Administrator privileges.  
- PowerShell and Group Policy Editor access.  

---

## **Part 1: Windows Defender Overview**  
### **Task 1: Verify Windows Defender Status**  
1. Open **Windows Security** from the Start menu.  
2. Navigate to **Virus & threat protection**.  
3. Verify that real-time protection, cloud-based protection, and automatic sample submission are enabled.  
4. Take a screenshot of the status and note any disabled features.  

**Challenge:** If any features are disabled, research and explain why they might be turned off and how to enable them.  

---

## **Part 2: Configuring Windows Defender Settings**  
### **Task 2: Enable and Configure Real-Time Protection**  
1. In **Windows Security**, navigate to **Virus & threat protection settings**.  
2. Enable or verify **Real-time protection** is on.  
3. Enable **Cloud-delivered protection** and **Automatic sample submission**.  

### **Task 3: Configure Exclusions**  
1. Scroll down to **Exclusions** and click **Add or remove exclusions**.  
2. Add an exclusion for a specific **folder** (e.g., `C:\ExcludedFolder`).  
3. Add an exclusion for a specific **file** (e.g., `C:\ExcludedFolder\test.exe`).  
4. Take a screenshot of the exclusions list.  

**Challenge:** Explain when exclusions should be used and why adding too many exclusions can be a security risk.  

---

## **Part 3: Performing and Managing Scans**  
### **Task 4: Run a Quick Scan and a Full Scan**  
1. In **Windows Security**, go to **Virus & threat protection**.  
2. Click **Quick scan** and document the results.  
3. Click **Scan options**, select **Full scan**, and run it.  
4. Record the time taken and any detected threats.  

### **Task 5: Run a Scan Using PowerShell**  
1. Open PowerShell as Administrator.  
2. Run the following command to perform a quick scan:  
   ```powershell
   Start-MpScan -ScanType QuickScan
   ```
3. Run a full scan:  
   ```powershell
   Start-MpScan -ScanType FullScan
   ```
4. Take a screenshot of the output.  

**Challenge:** Research and run a custom Defender scan using PowerShell to scan only a specific folder.  

---

## **Part 4: Managing Defender with PowerShell**  
### **Task 6: Check Defender Status Using PowerShell**  
1. Open PowerShell as Administrator.  
2. Run the following command to check Defender’s real-time protection status:  
   ```powershell
   Get-MpComputerStatus | Select RealTimeProtectionEnabled
   ```
3. Run the following command to check the last scan time:  
   ```powershell
   Get-MpComputerStatus | Select QuickScanEndTime
   ```
4. Document your results.  

### **Task 7: Enable or Disable Features Using PowerShell**  
1. Disable real-time protection:  
   ```powershell
   Set-MpPreference -DisableRealtimeMonitoring $true
   ```
2. Re-enable real-time protection:  
   ```powershell
   Set-MpPreference -DisableRealtimeMonitoring $false
   ```
3. Confirm the setting change using:  
   ```powershell
   Get-MpComputerStatus | Select RealTimeProtectionEnabled
   ```
4. Take screenshots of the output.  

**Challenge:** Research and configure Defender to block **PUAs (Potentially Unwanted Applications)** using PowerShell.  

---

## **Part 5: Configuring Windows Defender Firewall**  
### **Task 8: Manage Firewall Rules**  
1. Open **Windows Security > Firewall & network protection**.  
2. Click **Advanced settings** to open the **Windows Defender Firewall with Advanced Security** console.  
3. Navigate to **Inbound Rules** and find an existing rule for an application (e.g., Remote Desktop).  
4. Modify the rule to **block** connections.  
5. Create a **new outbound rule** to block all outbound traffic for a specific application (e.g., `notepad.exe`).  

### **Task 9: Configure Firewall Rules Using PowerShell**  
1. Open PowerShell as Administrator.  
2. Run the following command to create a new firewall rule blocking an application:  
   ```powershell
   New-NetFirewallRule -DisplayName "Block Notepad" -Direction Outbound -Program "C:\Windows\System32\notepad.exe" -Action Block
   ```
3. Verify the rule:  
   ```powershell
   Get-NetFirewallRule -DisplayName "Block Notepad"
   ```
4. Remove the rule:  
   ```powershell
   Remove-NetFirewallRule -DisplayName "Block Notepad"
   ```
5. Take screenshots of each step.  

**Challenge:** Research how to configure Defender Firewall to allow only specific applications and block all others.  

---

## **Part 6: Simulating and Analyzing Threats**  
### **Task 10: Simulate a Malware Detection**  
1. Download the **EICAR test file** (a safe antivirus test file).  
   - Open Notepad.  
   - Paste the following text exactly:  
     ```
     X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
     ```
   - Save it as `testvirus.com`.  
2. Try running the file and observe Defender’s reaction.  
3. Take screenshots of the detection and how Defender responds.  

### **Task 11: Review Windows Defender Security Logs**  
1. Open **Event Viewer**.  
2. Navigate to **Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational**.  
3. Find an event related to a **malware detection** or scan result.  
4. Take a screenshot and document the event details.  

**Challenge:** Research how to configure **Windows Defender Attack Surface Reduction (ASR) Rules** to block scripts, executables, and Office macros.  

---

## **Lab Submission and Reflection**  
1. Submit a document with the following:  
   - Screenshots of each completed task.  
   - Answers to each challenge question.  
   - A summary of what you learned.  
   - A reflection on how Windows Defender contributes to system security.  

---

### **Assessment Criteria**  
| Task | Points |  
|------|--------|  
| Verified Windows Defender status | 5 |  
| Configured real-time protection and exclusions | 10 |  
| Performed scans (GUI & PowerShell) | 10 |  
| Used PowerShell to manage Defender settings | 10 |  
| Configured Firewall rules (GUI & PowerShell) | 10 |  
| Simulated malware detection | 10 |  
| Analyzed security logs | 10 |  
| Answered challenge questions | 15 |  
| Submitted a well-organized report | 10 |  
| **Total** | **80** |  

---

### **Conclusion**  
This lab provides hands-on experience configuring and managing Windows Defender, an essential security tool for protecting Windows systems. By automating tasks through PowerShell and analyzing Defender’s security logs, students gain real-world skills applicable to cybersecurity and system administration roles.