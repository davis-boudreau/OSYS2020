Here is your **revised quiz** with **no duplicates** and **numbered sequentially**:

---

# **OSYS2020: Windows Security - Advanced Quiz (Standalone Windows Systems Only)**  

## **A. Multiple Choice**  

1. Which tool allows you to configure **Local Group Policy settings** on a Windows computer?  
   a) `secpol.msc`  
   **b) `gpedit.msc`**  
   c) `regedit.exe`  
   d) `control.exe`  

2. Which setting in **Local Security Policy (`secpol.msc`)** specifies how long a user must wait before retrying a failed login?  
   a) Maximum password age  
   b) Minimum password length  
   **c) Account lockout duration**  
   d) Password expiration warning  

3. A user reports being unable to modify a file despite having **Modify** permission. What is the most likely reason?  
   a) The user is a member of the **Administrators** group  
   **b) The "Deny Write" permission is applied to another group the user belongs to**  
   c) The **Full Control** permission overrides all other settings  
   d) The NTFS file system is disabled  

4. Which NTFS permission allows a user to **view folder contents** but **not modify any files**?  
   a) Modify  
   **b) Read & Execute**  
   c) Write  
   d) Full Control  

5. When setting **shared folder permissions**, which of the following provides the **most restrictive** level of access?  
   **a) Read**  
   b) Change  
   c) Full Control  
   d) Modify  

6. If a **local GPO** contradicts an **NTFS permission**, which setting takes precedence?  
   a) NTFS permissions  
   b) Local GPO  
   c) Registry settings  
   **d) The most restrictive setting**  

7. What happens if the **"Deny" permission** is applied to a user in NTFS settings?  
   a) The user will have Full Control  
   **b) The user is denied access, even if other groups grant access**  
   c) The user can still read files but not modify them  
   d) The Deny setting is ignored if the user is an administrator  

---

## **B. Multiple Answer**  

8. Which **password policies** can be enforced using Local Group Policy Editor (`gpedit.msc`)?  
   **a) Minimum password length**  
   **b) Enforce password history**  
   **c) Maximum password age**  
   d) Require smart card login  
   **e) Password complexity requirements**  

9. When configuring **User Rights Assignment** in Local Security Policy (`secpol.msc`), which of the following can be restricted?  
   **a) Log on locally**  
   **b) Access this computer from the network**  
   c) Change desktop wallpaper  
   **d) Shut down the system**  
   **e) Modify firmware environment values**  

10. When securing **shared resources** on a standalone Windows machine, which steps are recommended?  
   **a) Remove the "Everyone" group from share permissions**  
   **b) Set NTFS permissions instead of relying only on share permissions**  
   c) Allow full control for all users  
   **d) Use auditing to track access attempts**  
   **e) Disable the Guest account**  

---

## **C. True or False**  

11. Local GPO settings apply **only to the computer they are configured on** and do not affect networked systems.  
   **True**  

12. NTFS permissions apply even if a folder is accessed over the network.  
   **True**  

13. A **user with administrative privileges** can always access all files, even if **explicit Deny permissions** are set.  
   **False**  

14. The **Account Lockout Policy** can be configured in Local Security Policy (`secpol.msc`) to prevent brute-force login attempts.  
   **True**  

---

## **D. Short Answer**  

15. The command used to manually **refresh Local Group Policy settings** on a Windows computer is:  
   **`gpupdate /force`**  

16. The **Windows log file** that records **failed login attempts** is called:  
   **Security Log**  

17. The **Registry Editor (`regedit.exe`)** is mainly used to:  
   **Modify system settings at a low level**  

18. The **NTFS permission** that allows a user to create and delete **files** in a folder but **not modify existing files** is:  
   **Write**  

---

## **E. Matching**  

19. Match each **security setting** with its correct Local GPO location:  

   - **Password complexity** → Local Computer Policy → Computer Configuration → Windows Settings → Security Settings → Account Policies → Password Policy  
   - **Audit logon failures** → Local Computer Policy → Computer Configuration → Windows Settings → Security Settings → Local Policies → Audit Policy  
   - **User rights assignment** → Local Computer Policy → Computer Configuration → Windows Settings → Security Settings → Local Policies → User Rights Assignment  
   - **NTFS folder permissions** → File Explorer → Right-click folder → Properties → Security tab  

---

## **F. Ordering**  

20. Arrange the following steps in the correct **order** to configure a **local security policy** for **password complexity**:  

   1. Open `secpol.msc`  
   2. Navigate to **Account Policies → Password Policy**  
   3. Double-click **"Password must meet complexity requirements"**  
   4. Select **Enabled**  
   5. Click **OK** and close the window  
   6. Restart the computer (if required)  

21. Arrange the following steps to **secure a shared folder using NTFS permissions**:  

   1. Right-click the folder and select **Properties**  
   2. Go to the **Security** tab  
   3. Click **Edit** to modify permissions  
   4. Remove **unnecessary users** from the permission list  
   5. Assign **Read & Execute** or **Modify** based on requirements  
   6. Click **Apply**, then **OK**  

---

This version removes **duplicate questions** and **ensures a clear numbering sequence.** 🚀 Would you like me to refine anything further?