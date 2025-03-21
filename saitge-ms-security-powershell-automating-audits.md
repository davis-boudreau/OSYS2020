# OSYS2020: Windows Security
## Lab: Automating Windows Security Audits with PowerShell

### **Lab Overview**
In this lab, you will learn how to use PowerShell to automate security audits in a Windows environment. You will:

- Understand PowerShell basics and scripting best practices.
- Use PowerShell to audit security configurations, including Windows Defender, Firewall, user accounts, and event logs.
- Debug and improve an existing PowerShell security script.
- Implement robust error handling using `try` and `catch`.
- Reflect on the benefits of automation in Windows security.

---

## **Part 1: PowerShell Basics & Best Practices**
### **Task 1: Open PowerShell as Administrator**
1. Click **Start**, type `PowerShell`, right-click **Windows PowerShell**, and select **Run as administrator**.
2. Verify PowerShell’s execution policy:
   ```powershell
   Get-ExecutionPolicy
   ```
3. If the policy is **Restricted**, allow script execution temporarily:
   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope Process
   ```
4. Confirm the change:
   ```powershell
   Get-ExecutionPolicy
   ```

### **Task 2: Basic PowerShell Commands for Security Checks**
#### **Check Windows Defender Status**
```powershell
try {
    Get-MpComputerStatus | Select-Object AMRunningMode, AntivirusEnabled
} catch {
    Write-Host "Error retrieving Windows Defender status: $_" -ForegroundColor Red
}
```
#### **Check Firewall Status**
```powershell
try {
    Get-NetFirewallProfile | Select-Object Name, Enabled
    foreach ($profile in $firewallStatus) {
        Write-Log "Profile Name: $($profile.Name), Enabled:`$($profile.Enabled)"
        }
} catch {
    Write-Log "Error retrieving Firewall status: $_" -ForegroundColor Red
}
```
#### **List Local Administrators**
```powershell
try {
    Get-LocalGroupMember -Group "Administrators"
} catch {
    Write-Host "Error retrieving local administrators: $_" -ForegroundColor Red
}
```
#### **Check for Failed Login Attempts**
```powershell
try {
    Get-WinEvent -LogName Security | Where-Object { $_.Id -eq 4625 } | Select-Object TimeCreated, Message -First 5
} catch {
    Write-Host "Error retrieving failed login attempts: $_" -ForegroundColor Red
}
```

---

## **Part 2: Hands-On Security Audit with PowerShell**
### **Task 3: Automate Security Auditing with Error Handling**
Create a PowerShell script that audits security settings and logs the results with error handling.

#### **Step 1: Create the Script File**
1. Open Notepad and paste the following script:
   ```powershell
   $logFile = "C:\Logs\SecurityAudit.txt"
   function Write-Log {
       param([string]$message)
       "$((Get-Date).ToString('yyyy-MM-dd HH:mm:ss')) - $message" | Out-File -Append -FilePath $logFile
   }
   
   Write-Log "Starting Security Audit"
   
   try {
       $defenderStatus = Get-MpComputerStatus | Select-Object AMRunningMode, AntivirusEnabled
       if ($defenderStatus) {
           Write-Log "Windows Defender Status: $($defenderStatus.AMRunningMode)"
       } else {
           Write-Log "Windows Defender is not running or disabled."
       }
   } catch {
       Write-Log "Error retrieving Windows Defender status: $_"
   }
   
   try {
    Get-NetFirewallProfile | Select-Object Name, Enabled
    foreach ($profile in $firewallStatus) {
        Write-Log "Profile Name: $($profile.Name), Enabled:`$($profile.Enabled)"
        }
    } catch {
    Write-Log "Error retrieving Firewall status: $_" -ForegroundColor Red
    }
   
   try {
       $failedLogins = Get-WinEvent -LogName Security | Where-Object { $_.Id -eq 4625 }
       Write-Log "Failed Login Attempts: $($failedLogins.Count)"
   } catch {
       Write-Log "Error retrieving failed login attempts: $_"
   }
   
   try {
       $admins = Get-LocalGroupMember -Group "Administrators"
       Write-Log "Local Administrators: $admins"
   } catch {
       Write-Log "Error retrieving local administrators: $_"
   }
   
   Write-Log "Security Audit Completed"
   ```
2. Save the file as **C:\SecurityCheck.ps1**.

#### **Step 2: Execute the Script**
Run the script in PowerShell:
```powershell
powershell -ExecutionPolicy Bypass -File C:\SecurityCheck.ps1
```
Check the log file:
```powershell
Get-Content C:\Logs\SecurityAudit.txt
```

---

## **Part 3: Debugging & Improving the Script**
### **Scenario: Debugging the Security Audit Script**
A system administrator reports that the **Windows Defender Status** is returning `null`. You need to debug and fix the script.

### **Task 4: Debugging and Fixing the Script**
1. Run the following command to verify the `Get-MpComputerStatus` output:
   ```powershell
   Get-MpComputerStatus
   ```
2. If it returns `null`, Windows Defender may be disabled. Enable it:
   ```powershell
   Set-MpPreference -DisableRealtimeMonitoring $false
   ```
3. Modify the script to check if Defender is disabled before logging:
   ```powershell
   try {
       $defenderStatus = Get-MpComputerStatus | Select-Object AMRunningMode, AntivirusEnabled
       if ($defenderStatus) {
           Write-Log "Windows Defender Status: $($defenderStatus.AMRunningMode)"
       } else {
           Write-Log "Windows Defender is not running or disabled."
       }
   } catch {
       Write-Log "Error retrieving Windows Defender status: $_"
   }
   ```
4. Save and re-run the script.

---

## **Reflective Summary**
### **Discussion Questions:**
1. What are the advantages of automating security audits with PowerShell?
2. How did implementing error handling improve the reliability of your script?
3. How can you extend this script to provide more security insights?

By completing this lab, you have gained hands-on experience in automating security tasks, debugging scripts, implementing robust error handling, and improving Windows security. Automation with error handling not only saves time but also enhances accuracy and reliability in security management.

