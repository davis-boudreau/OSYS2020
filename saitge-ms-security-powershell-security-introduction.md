### **OSYS2020: Introduction to Automating Windows Security with PowerShell**  
**Course: OSYS2020 – Windows Security**  
**Module: Automating Windows Security with PowerShell**  

---

## **Learning Objectives**  
By the end of this tutorial and lab, students will be able to:  
1. Understand PowerShell fundamentals and scripting best practices.  
2. Develop secure and efficient PowerShell scripts for automating security tasks.  
3. Debug and improve existing PowerShell security scripts.  
4. Reflect on automation’s role in Windows security administration.  

---

# **Part 1: Introduction to PowerShell for Security Automation**  

## **1.1 PowerShell Basics**  
PowerShell is a powerful scripting language and command-line shell built on the .NET framework. It allows system administrators to automate administrative tasks, including security configuration, system auditing, and compliance enforcement.  

### **Key PowerShell Features for Security**  
- Cmdlets (e.g., `Get-Service`, `Get-Process`)  
- Scripting with `.ps1` files  
- Variables and data types  
- Conditional logic (`if`, `switch`)  
- Loops (`for`, `foreach`, `while`)  
- Functions and modular scripting  
- Error handling (`try/catch`)  

### **Example: Checking Windows Defender Status**  
```powershell
Get-MpComputerStatus | Select-Object AMRunningMode, AntivirusEnabled
```
This command checks whether Windows Defender is running and if antivirus protection is enabled.

---

## **1.2 PowerShell Scripting Best Practices**  
Before automating security tasks, it’s important to follow best practices for writing secure, maintainable, and efficient scripts.

### **PowerShell Best Practices**  
✅ **Use Descriptive Naming**: Use meaningful variable and function names (e.g., `$DefenderStatus` instead of `$x`).  
✅ **Apply Commenting and Documentation**: Use comments to explain purpose and logic (`# This function checks Windows Defender status`).  
✅ **Error Handling**: Use `try/catch` blocks to manage errors gracefully.  
✅ **Avoid Hardcoding Credentials**: Use `Get-Credential` instead of storing passwords in plain text.  
✅ **Code Reusability**: Use functions and modules to avoid redundant code.  
✅ **Logging**: Maintain logs of script actions using `Out-File` or `Write-EventLog`.

### **Example: Secure Script with Error Handling**  
```powershell
try {
    $status = Get-MpComputerStatus | Select-Object AMRunningMode, AntivirusEnabled
    Write-Output "Windows Defender Status: $($status.AMRunningMode)"
} catch {
    Write-Output "Error retrieving Defender status: $_"
}
```

---

# **Part 2: Debugging and Improving an Existing PowerShell Security Script**  

### **Scenario**  
A security administrator wrote a PowerShell script to check and enable Windows Defender real-time protection. However, users report that it sometimes fails without clear errors and does not log its actions.  

**Existing Script (With Issues)**  
```powershell
Set-MpPreference -DisableRealtimeMonitoring $false
Write-Output "Defender real-time protection enabled."
```
**Issues Identified:**  
❌ No error handling—fails silently if execution fails.  
❌ No logging—admins cannot track changes.  
❌ No validation—does not check if Defender is installed.  

### **Improved Script: Adding Debugging and Logging**  
```powershell
$logFile = "C:\Logs\SecurityLog.txt"
function Write-Log {
    param([string]$message)
    "$((Get-Date).ToString('yyyy-MM-dd HH:mm:ss')) - $message" | Out-File -Append -FilePath $logFile
}

try {
    # Check if Windows Defender is installed
    if (Get-Command -Name Set-MpPreference -ErrorAction SilentlyContinue) {
        Set-MpPreference -DisableRealtimeMonitoring $false
        Write-Output "Windows Defender real-time protection enabled."
        Write-Log "Success: Defender real-time protection enabled."
    } else {
        Write-Output "Windows Defender not found on this system."
        Write-Log "Error: Windows Defender is not installed."
    }
} catch {
    Write-Output "Error enabling Defender real-time protection: $_"
    Write-Log "Error: $_"
}
```

### **Key Improvements:**  
✅ **Error Handling**: Prevents silent failures.  
✅ **Logging**: Writes success/error messages to a log file.  
✅ **Validation**: Checks if Defender is installed before running.  

---

# **Part 3: Practical Lab – Automating Security with PowerShell**  

### **Lab Task:**  
Develop a PowerShell script that audits and enforces the following security settings:  
1. Ensures Windows Defender real-time protection is enabled.  
2. Checks for outdated Windows Defender definitions.  
3. Enables the Windows Firewall if disabled.  
4. Logs all actions to a file.  

### **Lab Steps:**  

#### **Step 1: Setup**  
1. Open PowerShell as Administrator.  
2. Create a working directory:  
   ```powershell
   mkdir C:\PowerShellSecurity
   cd C:\PowerShellSecurity
   ```

#### **Step 2: Create the Security Audit Script**  
Use the provided template and enhance it with additional security checks.  

```powershell
$logFile = "C:\Logs\SecurityAudit.txt"

function Write-Log {
    param([string]$message)
    "$((Get-Date).ToString('yyyy-MM-dd HH:mm:ss')) - $message" | Out-File -Append -FilePath $logFile
}

try {
    # Check and enable Defender real-time protection
    if (Get-Command -Name Set-MpPreference -ErrorAction SilentlyContinue) {
        Set-MpPreference -DisableRealtimeMonitoring $false
        Write-Output "Windows Defender real-time protection is enabled."
        Write-Log "Defender real-time protection enabled."
    } else {
        Write-Output "Windows Defender not found."
        Write-Log "Error: Windows Defender not installed."
    }

    # Check for outdated definitions
    $lastUpdate = (Get-MpComputerStatus).AntivirusSignatureLastUpdated
    if ($lastUpdate -lt (Get-Date).AddDays(-7)) {
        Write-Output "Defender signatures are outdated!"
        Write-Log "Warning: Defender definitions outdated."
    } else {
        Write-Output "Defender signatures are up to date."
        Write-Log "Defender definitions up to date."
    }

    # Check and enable Windows Firewall
    if ((Get-NetFirewallProfile -Profile Domain,Public,Private).Enabled -contains $false) {
        Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
        Write-Output "Windows Firewall enabled."
        Write-Log "Windows Firewall enabled."
    } else {
        Write-Output "Windows Firewall is already enabled."
        Write-Log "Windows Firewall was already enabled."
    }
} catch {
    Write-Output "Error in security audit script: $_"
    Write-Log "Error: $_"
}
```

#### **Step 3: Run the Script**  
Save it as `SecurityAudit.ps1` and execute it:  
```powershell
powershell -ExecutionPolicy Bypass -File C:\PowerShellSecurity\SecurityAudit.ps1
```

#### **Step 4: Verify Logs**  
Check `C:\Logs\SecurityAudit.txt` to confirm script execution.

---

# **Reflective Summary**  

PowerShell is a powerful tool for automating security in Windows environments. Through this tutorial, we explored:  
- PowerShell fundamentals and best practices for writing secure scripts.  
- Debugging and improving existing PowerShell scripts for reliability.  
- Automating Windows Defender and Windows Firewall security settings.  

**Reflection Questions:**  
1. What challenges did you face while debugging the existing script?  
2. How does logging improve the maintainability of security scripts?  
3. What additional security tasks could be automated using PowerShell?  

By integrating automation, security administrators can reduce manual workload, ensure consistency, and improve response times to security threats. This lab serves as a foundation for further exploration into PowerShell-based security automation.