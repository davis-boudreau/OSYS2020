# **In-Class Activity: Securing Shared Resources and Drives**  
**Course:** OSYS2020 – Windows Security  
**Topic:** Securing Shared Folders and Drives  


## **Objective**  
By the end of this activity, students will:  
✅ Understand how to **create shared folders and drives** in Windows.  
✅ Apply **NTFS permissions** to secure shared resources.  
✅ Configure **Share Permissions** to restrict access.  
✅ Test security configurations by simulating **unauthorized and authorized access**.  

---

## **Prerequisites**  
- A Windows computer (Windows 10/11 or Windows Server)  
- At least two local user accounts (e.g., `UserA` and `UserB`)  
- Administrator privileges  

---

## **Activity Overview**  
Students will:  
1. **Create a shared folder** and configure NTFS permissions.  
2. **Apply share-level permissions** to control network access.  
3. **Restrict access to unauthorized users.**  
4. **Test access control from different user perspectives.**  

---

# **Step 1: Create a Secure Shared Folder**  

1. **Create a new folder**:  
   - Open **File Explorer** and navigate to `C:\`  
   - Create a new folder named **SecureShare**  

2. **Right-click on the folder → Properties → Sharing tab**  
   - Click **Advanced Sharing…**  
   - Check **Share this folder**  
   - Set the **Share Name** to `SecureShare`  
   - Click **Permissions**  
   - **Remove** the `Everyone` group (for security reasons)  
   - Click **Add**, enter `UserA`, and grant **Read** permissions  
   - Click **Add**, enter `UserB`, and grant **Full Control**  
   - Click **OK** and **Close**  

---

# **Step 2: Configure NTFS Permissions**  

1. **Go to the “Security” tab** in the folder properties  
   - Click **Edit** → **Add**  
   - Enter `UserA` and **grant Read & Execute permissions**  
   - Enter `UserB` and **grant Full Control**  
   - Click **Apply** and **OK**  

2. **Remove unnecessary permissions**:  
   - Select `Everyone` (if present) and click **Remove**  

---

# **Step 3: Test Access from Different Users**  

1. **Log in as UserA** and attempt to:  
   ✅ Open files in `\\ComputerName\SecureShare` (should work)  
   ❌ Create or modify files (should be denied)  

2. **Log in as UserB** and attempt to:  
   ✅ Open, create, and delete files (should be allowed)  

3. **Try accessing from an unauthorized user**:  
   - Log in as a third user who was not given access  
   - Attempt to open `\\ComputerName\SecureShare`  
   - **Expected result:** Access should be denied  

---

# **Step 4: Reflection & Discussion**  

- **Why did UserA have read-only access?**  
- **Why was UserB able to make changes?**  
- **How does removing ‘Everyone’ improve security?**  
- **What is the difference between Share and NTFS permissions?**  

---

# **Bonus Challenge**  
1. **Enable auditing** to log access attempts:  
   - Open **Local Security Policy** (`secpol.msc`)  
   - Go to **Local Policies → Audit Policy**  
   - Enable **Audit Object Access (Sucess)**  
   - Check Event Viewer (`eventvwr.msc`) for access logs  

2. **Restrict access based on time** using Group Policy  
   - `gpedit.msc` → **User Rights Assignment** → Set time-based access rules  

---

## **Expected Learning Outcomes**  
✅ Differentiate between **NTFS and Share Permissions**  
✅ Secure shared folders using **least privilege principles**  
✅ Test access restrictions and **troubleshoot permission issues**  
✅ Understand **the importance of removing default access groups**  

