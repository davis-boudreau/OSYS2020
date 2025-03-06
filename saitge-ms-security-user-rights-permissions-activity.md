# **In-Class Activity: Changing User Permissions in Windows**  
**Course:** OSYS 2020 – Windows Security  
**Topic:** Configuring User Permissions and Testing Access Control  
**Time Required:** 60–75 minutes  
**Objective:** Students will configure, modify, and test **NTFS file and folder permissions** and **User Rights Assignments** on a local Windows computer.  

---

## **Activity Overview**  
In this hands-on activity, students will:  
1. **Create new user accounts** and assign them to groups.  
2. **Set NTFS permissions** on a folder.  
3. **Modify user rights assignments** using `secpol.msc`.  
4. **Test and verify** permissions by logging in with different users.  

---

## **Materials Needed**  
- A **Windows computer** with administrator privileges.  
- At least two **local user accounts** for testing.  

---

## **Step 1: Create Test User Accounts** (10 minutes)  

### **Create Two Local Users**  
1. Open **Computer Management** (`Win + X → Computer Management` or `compmgmt.msc`).  
2. Navigate to **Local Users and Groups → Users**.  
3. Right-click **Users** and select **New User**.  
4. Create two users:  
   - **User1** (password: `P@ssword1`)  
   - **User2** (password: `P@ssword2`)  
5. Click **Create**, then **Close**.  

### **Create a Security Group**  
1. In **Computer Management**, go to **Groups**.  
2. Right-click **Groups** → **New Group**.  
3. Name the group **"RestrictedUsers"**.  
4. Click **Add**, type `User1`, and click **OK**.  
5. Click **Create**, then **Close**.  

---

## **Step 2: Create a Test Folder & Apply NTFS Permissions** (15 minutes)  

### **Create a Folder for Testing**  
1. Open **File Explorer** (`Win + E`).  
2. Navigate to ``C:\Users\Public\Documents` and create a new folder named **TestFolder**.  

### **Set NTFS Permissions**  
1. Right-click **TestFolder** → **Properties** → **Security** tab.  
2. Click **Advanced** → **Disable inheritance** → Choose **Convert inherited permissions**.  
3. Click **Edit** and remove **Users** group (optional).  
4. Click **Add** → **Select a principal** → Type `User1` → Click **OK**.  
5. Assign **Read & execute, List folder contents, and Read** permissions.  
6. Click **OK** → **Apply**.  
7. Click **Add** → Type `User2` → Click **OK**.  
8. Assign **Full control** to `User2`.  
9. Click **Apply → OK**.  

### **Expected Outcome**  
- `User1` should be able to read the folder but **cannot modify or delete files**.  
- `User2` should have **full control** over the folder.  

---

## **Step 3: Modify User Rights Assignments** (15 minutes)  

### **Restrict User1 from Logging in Locally**  
1. Press `Win + R`, type **secpol.msc**, and hit **Enter**.  
2. Navigate to **Local Policies → User Rights Assignment**.  
3. Find **Deny log on locally** and double-click it.  
4. Click **Add User or Group** → Type `User1` → Click **OK**.  
5. Click **Apply → OK**.  

### **Give User2 the Ability to Shut Down the System**  
1. In `secpol.msc`, find **Shut down the system**.  
2. Double-click it, then click **Add User or Group**.  
3. Type `User2` and click **OK**.  
4. Click **Apply → OK**.  

### **Force Policy Update**  
Run the following command in **Command Prompt (Admin)** to apply changes:  
```powershell
gpupdate /force
```

---

## **Step 4: Testing User Permissions** (20 minutes)  

### **Test NTFS Permissions**  
1. **Log in as User1**:  
   - Open `C:\Users\Public\Documents\TestFolder`.  
   - Try to **create or delete a file** (should **fail**).  
   - Try to **open and read a file** (should **work**).  
2. **Log in as User2**:  
   - Open `C:\Users\Public\Documents\TestFolder`.  
   - Try to **create and delete a file** (should **work**).  

### **Test User Rights Assignments**  
1. **Log in as User1** and check if **login is denied**.  
2. **Log in as User2** and try to **shut down the computer**:  
   - Press `Ctrl + Alt + Del`.  
   - Click **Shut down**.  
   - If successful, the privilege change worked.  

---

## **Step 5: Review & Discussion** (10 minutes)  

### **Discussion Questions**  
1. Why was `User1` denied access to ``C:\Users\Public\Documents\TestFolder` for editing?  
2. What happened when `User1` tried to log in locally?  
3. How does adding `User2` to the **"Shut down the system"** policy affect security?  
4. What other **privileges** or **restrictions** could be implemented in a real-world scenario?  

### **Bonus Challenge (Optional)**  
- Restrict `User2` from **deleting** files but allow **writing new ones** in `C:\Users\Public\Documents\TestFolder`.  
- Use PowerShell to query and modify user rights instead of `secpol.msc`.  

---

## **Conclusion**  
This activity teaches students how to **set and test user permissions** using NTFS security and User Rights Assignment policies. It reinforces **least privilege principles**, access control, and Windows security best practices.  
