# **Lab: Creating and Managing Group Policy Objects (GPOs)**  
**Course:** OSYS2020 – Windows Security  
**Topic:** Managing Local Security Policies and Group Policy Objects (GPOs)  

---

## **Objective**  
By the end of this activity, students will:  
✅ Understand how to **create and manage Group Policy Objects (GPOs)**.  
✅ Learn to enforce **security policies** using GPOs.  
✅ Apply **restrictions** to control user access and system settings.  
✅ Test and verify **GPO enforcement**.  

---

## **Prerequisites**  
- A **Windows 10/11 or Windows Server** computer (GPO works best in a domain but can be tested locally).  
- At least **two local user accounts** (`UserA` and `UserB`).  
- **Administrator privileges** on the system.  

---

# **Step 1: Accessing the Group Policy Editor (`gpedit.msc`)**  

1. Press `Win + R`, type **gpedit.msc**, and press **Enter**.  
2. Group Policy Editor will open, showing:  
   - **Computer Configuration** (applies to all users on the machine).  
   - **User Configuration** (applies to specific user accounts).  

---

# **Step 2: Create a GPO to Restrict Access to Control Panel**  

1. **Navigate to:**  
   - **User Configuration → Administrative Templates → Control Panel**.  
2. **Double-click** **Prohibit access to Control Panel and PC settings**.  
3. **Set it to Enabled**, then click **Apply → OK**.  
4. **Test:**  
   - Log in as `UserA` and attempt to open the **Control Panel** (should be blocked).  

---

# **Step 3: Apply a GPO to Restrict USB Access (Only on VM's with USB Host Integration)**  

1. **Navigate to:**  
   - **Computer Configuration → Administrative Templates → System → Removable Storage Access**.  
2. **Double-click** **All Removable Storage classes: Deny all access**.  
3. **Set it to Enabled**, then click **Apply → OK**.  
4. **Test:**  
   - Insert a **USB drive** and try accessing it (should be denied).  

---

# **Step 4: Apply a GPO to Set a Custom Login Message (Legal Notice)**  

1. **Navigate to:**  
   - **Computer Configuration → Windows Settings → Security Settings → Local Policies → Security Options**.  
2. **Find and modify:**  
   - **Interactive logon: Message title for users attempting to log on** → Set it to `"OSYS2020 Security Policy"`.  
   - **Interactive logon: Message text for users attempting to log on** → Set it to `"Unauthorized access is prohibited."`  
3. **Apply changes and restart the computer** to see the login message.  

---

# **Step 5: Testing the Group Policy Changes**  

1. **Run the command** `gpupdate /force` to apply the policy immediately.  
2. **Log out and log back in as `UserA` and `UserB`** to test restrictions:  
   ✅ **Control Panel should be blocked** for `UserA`.  
   ✅ **USB access should be denied**.  
   ✅ **Custom login message should appear** before signing in.  

---

# **Step 6: Reflection & Discussion**  

- **What is the difference between Computer Configuration and User Configuration?**  
- **How does GPO enforcement enhance security?**  
- **How can these policies be applied in a domain environment?**  

---

# **Bonus Challenge **  
✅ **Enable auditing for policy changes:**  
   - Navigate to **Security Settings → Local Policies → Audit Policy**.  
   - Enable **Audit Policy Change** to log changes in Event Viewer (`eventvwr.msc`).  

✅ **Apply GPO using PowerShell:**  
   ```powershell
   gpupdate /force
   Get-GPO -All
   ```
---

## **Expected Learning Outcomes**  
✅ Understand how to **create and apply GPOs**.  
✅ Configure **security restrictions** using Group Policy.  
✅ Test and troubleshoot **GPO application**.  
✅ Discuss **best practices for managing GPOs**.  

