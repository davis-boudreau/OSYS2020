# **OSYS2020 – Windows Security**

## **Workshop 02: Operating System Hardening through Patch Management, Updates, and Service Packs**

---

## **1. Assignment Details**

| Field                | Information                                             |
| -------------------- | ------------------------------------------------------- |
| **Workshop Title**   | Workshop 02 – OS Hardening with Patch Management        |
| **Course Code**      | OSYS2020                                                |
| **Course Title**     | Windows Security                                        |
| **Instructor**       | Davis Boudreau                                          |
| **Assignment Type**  | Guided Hands-On Workshop                                |
| **Weight**           | Not Graded (Formative – Required for later evaluations) |
| **Estimated Effort** | 2–3 hours                                               |
| **Delivery Mode**    | In-class / Remote (GNS3 + VPN)                          |
| **Due**              | End of Week 2                                           |

---

## **2. Overview / Purpose / Objectives**

### **Overview**

In this workshop, you will perform **operating system hardening** by reviewing, applying, and validating **patch management controls** on the Windows systems you built in **Workshop 00**.

Rather than treating updates as a background task, you will analyze:

* patch status
* update history
* reboot requirements
* security impact of missing updates

This workshop reinforces the idea that **patch management is the first and most effective security control** in Windows environments.

---

### **Purpose**

The purpose of this workshop is to help you develop:

* disciplined patching habits
* security-focused administrative thinking
* an understanding of how unpatched systems are exploited

You will learn that most attacks do not rely on “advanced hacking,” but on **known, unpatched vulnerabilities**.

---

### **Objectives**

By the end of this workshop, you will be able to:

* Assess patch status on Windows Server and Windows 11
* Apply security and quality updates correctly
* Identify pending reboots and incomplete patch states
* Explain the security risk of delayed patching
* Relate patching decisions to security goals

---

## **3. Learning Outcomes Addressed**

This workshop supports the following course learning outcomes:

* **LO1:** Describe the steps required to harden an operating system
* **LO2:** Interpret and manipulate components of Windows security
* **LO3:** Implement Windows security administration practices

---

## **4. Assignment Description / Use Case**

### **Use Case**

You are responsible for maintaining the Windows domain you built in **Workshop 00**.

Although the environment is functional, it has not yet been **secured**.

Your task is to:

* evaluate the current update state
* apply missing patches
* confirm that systems are fully updated
* understand the security implications of patching decisions

> In real environments, patching is usually the **first response** after a security review.

---

## **5. Tasks / Instructions**

You will complete the following tasks on **both systems**:

* **OSYS-DC01 (Windows Server – Domain Controller)**
* **OSYS-W11-01 (Windows 11 Client)**

---

### **Part A – Review Current Patch Status**

On **each system**:

1. Open **Windows Update** settings.
2. Record:

   * Current update status
   * Date of last successful update
   * Whether updates are paused or deferred
3. Review **Update History**:

   * Installed updates
   * Failed updates
   * Pending updates

✅ **Checkpoint:** You can clearly describe the patch state of each system.

---

### **Part B – Identify Security vs Feature Updates**

Using the update history, identify examples of:

* Security updates
* Quality (cumulative) updates
* Feature updates (if applicable)

Answer:

* Which updates address **security vulnerabilities**?
* Which updates improve **stability or performance**?
* Why are feature updates treated differently in enterprises?

---

### **Part C – Apply Updates and Manage Reboots**

On **each system**:

1. Ensure updates are **enabled**.
2. Install all available updates.
3. Reboot the system **if required**.
4. After reboot, re-check update status.

Answer:

* Was a reboot required?
* What happens if a system is patched but not rebooted?
* Why do administrators schedule reboots carefully?

✅ **Checkpoint:** System reports **“You’re up to date.”**

---

### **Part D – Validate Patch Health**

Use built-in tools to confirm patch success:

* Windows Update status page
* Update history timestamps
* System uptime (optional)

Document:

* Any failed updates
* Any updates that required multiple reboots

---

### **Part E – Risk Analysis**

Answer the following questions:

1. What types of attacks are possible on unpatched systems?
2. Which security goals does patch management support?

   * Confidentiality
   * Integrity
   * Availability
   * Accountability
3. Why is patch management often delayed in organizations?

---

### **Part F – Reflection**

Write short reflective responses:

* Which system required more updates, the server or the client?
* Why is patching especially critical for a domain controller?
* Would you prioritize patching over installing antivirus? Why?

---

## **6. Deliverables**

Submit **one document** (Word) containing:

* Patch status summary for both systems
* Evidence of updates applied (screenshots optional)
* Answers to analysis and reflection questions

**File name format:**
`StudentID_OSYS2020_Workshop02_PatchManagement`

---

## **7. Reflection Questions**

Include responses to:

* How does patch management reduce attack surface?
* What risks exist when patching is delayed?
* How does patching support overall OS hardening?

---

## **8. Assessment & Rubric**

### **Assessment Type**

* **Formative (Not Graded)**

### **Success Criteria**

* Accurate assessment of update status
* Successful application of updates
* Clear explanation of patch-related risk
* Thoughtful reflection demonstrating security reasoning

Instructor feedback will prepare you for:

* Quizzes
* Baseline analysis
* Domain hardening evaluations

---

## **9. Submission Guidelines**

* Submit via **Brightspace**
* One document per student
* Screenshots are optional but encouraged
* Partial submissions accepted with documented blockers

---

## **10. Resources / Equipment**

* GNS3-based Windows domain (Workshop 00)
* Windows Update (Server + Client)
* Course slides (Week 2)
* Microsoft Learn – Windows Update Fundamentals

---

## **11. Academic Policies**

* Collaboration for troubleshooting is encouraged
* Submitted work must reflect your own environment
* Academic integrity policies apply

---

## **12. Copyright Notice**

© Nova Scotia Community College
For educational use within OSYS2020 only.

---
