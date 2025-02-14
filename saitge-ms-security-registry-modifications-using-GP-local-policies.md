# **Lab: Registry Modifications for Security Using Group Policy and Local Security Policies**  
**Course:** OSYS2020 – Windows Security  
**Topic:** Managing Local Security Policies and Group Policy Objects (GPOs)  
**Subtopic:** Registry Modifications for Security  

---

## **Objective**  
By the end of this activity, students will:  
✅ Understand how to use **Registry Editor (`regedit`)** to modify security settings.  
✅ Learn how to apply **security-related registry changes** using **GPO (`gpedit.msc`)**.  
✅ Test the effectiveness of **registry modifications** on system security.  
✅ Understand how to **backup and restore** the Windows Registry before making changes.  

---

## **Prerequisites**  
- A **Windows 10/11 or Windows Server** computer.  
- At least **two local user accounts** (`UserA` and `UserB`).  
- **Administrator privileges** on the system.  
- Understanding of the **Windows Registry structure** (HKEY_LOCAL_MACHINE, HKEY_CURRENT_USER, etc.).  

---

## **Step 1: Backup the Registry Before Making Changes**  

1. **Open Registry Editor:**  
   - Press `Win + R`, type **regedit**, and press **Enter**.  

2. **Create a backup of the Registry:**  
   - Click **File → Export**.  
   - Name the file **RegistryBackup.reg** and save it to a safe location (e.g., Desktop).  

---

## **Step 2: Restrict Access to Task Manager via Registry**  

1. **Navigate to:**  
   ```
   HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System
   ```
2. **Create a new DWORD value:**  
   - Right-click **System** → **New → DWORD (32-bit) Value**.  
   - Name it **DisableTaskMgr**.  
   - Double-click it and set its value to `1`.  

3. **Apply Changes:**  
   - Restart the computer or **log out and log back in** to test.  
   - Try opening Task Manager (`Ctrl + Shift + Esc`)—it should be disabled.  

---

## **Step 3: Disable USB Storage via Registry**  

1. **Navigate to:**  
   ```
   HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\USBSTOR
   ```
2. **Modify the "Start" DWORD value:**  
   - Double-click **Start** and change its value to **4** (Disables USB storage).  

3. **Apply Changes:**  
   - Restart the computer or **run `gpupdate /force`**.  
   - Insert a USB drive to test whether access is blocked.  

---

## **Step 4: Enforce Registry Modifications via Group Policy**  

1. **Open Group Policy Editor (`gpedit.msc`)**  
   - Press `Win + R`, type **gpedit.msc**, and press **Enter**.  

2. **Create a GPO to disable Task Manager:**  
   - Navigate to:  
     ```
     User Configuration → Administrative Templates → System → Ctrl+Alt+Del Options
     ```
   - Double-click **Remove Task Manager** and set it to **Enabled**.  
   - Click **Apply → OK**.  

3. **Create a GPO to disable USB storage:**  
   - Navigate to:  
     ```
     Computer Configuration → Administrative Templates → System → Removable Storage Access
     ```
   - Double-click **All Removable Storage classes: Deny all access** and set it to **Enabled**.  

4. **Apply Group Policies:**  
   - Run the command:  
     ```
     gpupdate /force
     ```
   - Restart the computer to ensure the policies take effect.  

---

## **Step 5: Testing the Registry and Group Policy Changes**  

1. **Log in as `UserA` and `UserB`** and attempt to:  
   ✅ Open **Task Manager** (`Ctrl + Shift + Esc`) – should be disabled.  
   ✅ Insert a **USB drive** – access should be denied.  

2. **Verify the applied settings in Registry Editor (`regedit`)**  
   ✅ Check the values of `DisableTaskMgr` and `Start` under their respective registry paths.  

3. **Check if policies were applied using PowerShell:**  
   ```powershell
   Get-GPResultantSetOfPolicy -ReportType HTML -Path C:\Users\Public\GPOReport.html
   ```

---

## **Step 6: Restoring the Registry (If Needed)**  

1. **Open Registry Editor (`regedit`)**.  
2. **Click File → Import**.  
3. **Select the `RegistryBackup.reg` file** and click **Open**.  
4. **Restart the system to revert the changes**.  

---

# **Reflection & Discussion**  

- **Why is modifying the Windows Registry risky?**  
- **When should policies be enforced using GPO instead of manual registry edits?**  
- **How can attackers exploit registry settings, and how do security policies prevent this?**  
- **What are other security-related registry settings that can be modified?**  

---

# **Bonus Challenge**  

✅ **Disable Windows Command Prompt (cmd.exe) using the Registry:**  
   - Navigate to:  
     ```
     HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\System
     ```
   - Create a new **DWORD (32-bit) Value** named **DisableCMD** and set it to **1**.  
   - Test by trying to open `cmd.exe`.  

✅ **Automate Registry Edits with PowerShell:**  
   ```powershell
   # Disable Task Manager
   Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableTaskMgr" -Value 1

   # Disable USB Storage
   Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\USBSTOR" -Name "Start" -Value 4
   ```

---

## **Expected Learning Outcomes**  
✅ Modify **security settings** using the Windows Registry (`regedit`).  
✅ Enforce **Registry-based security** using Group Policy (`gpedit.msc`).  
✅ Understand **risk management** when making registry changes.  
✅ Test and validate **registry modifications** in a security environment.  
