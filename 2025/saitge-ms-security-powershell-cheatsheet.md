### **PowerShell Security Cheat Sheet**  
**Quick Reference for Determining Windows Security Settings**

This cheat sheet provides essential PowerShell commands for auditing and managing Windows security settings, including Defender, Firewall, user accounts, policies, and event logs.  

---

## **🔍 Windows Defender Security Status**
### **Check if Windows Defender is Running**
```powershell
Get-MpComputerStatus | Select-Object AMRunningMode, AntivirusEnabled
```

### **Check Windows Defender’s Real-Time Protection Status**
```powershell
(Get-MpPreference).DisableRealtimeMonitoring
```
🔹 **Returns `False` if real-time protection is enabled**  

### **Enable Real-Time Protection**
```powershell
Set-MpPreference -DisableRealtimeMonitoring $false
```

### **Check When Windows Defender Last Updated**
```powershell
(Get-MpComputerStatus).AntivirusSignatureLastUpdated
```

### **Update Windows Defender Signatures**
```powershell
Update-MpSignature
```

### **Run a Quick Scan**
```powershell
Start-MpScan -ScanType QuickScan
```

### **Run a Full System Scan**
```powershell
Start-MpScan -ScanType FullScan
```

---

## **🔥 Windows Firewall Configuration**
### **Check Firewall Status (All Profiles)**
```powershell
Get-NetFirewallProfile | Select-Object Name, Enabled
```

### **Enable Windows Firewall for All Profiles**
```powershell
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
```

### **List All Active Firewall Rules**
```powershell
Get-NetFirewallRule | Where-Object {$_.Enabled -eq "True"} | Select-Object DisplayName, Direction, Action
```

### **Check if Specific Port is Allowed Through Firewall**
```powershell
Get-NetFirewallRule | Where-Object {$_.LocalPort -eq "3389" -and $_.Enabled -eq "True"}
```
🔹 **Change `3389` to the port you want to check**  

---

## **🛡️ User & Account Security**
### **Check if User Account Control (UAC) is Enabled**
```powershell
(Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System").EnableLUA
```
🔹 **Returns `1` if UAC is enabled, `0` if disabled**  

### **List All Local Users**
```powershell
Get-LocalUser | Select-Object Name, Enabled, LastLogon
```

### **List Members of the Administrators Group**
```powershell
Get-LocalGroupMember -Group "Administrators"
```

### **Check if the Built-in Administrator Account is Enabled**
```powershell
(Get-LocalUser -Name "Administrator").Enabled
```

### **Disable the Built-in Administrator Account (If Enabled)**
```powershell
Disable-LocalUser -Name "Administrator"
```

---

## **🔑 Security Policies & Password Settings**
### **Check Password Policy (Minimum & Maximum Age, Complexity, etc.)**
```powershell
Get-LocalUser | ForEach-Object {net accounts}
```

### **Check If Guest Account is Disabled**
```powershell
(Get-LocalUser -Name "Guest").Enabled
```
🔹 **Returns `False` if disabled, `True` if enabled**  

### **Check Remote Desktop (RDP) Status**
```powershell
(Get-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server").fDenyTSConnections
```
🔹 **Returns `1` if disabled, `0` if enabled**  

### **Disable Remote Desktop (RDP)**
```powershell
Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server" -Name fDenyTSConnections -Value 1
```

---

## **📝 Windows Security Event Logs**
### **View Recent Security Events (Login Attempts, Access Violations)**
```powershell
Get-WinEvent -LogName Security -MaxEvents 10
```

### **Check for Failed Login Attempts**
```powershell
Get-WinEvent -LogName Security | Where-Object { $_.Id -eq 4625 } | Select-Object TimeCreated, Message -First 5
```

### **Check for Successful Logins**
```powershell
Get-WinEvent -LogName Security | Where-Object { $_.Id -eq 4624 } | Select-Object TimeCreated, Message -First 5
```

### **Check If Audit Logging is Enabled**
```powershell
auditpol /get /category:*
```

---

## **🔓 Checking Open Network Ports**
### **List All Open Network Connections**
```powershell
Get-NetTCPConnection | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

### **Check for Open Ports**
```powershell
Test-NetConnection -ComputerName localhost -Port 3389
```
🔹 **Change `3389` to check a specific port**  

---

## **🚀 Security Hardening Actions**
### **Disable SMBv1 (Vulnerable Protocol)**
```powershell
Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force
```

### **Enable BitLocker on Drive C:**
```powershell
Enable-BitLocker -MountPoint "C:" -EncryptionMethod AES256 -UsedSpaceOnly
```

### **Check if BitLocker is Enabled on Any Drive**
```powershell
Get-BitLockerVolume | Select-Object MountPoint, VolumeStatus
```

### **Disable Automatic Execution of Scripts from the Internet**
```powershell
Set-ExecutionPolicy Restricted -Scope LocalMachine
```

---

## **📌 System Information & Security Overview**
### **Check Windows Version & Build**
```powershell
[System.Environment]::OSVersion
```

### **Check If System Has Pending Security Updates**
```powershell
Get-WindowsUpdateLog
```

### **Get System Patch Level**
```powershell
wmic qfe list | Select-String KB
```

---

## **🔄 Automating Security Checks with a Script**
Save this as `SecurityCheck.ps1` to run a quick security audit:
```powershell
$logFile = "C:\Logs\SecurityAudit.txt"
function Write-Log {
    param([string]$message)
    "$((Get-Date).ToString('yyyy-MM-dd HH:mm:ss')) - $message" | Out-File -Append -FilePath $logFile
}

Write-Log "Starting Security Audit"

# Defender Status
$defenderStatus = Get-MpComputerStatus | Select-Object AMRunningMode, AntivirusEnabled
Write-Log "Windows Defender Status: $($defenderStatus.AMRunningMode)"

# Firewall Status
$firewallStatus = Get-NetFirewallProfile | Select-Object Name, Enabled
Write-Log "Firewall Status: $firewallStatus"

# Failed Login Attempts
$failedLogins = Get-WinEvent -LogName Security | Where-Object { $_.Id -eq 4625 }
Write-Log "Failed Login Attempts: $($failedLogins.Count)"

# Local Administrators
$admins = Get-LocalGroupMember -Group "Administrators"
Write-Log "Local Administrators: $admins"

Write-Log "Security Audit Completed"
```
Run the script:
```powershell
powershell -ExecutionPolicy Bypass -File C:\SecurityCheck.ps1
```

---

### **💡 Summary**
This cheat sheet provides PowerShell commands for auditing and managing security settings. It includes:
✅ Windows Defender management  
✅ Firewall status and rules  
✅ User and account security  
✅ Password policies  
✅ System hardening and network security  

Using these commands, administrators can automate security checks, enforce policies, and improve system security.