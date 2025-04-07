# Simulate a Windows security incident

## To test your ability to detect and mitigate a **brute-force attack** on a Windows machine using an attacker VM, follow these steps:

---

## **Step 1: Configure the Windows Target (Victim)**
### **1.1 Enable RDP on Windows**
On the **Windows VM (target system):**  
1. Open **System Properties** (`sysdm.cpl` from Run dialog).
2. Go to **Remote** tab.
3. Check **Allow remote connections to this computer**.
4. Click **Select Users** and add a test user with RDP access.

### **1.2 Set Up a Weak User Account**
1. Open **Command Prompt (Admin)** and create a test user:
   ```powershell
   net user attacker test123 /add
   ```
2. Assign the user RDP permissions:
   ```powershell
   net localgroup "Remote Desktop Users" attacker /add
   ```
3. Lower account lockout settings to allow detection:
   ```powershell
   net accounts /lockoutthreshold:5 /lockoutduration:15
   ```
   - This locks the account after **5 failed attempts** for **15 minutes**.

---

## **Step 2: Launch Brute-Force Attack from Attacker VM**
From the **Kali Linux VM (attacker system)**:

### **2.1 Use Hydra to Attack RDP Login**
Hydra is a powerful brute-force tool. Use the following command:
```bash
hydra -V -l attacker -P /usr/share/wordlists/rockyou.txt rdp://<WINDOWS_IP>
```
- `-l attacker`: Specifies the username.  
- `-P <wordlist>`: Uses a password dictionary.  
- `rdp://<WINDOWS_IP>`: Targets the RDP service.

### **2.2 Alternative: Use Ncrack**
Another option is `ncrack`:
```bash
ncrack -vv -U userlist.txt -P passlist.txt rdp://<WINDOWS_IP>
```
This tests multiple users against RDP.

---

## **Step 3: Detect the Attack Using Windows Logs**
On the **Windows VM**, monitor security logs.

### **3.1 Open Event Viewer**
1. Press `Win + R`, type `eventvwr.msc`, and press **Enter**.
2. Navigate to **Windows Logs > Security**.

### **3.2 Filter for Failed Logins**
1. Click **Filter Current Log**.
2. Select **Event ID 4625** (**Failed Logon Attempts**).
3. Check timestamps and source IP (attacker's IP should appear).

### **3.3 Monitor Logs with PowerShell**
Run the following command to detect failed login attempts:
```powershell
Get-WinEvent -LogName Security | Where-Object { $_.Id -eq 4625 } | Select-Object TimeCreated, Message
```
- This displays all **failed login events**.

---

## **Step 4: Mitigate the Attack**
### **4.1 Enable Account Lockout**
If not already done:
```powershell
net accounts /lockoutthreshold:5 /lockoutduration:30
```
This locks the account for **30 minutes** after **5 failures**.

### **4.2 Block Attacker's IP in Windows Firewall**
Use PowerShell:
```powershell
New-NetFirewallRule -DisplayName "Block Attacker IP" -Direction Inbound -Action Block -RemoteAddress <ATTACKER_IP>
```

### **4.3 Enable RDP Network Level Authentication (NLA)**
1. Open **System Properties** (`sysdm.cpl`).
2. Go to **Remote** tab.
3. Check **Allow connections only from computers running Remote Desktop with Network Level Authentication**.
4. Apply the settings.

### **4.4 Disable RDP if No Longer Needed**
To prevent further attacks:
```powershell
Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server" -Name "fDenyTSConnections" -Value 1
```

---

## **Step 5: Document Findings and Reflection**
- Take **screenshots** of:
  - Brute-force attack output in **Kali Linux**.
  - Failed login attempts in **Event Viewer**.
  - Mitigation steps (firewall block, account lockout, PowerShell commands).
- **Reflection Questions:**
  - What indicators helped you detect the attack?
  - How would you automate detection and response in an enterprise setting?
  - What additional security controls could prevent brute-force attacks?

---

### **Conclusion**
This lab allows students to experience **real-world cybersecurity scenarios**, reinforcing incident detection and response techniques. 🔐