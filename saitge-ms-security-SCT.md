### Lab Activity: Review and Apply Microsoft’s Security Compliance Toolkit (SCT)

#### Objective:
To understand and apply Microsoft’s Security Compliance Toolkit (SCT) and compare security settings before and after applying a security baseline.

#### Materials Needed:
- A Windows-based computer or virtual machine
- Internet access
- Microsoft Security Compliance Toolkit (SCT)
- Administrative access to the system

#### Pre-Lab Preparation:
1. **Download SCT:**
   - Visit the Microsoft Security Compliance Toolkit website and download the latest version of the toolkit.
   - Extract the downloaded files to a convenient location on your computer.

2. **Familiarize with Baselines:**
   - Review the documentation provided with the SCT to understand the different security baselines available (e.g., Windows 10, Windows Server).

#### Lab Steps:

1. **Initial Security Settings Review:**
   - Open the Local Group Policy Editor (`gpedit.msc`) on your system.
   - Navigate through the security settings and document the current configurations for key policies (e.g., password policies, account lockout policies, audit policies).

2. **Apply a Security Baseline:**
   - Open the SCT folder and locate the baseline you wish to apply (e.g., Windows 10 Security Baseline).
   - Use the `LGPO.exe` tool included in the SCT to apply the baseline. For example, run the following command in Command Prompt with administrative privileges:
     ```bash
     LGPO.exe /g <path_to_baseline_folder>
     ```
   - Replace `<path_to_baseline_folder>` with the path to the extracted baseline folder.

3. **Post-Baseline Security Settings Review:**
   - After applying the baseline, open the Local Group Policy Editor again.
   - Navigate through the same security settings as in step 1 and document the new configurations.

4. **Comparison and Analysis:**
   - Compare the security settings documented before and after applying the baseline.
   - Identify and discuss the changes made by the baseline. Consider the following questions:
     - Which settings were tightened or enhanced?
     - Were there any settings that remained unchanged?
     - How do these changes improve the overall security posture of the system?

5. **Reflection:**
   - Reflect on the importance of applying security baselines in an organizational environment.
   - Discuss how regular reviews and updates to security settings can help mitigate potential security risks.

#### Deliverables:
- A report documenting the initial and post-baseline security settings.
- A comparison table highlighting the changes in security settings.
- A reflection section discussing the impact of the applied baseline on system security.

#### Evaluation Criteria:
- **Accuracy:** Correct documentation of security settings before and after applying the baseline.
- **Analysis:** Clear and insightful comparison of the security settings.
- **Reflection:** Thoughtful discussion on the importance and impact of security baselines.
- **Presentation:** Well-organized and clearly written report.

---
