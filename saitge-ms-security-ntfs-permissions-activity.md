# **In-Class Activity: Understanding NTFS Permissions**  
**Course:** OSYS 2020 – Windows Security  
**Topic:** NTFS Permissions  
**Time Required:** 45–60 minutes  
**Objective:** Students will configure, test, and analyze NTFS file and folder permissions on a Windows system.  

---

## **Preparation (Instructor)**
- Ensure students have access to a **Windows computer** (real or virtual machine).  
- Each student should log in with an **administrator** account or be able to create standard user accounts.  
- If necessary, provide a brief overview of **NTFS (New Technology File System)** and its security model.  

---

## **Step-by-Step Activity**  

### **Step 1: Create User Accounts** (10 minutes)  
1. Open **Computer Management** (`Win + X → Computer Management` or `compmgmt.msc`).  
2. Navigate to **Local Users and Groups → Users**.  
3. Create two new local users:  
   - **User1** (password: `P@ssw0rd1`)  
   - **User2** (password: `P@ssw0rd2`)  
4. Ensure both accounts are in the **Users** group (not Administrators).  

---

### **Step 2: Create a Test Folder & Set Initial Permissions** (10 minutes)  
1. Open **File Explorer** (`Win + E`).  
2. Navigate to `C:\Users\Public\Documents\` and create a new folder called `TestPermissions`.  
3. Right-click inside the location and select **New → Folder**. Name it **SecureData**.  You now should have `C:\Users\Public\Documents\TestPermissions\SecureData`
4. Right-click **SecureData** → **Properties** → **Security** tab.  
5. Click **Advanced** → Uncheck **"Include inheritable permissions from this object’s parent"**. Click **Disable inheritance** when prompted.  There should be two options.  Select option 2 as detailed below:
- Option 1 - Convert Inherited Permission into explicit permissions on this object.
    - This option will take all the permissions that are inherited from parent objects and convert them into explicit permissions on the current object. This means the object will retain the same permissions, but they will no longer be linked to the parent objects.

- Option 2 - Remove all inherited permission from this object.
    - This option will remove all permissions that the object inherits from parent objects. After this, you will need to manually set the permissions you want for this object.
---

### **Step 3: Assign NTFS Permissions** (15 minutes)  
1. Click **Add** → **Select a principal** → Type `User1` → Click **OK**.  
2. Set **User1’s permissions**:  
   - Check **Modify, Read & execute, List folder contents, Read, and Write**.  
   - Click **OK**.  
3. Click **Add** → **Select a principal** → Type `User2` → Click **OK**.  
4. Set **User2’s permissions**:  
   - Only check **Read & execute** and **List folder contents**.  
   - Click **OK**.  
5. Click **Apply** → **OK** → Close all windows.  

---

### **Step 4: Testing NTFS Permissions** (15 minutes)  
1. **Log in as User1** and navigate to `C:\Users\Public\Documents\TestPermissions\SecureData`.  
   - Try to **create a new text file** (should work).  
   - Try to **edit and save the file** (should work).  
2. **Log in as User2** and navigate to `C:\Users\Public\Documents\TestPermissions\SecureData`.  
   - Try to **open and read the file** (should work).  
   - Try to **edit and save the file** (should fail).  
   - Try to **delete the file** (should fail).  
3. **Log back in as an Administrator**, open **Properties → Security**, and discuss what happened.  

---

### **Step 5: Modify and Inherit Permissions** (10 minutes)  
1. As an Administrator, go back to the **SecureData** folder properties.  
2. Click **Advanced** → **Enable inheritance**.  
3. Apply and close, then **log in as User2** and check if anything changed.  
4. Test what User2 can do now.  

---

## **Discussion & Key Takeaways**  
- What happened when inheritance was disabled?  
- Why couldn’t User2 modify or delete files?  
- How do NTFS permissions affect file security in Windows?  
- What happens when permissions are combined from multiple sources?  

**Optional Challenge:**  
- **Scenario:** A new user (User3) needs **read-only** access to a **specific file** in `SecureData`, but not the rest of the folder.  
- Ask students to modify permissions to allow this.  

---

This hands-on activity reinforces the concepts of NTFS permissions, inheritance, and access control, all essential for **Windows security hardening**.