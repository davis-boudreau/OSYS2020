# **Lab: Creating and Applying GPOs to Manage Password Complexity and Audit Policies**  
**Course:** OSYS2020 – Windows Security  
**Topic:** Managing Local Security Policies and Group Policy Objects (GPOs)  
**Subtopic:** Creating and Applying GPOs to Manage Password Complexity and Audit Policies  

---

## **Objective**  
By the end of this activity, students will:  
✅ Understand **Group Policy Objects (GPOs)** and their role in security management.  
✅ Configure and apply **password complexity policies** using GPOs.  
✅ Set up **audit policies** to track authentication events.  
✅ Test the effectiveness of the policies using real login scenarios.  

---

## **Prerequisites**  
- A **Windows 10/11 or Windows Server** computer.  
- **Administrator privileges** on the system.  
- Basic knowledge of **Active Directory Group Policies** (for domain environments) or **Local Group Policies** (for standalone systems).  

---

# **Part 1: Configuring Password Complexity Using GPO**  

## **Step 1: Open Group Policy Management Editor**  
1. **For Standalone Systems (Windows 10/11, non-domain):**  
   - Press `Win + R`, type **gpedit.msc**, and press **Enter**.  
   - Navigate to:  
     ```
     Computer Configuration → Windows Settings → Security Settings → Account Policies → Password Policy
     ```
2. **For Domain Environments (Windows Server with Active Directory):**  
   - Open **Group Policy Management** (`gpmc.msc`).  
   - Right-click the **domain** or an **organizational unit (OU)** where the policy should apply and select **Create a GPO in this domain, and Link it here**.  
   - Name the GPO **"Password Policy"** and click **OK**.  
   - Right-click the GPO and select **Edit**.  
   - Navigate to the same **Password Policy** location as above.  

---

## **Step 2: Configure Password Complexity Policies**  
1. **Enforce Password History:**  
   - Double-click **"Enforce password history"** → Set to **24** passwords remembered.  

2. **Maximum Password Age:**  
   - Double-click **"Maximum password age"** → Set to **60** days.  

3. **Minimum Password Age:**  
   - Double-click **"Minimum password age"** → Set to **1** day.  

4. **Minimum Password Length:**  
   - Double-click **"Minimum password length"** → Set to **12** characters.  

5. **Password Must Meet Complexity Requirements:**  
   - Double-click **"Password must meet complexity requirements"** → **Enable**.  
   - This enforces a mix of **uppercase, lowercase, numbers, and special characters**.  

6. **Store Passwords Using Reversible Encryption:**  
   - Double-click **"Store passwords using reversible encryption"** → **Disable** (for security).  

7. **Click Apply → OK**.  

---

## **Step 3: Apply and Test Password Policy**  
1. Run the following command in **Command Prompt (Admin)** to apply the changes:  
   ```
   gpupdate /force
   ```
2. Try changing the password for a local user (`UserA`) using:  
   ```
   Ctrl + Alt + Del → Change a password
   ```
   - If the new password doesn't meet complexity requirements, Windows should **reject** it.  

3. Attempt to reuse an old password → Windows should **prevent reuse**.  

---

# **Part 2: Configuring Audit Policies Using GPO**  

## **Step 4: Configure Audit Policies to Track Logon Events**  
1. Open **Group Policy Editor** (`gpedit.msc` or `gpmc.msc`).  
2. Navigate to:  
   ```
   Computer Configuration → Windows Settings → Security Settings → Local Policies → Audit Policy
   ```
3. **Enable Audit Logon Events:**  
   - Double-click **"Audit logon events"** → Check **Success and Failure** → Click **Apply → OK**.  

4. **Enable Audit Account Logon Events:**  
   - Double-click **"Audit account logon events"** → Check **Success and Failure** → Click **Apply → OK**.  

5. **Enable Audit Policy Changes:**  
   - Double-click **"Audit policy change"** → Check **Success and Failure** → Click **Apply → OK**.  

6. **Click Apply → OK**.  

---

## **Step 5: Apply and Test Audit Policy**  
1. Run the following command to enforce the policy:  
   ```
   gpupdate /force
   ```
2. Log in to **UserA** and enter the wrong password **three times**.  
3. Log in to **UserB** successfully.  
4. Open **Event Viewer** (`eventvwr.msc`):  
   - Navigate to:  
     ```
     Windows Logs → Security
     ```
   - Look for **event IDs 4624 (Successful login), 4625 (Failed login attempt), and 4672 (Special privileges assigned to new logon)**.  
   - Verify that **logon attempts and failures are logged**.  

---

# **Step 6: Verify Policy Enforcement Using PowerShell**  
Run the following command to verify applied policies:  
```powershell
secedit /export /cfg C:\Users\Public\SecurityPolicy.txt
notepad C:\Users\Public\SecurityPolicy.txt
```
- Review the exported policy file for password and audit settings.  

---

# **Reflection & Discussion**  
- **Why are password complexity policies essential?**  
- **What security risks exist if passwords are too short or simple?**  
- **How can auditing help detect unauthorized access attempts?**  
- **How do attackers try to bypass password and auditing policies?**  

---

# **Bonus Challenge**  
✅ **Configure Account Lockout Policies**:  
   - Navigate to:  
     ```
     Computer Configuration → Windows Settings → Security Settings → Account Policies → Account Lockout Policy
     ```
   - Set:  
     - **Account lockout threshold:** `5` failed attempts.  
     - **Account lockout duration:** `15` minutes.  
     - **Reset account lockout counter after:** `10` minutes.  

✅ **Monitor Audit Logs Using PowerShell**:  
   ```powershell
   Get-WinEvent -LogName Security | Where-Object { $_.Id -eq 4625 } | Format-Table TimeCreated, Message -AutoSize
   ```
   - This will display **failed login attempts** and timestamps.  

---

# **Expected Learning Outcomes**  
✅ Configure and enforce **password complexity policies** via GPO.  
✅ Implement and test **audit policies** to track authentication events.  
✅ Use **Event Viewer and PowerShell** to monitor security logs.  
✅ Understand the impact of **password and account lockout policies**.  
