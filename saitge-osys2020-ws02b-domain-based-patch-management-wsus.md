# **OSYS2020 – Windows Security**

## **Workshop 02 (Extended): Domain-Based Patch Management & WSUS Concepts**

---

## **1. Assignment Details**

| Field                | Information                                                      |
| -------------------- | ---------------------------------------------------------------- |
| **Workshop Title**   | Workshop 02 (Extended) – Domain Patch Management & WSUS Concepts |
| **Course Code**      | OSYS2020                                                         |
| **Course Title**     | Windows Security                                                 |
| **Assignment Type**  | Guided Hands-On + Conceptual Workshop                            |
| **Weight**           | Not Graded (Formative – prepares for enterprise patching)        |
| **Estimated Effort** | 2–3 hours                                                        |
| **Delivery Mode**    | In-class / Remote (GNS3 + VPN)                                   |
| **Prerequisite**     | Workshop 00 – Windows Domain Setup                               |
| **Due**              | End of Week 2                                                    |

---

## **2. Overview / Purpose / Objectives**

### **Overview**

In this extended workshop, you will move from **standalone patching** to **domain-based patch management**, exploring how organizations centrally control Windows updates using **Windows Server Update Services (WSUS)** and **Group Policy**.

Rather than deploying a full WSUS server, you will:

* Learn how WSUS fits into enterprise security
* Simulate WSUS behavior using Group Policy settings
* Understand approval workflows, testing rings, and compliance

This workshop bridges the gap between **technical patching** and **administrative security governance**.

---

### **Purpose**

The purpose of this workshop is to help you:

* Understand why centralized patching exists
* Recognize the limitations of local Windows Update
* Think like a domain administrator responsible for uptime and security

Most real-world Windows environments **do not allow clients to update themselves freely**.

---

### **Objectives**

By the end of this workshop, you will be able to:

* Explain the role of WSUS in enterprise patch management
* Describe how Group Policy controls update behavior
* Simulate centralized patch control in a domain
* Evaluate patch deployment risks and trade-offs
* Relate WSUS concepts to security goals and incident prevention

---

## **3. Learning Outcomes Addressed**

This workshop supports the following course learning outcomes:

* **LO1:** Describe steps required to harden an operating system
* **LO2:** Interpret Windows security objects and policies
* **LO3:** Implement Windows security administration practices

---

## **4. Assignment Description / Use Case**

### **Use Case**

You are now the Windows administrator for a growing organization.

Management wants:

* Security updates applied promptly
* Minimal downtime
* Predictable reboots
* Central visibility into patch status

Allowing each system to update independently is no longer acceptable.

Your task is to **design and simulate a domain-based patch management approach** using WSUS concepts.

---

## **5. Tasks / Instructions**

You will work primarily on:

* **OSYS-DC01 (Windows Server – Domain Controller)**
* **OSYS-W11-01 (Domain-joined Windows 11 client)**

---

## **Part A – Understanding WSUS (Conceptual Foundation)**

Research and answer:

1. What is **WSUS**?
2. Why do organizations deploy WSUS instead of relying on Windows Update?
3. What types of updates are typically:

   * Approved immediately?
   * Delayed?
   * Declined?

Identify at least **three advantages** and **two risks** of centralized patching.

---

## **Part B – Patch Management Architecture (Thinking Like an Admin)**

Using your current domain, answer:

* Where would WSUS logically be installed?
* Which systems should update first?
* Which systems should update last?
* Why should domain controllers be patched differently?

Describe a **basic patching ring model**:

* Test systems
* Pilot users
* Production systems

---

## **Part C – Simulating WSUS with Group Policy**

Even without installing WSUS, you can simulate its behavior.

On **OSYS-DC01**:

1. Open **Group Policy Management**
2. Create a new GPO:

   * Name: `WSUS-Simulated-Patch-Control`
3. Edit the GPO and navigate to:

   ```
   Computer Configuration
   └ Administrative Templates
     └ Windows Components
       └ Windows Update
   ```

Configure (discussion-level if not enforcing yet):

* Configure Automatic Updates
* Specify update behavior (notify vs auto-install)
* Control reboot behavior

📌 You are **not required** to specify a WSUS server URL yet.

---

## **Part D – Apply and Observe Policy Behavior**

1. Link the GPO to:

   * The domain
   * Or a test OU (recommended)
2. On **OSYS-W11-01**:

   * Run `gpupdate /force`
   * Review Windows Update behavior

Answer:

* How does update behavior differ from standalone mode?
* Why is this important in enterprise environments?

---

## **Part E – Security and Risk Analysis**

Answer the following:

1. What risks exist if updates are applied automatically without control?
2. What risks exist if updates are delayed too long?
3. How does WSUS support:

   * Confidentiality
   * Integrity
   * Availability
   * Accountability

Relate your answers to **real-world incidents** discussed in class.

---

## **Part F – Reflection**

Write reflective responses:

* Why is patch management considered a **governance problem**, not just a technical one?
* How does centralized patching reduce organizational risk?
* How would poor patch management appear during a security audit?

---

## **6. Deliverables**

Submit **one document** (PDF or Word) containing:

* WSUS concept explanations
* Patch ring model description
* GPO screenshots or descriptions
* Security and risk analysis
* Reflection responses

**File name format:**
`StudentID_OSYS2020_Workshop02_WSUS_Concepts`

---

## **7. Reflection Questions**

Include written responses to:

* Why do enterprises avoid unmanaged patching?
* How does WSUS support compliance and auditing?
* What trade-offs exist between speed and stability?

---

## **8. Assessment & Rubric**

### **Assessment Type**

* **Formative (Not Graded)**

### **Success Criteria**

* Clear understanding of WSUS concepts
* Logical patch management design
* Correct use of Group Policy concepts
* Thoughtful reflection demonstrating administrative thinking

---

## **9. Submission Guidelines**

* Submit via **Brightspace**
* One document per student
* Screenshots optional but encouraged
* Partial submissions accepted with explanation of blockers

---

## **10. Resources / Equipment**

* OSYS2020 Windows Domain (Workshop 00)
* Group Policy Management Console
* Microsoft Learn – WSUS Overview
* Course slides (Week 2)

---

## **11. Academic Policies**

* Collaboration encouraged for discussion
* Work must reflect your own understanding
* Academic integrity policies apply

---

## **12. Copyright Notice**

© Nova Scotia Community College
For educational use within OSYS2020 only.

---

## **Instructor Alignment Note (Not Student-Facing)**

This extension:

* Prepares students for **real enterprise patching**
* Sets up cleanly for:

  * Security baselines
  * GPO enforcement
  * Compliance monitoring
* Avoids WSUS installation overhead while preserving conceptual rigor

---

### **Looking Ahead**

In later workshops, you will:

* Enforce baselines with GPO
* Introduce compliance and drift
* Examine patching failures during incidents

You are now thinking not just like a technician — but like a **Windows security administrator**.

---
