# Understanding NTFS File Permissions

## Introduction
The NTFS (New Technology File System) permissions in Windows allow administrators to control how users and groups access files and folders. Properly configuring NTFS permissions ensures data security by limiting unauthorized access and maintaining data integrity.

This tutorial will explain NTFS file permissions, how they work, and how to configure them effectively.

## NTFS Permission Types
NTFS permissions are divided into two categories:

1. **Basic Permissions**
2. **Advanced Permissions**

### Basic Permissions
Basic permissions consist of predefined sets of advanced permissions that simplify the permission-setting process. The standard basic permissions are:

- **Full Control** – Grants all permissions, including modifying permissions and taking ownership.
- **Modify** – Allows reading, writing, and deleting files or folders.
- **Read & Execute** – Permits reading files and running executables.
- **List Folder Contents** – Allows listing files and subfolders but not opening files.
- **Read** – Grants the ability to view files but not modify them.
- **Write** – Allows modifying file contents and creating new files.

### Advanced Permissions
Advanced permissions provide granular control over access and include:

- **Traverse Folder / Execute File** – Navigate through folders and run executable files.
- **List Folder / Read Data** – View folder contents and read file data.
- **Read Attributes** – View basic file attributes.
- **Read Extended Attributes** – View additional file metadata.
- **Create Files / Write Data** – Create new files and modify file contents.
- **Create Folders / Append Data** – Create subfolders and add data to existing files.
- **Write Attributes** – Modify file attributes (e.g., read-only, hidden).
- **Write Extended Attributes** – Modify extended metadata.
- **Delete Subfolders and Files** – Delete all contents within a folder.
- **Delete** – Remove a file or folder.
- **Read Permissions** – View permission settings.
- **Change Permissions** – Modify permission settings.
- **Take Ownership** – Take ownership of files and folders.

## NTFS Permission Inheritance
By default, files and folders inherit permissions from their parent folder. This means that if a folder has specific permissions, any file or subfolder inside it will automatically receive the same permissions unless explicitly changed.

### Overriding Inheritance
To modify inherited permissions:
1. Right-click a file or folder and select **Properties**.
2. Navigate to the **Security** tab.
3. Click **Advanced**.
4. Click **Disable inheritance** and choose:
   - **Convert inherited permissions into explicit permissions** – Keeps existing permissions but makes them non-inheritable.
   - **Remove all inherited permissions** – Clears inherited permissions.

## Configuring NTFS Permissions
To modify NTFS permissions:

### Using the GUI
1. Right-click a file or folder and select **Properties**.
2. Click the **Security** tab.
3. Click **Edit** to modify permissions.
4. Select a user or group and check the desired permissions.
5. Click **OK** to apply changes.

### Using PowerShell
To set NTFS permissions via PowerShell, use the `icacls` command.

#### Example 1: Grant Read and Execute Permission
```powershell
icacls "C:\Folder" /grant User:(RX)
```

#### Example 2: Remove All Permissions for a User
```powershell
icacls "C:\Folder" /remove User
```

#### Example 3: Reset NTFS Permissions
```powershell
icacls "C:\Folder" /reset
```

## Effective Permissions
When multiple users and groups have permissions on a file or folder, the **effective permissions** determine what actions a user can perform.

- **Deny permissions** override Allow permissions.
- Permissions assigned to a user are combined with group permissions.
- The most restrictive permission takes precedence.

## Best Practices
1. **Follow the Principle of Least Privilege** – Grant only the necessary permissions.
2. **Use Groups Instead of Individual Users** – Assign permissions to groups to simplify management.
3. **Avoid Using Deny Unless Necessary** – Deny permissions can cause conflicts if users belong to multiple groups.
4. **Regularly Review Permissions** – Conduct periodic audits to ensure appropriate access control.
5. **Document Permission Changes** – Maintain a log of permission modifications for security tracking.

