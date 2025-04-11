## Implementing Role-Based Access Control (RBAC) on a Windows workstation involves using built-in tools and features to manage user roles and permissions. Here’s a step-by-step guide:

### 1. **Create User Roles**
1. **Using Local Users and Groups**:
   - Open `Computer Management` (right-click on `This PC` > `Manage`).
   - Navigate to `System Tools > Local Users and Groups > Groups`.
   - Create new groups for different roles (e.g., Admins, Users).

2. **Using PowerShell**:
   - Open PowerShell as an administrator.
   - Create a new group:
     ```powershell
     New-LocalGroup -Name "Admins" -Description "Administrators Group"
     ```

### 2. **Assign Users to Roles**
1. **Using Local Users and Groups**:
   - In `Computer Management`, add users to the groups you created.
   - Right-click on the group > `Add to Group` > `Add` > enter the user names.

2. **Using PowerShell**:
   - Add users to the group:
     ```powershell
     Add-LocalGroupMember -Group "Admins" -Member "User1","User2"
     ```

### 3. **Set Permissions**
1. **File and Folder Permissions**:
   - Right-click on a file or folder > `Properties` > `Security` tab.
   - Edit permissions to allow or deny access based on the user roles.

2. **Using PowerShell**:
   - Set permissions for a folder:
     ```powershell
     $acl = Get-Acl "C:\MyFolder"
     $permission = "DOMAIN\User1","FullControl","Allow"
     $accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule $permission
     $acl.SetAccessRule($accessRule)
     Set-Acl "C:\MyFolder" $acl
     ```

### 4. **Test RBAC Implementation**
1. **Log in as Different Users**:
   - Log in with different user accounts to verify access permissions.
   - Ensure users can only access resources appropriate for their roles.

2. **Check Event Logs**:
   - Open Event Viewer and navigate to `Windows Logs > Security`.
   - Look for events related to access attempts and permissions.

