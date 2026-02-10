# **OSYS2020 – Windows Security**

## **Workshop 04: Local Security Policies, User Accounts, Groups, Rights, and Privileges**

---

## **1. Assignment Details**

| Field                | Information                                               |
| -------------------- | --------------------------------------------------------- |
| **Workshop Title**   | Workshop 04 – Local Security Policies & Privilege Control |
| **Course Code**      | OSYS2020                                                  |
| **Course Title**     | Windows Security                                          |
| **Instructor**       | Davis Boudreau                                            |
| **Assignment Type**  | Guided Hands-On + Policy Analysis Workshop                |
| **Weight**           | Not Graded (Formative – Required for later evaluations)   |
| **Estimated Effort** | 2–3 hours                                                 |
| **Delivery Mode**    | In-class / Remote (GNS3 + VPN)                            |
| **Prerequisite**     | Workshop 00, Workshop 02a, Workshop 03                    |
| **Due**              | End of Week 4                                             |

---

## **2. Overview / Purpose / Objectives**

### **Overview**

In this workshop, you will move from **baseline analysis** (Workshop 03) to **controlled security enforcement** by working directly with:

* Local Security Policies
* User accounts and groups
* User rights and privileges

Rather than applying security broadly or automatically, you will **carefully review, justify, and apply changes** at the **local system level**.

This reflects real-world security practice:

> *Policy enforcement without understanding introduces risk.*

---

### **Purpose**

The purpose of this workshop is to help you:

* Understand how Windows enforces security through **policies and privileges**
* Recognize the difference between **authentication** and **authorization**
* Apply **least privilege** principles safely
* Prepare for **centralized enforcement with Group Policy** in later workshops

This workshop intentionally focuses on **local policy first** to ensure you understand *what* is being enforced before *how* it is enforced centrally.

---

### **Objectives**

By the end of this workshop, you will be able to:

* Navigate and interpret Local Security Policy settings
* Analyze user accounts and group membership
* Modify user rights assignments responsibly
* Relate privilege decisions to security risk
* Validate the impact of policy changes

---

## **3. Learning Outcomes Addressed**

This workshop supports the following course learning outcomes:

* **LO1:** Describe steps required to harden an operating system
* **LO2:** Interpret and manipulate Windows security components
* **LO3:** Implement Windows security administration practices

---

## **4. Assignment Description / Use Case**

### **Use Case**

Your organization now has:

* A working Windows domain (Workshop 00)
* Patched systems (Workshop 02a)
* A defined security baseline (Workshop 03)

Management asks:

> “Can we safely reduce risk by tightening who can do what on our systems?”

Your task is to:

* examine **local security enforcement mechanisms**
* compare them against baseline expectations
* apply **select, justified changes**
* validate system behavior after changes

---

## **5. Tasks / Instructions**

You will work on **both systems**, with different emphasis:

* **OSYS-DC01** – Domain Controller (high-risk, restricted)
* **OSYS-W11-01** – Windows Client (user-facing)

---

## **Part A – Explore Local Security Policy**

On **each system**:

1. Open **Local Security Policy**:

   ```
   secpol.msc
   ```
2. Explore the following sections:

   * Account Policies
   * Local Policies → Audit Policy
   * Local Policies → User Rights Assignment
   * Local Policies → Security Options

Answer:

* Which settings directly enforce **security decisions**?
* Which settings align with your **Workshop 03 baseline analysis**?

✅ **Checkpoint:** You can locate and describe key policy categories.

---

## **Part B – User Accounts and Groups**

Using **Computer Management**:

1. Review:

   * Local Users
   * Local Groups
2. Identify:

   * Members of the **Administrators** group
   * Any unused or unnecessary accounts
3. Compare findings to baseline expectations.

Answer:

* Why is group membership more important than individual permissions?
* Which accounts represent the highest risk?

---

## **Part C – User Rights and Privilege Assignment**

In **Local Security Policy → User Rights Assignment**, focus on:

* Log on locally
* Log on through Remote Desktop Services
* Access this computer from the network
* Shut down the system
* Back up files and directories

For **at least three (3)** rights:

1. Identify current assignments
2. Compare to baseline guidance
3. Decide whether the assignment is appropriate

⚠️ Do **not** remove rights without understanding system impact.

---

## **Part D – Controlled Policy Changes**

On **one system only** (as directed by instructor):

1. Apply **one or two justified changes**, such as:

   * Restricting logon rights
   * Removing unnecessary admin membership
2. Document:

   * What was changed
   * Why it was changed
   * Expected impact

Reboot **if required**.

✅ **Checkpoint:** System remains functional after changes.

---

## **Part E – Validation and Impact Assessment**

After changes:

* Attempt normal logon
* Validate administrative access
* Confirm no unintended lockouts occurred

Answer:

* What changed in system behavior?
* What risks were reduced?
* What risks were introduced?

---

## **Part F – Risk & Security Goal Mapping**

For each change made:

* Identify the supported security goal:

  * Confidentiality
  * Integrity
  * Availability
  * Accountability
* Explain how privilege control reduces attack surface.

---

## **Part G – Reflection**

Answer thoughtfully:

* Why is **least privilege** difficult to implement?
* What could go wrong if privileges are removed too aggressively?
* Why should these changes be tested locally before GPO enforcement?

---

## **6. Deliverables**

You must complete the **Workshop 04 fillable work form** provided by your instructor.

The completed form must include:

* Policy observations
* Group and account analysis
* Privilege review
* Documented changes
* Validation results
* Reflection responses

**Required file name:**

```
StudentID_OSYS2020_Workshop04_LocalSecurityPolicies.docx
```

Submit via **Brightspace**.

---

## **7. Reflection Questions**

All reflection responses must be completed **inside the work form**, including:

* Privilege risk analysis
* Impact of policy enforcement
* Lessons learned from controlled changes

---

## **8. Assessment & Rubric**

### **Assessment Type**

* **Formative (Not Graded)**

### **Success Criteria**

* Accurate policy interpretation
* Safe and justified changes
* Clear documentation
* Thoughtful security reasoning

Instructor feedback prepares you for:

* **Group Policy enforcement**
* **Domain-wide security controls**
* **Midterm domain hardening**

---

## **9. Submission Guidelines**

* Submit via **Brightspace**
* One Word document per student
* Partial submissions accepted with documented blockers

---

## **10. Resources / Equipment**

* OSYS2020 Windows domain (Workshops 00–03)
* Local Security Policy (`secpol.msc`)
* Computer Management
* Baseline documentation (Workshop 03)

---

## **11. Academic Policies**

* Collaboration encouraged for troubleshooting
* Submissions must reflect your own system and decisions
* Academic integrity policies apply

---

## **12. Copyright Notice**

© Nova Scotia Community College
For educational use within OSYS2020 only.

---
