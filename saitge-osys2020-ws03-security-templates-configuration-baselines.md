# **OSYS2020 – Windows Security**

## **Workshop 03: Security Templates, Configuration Baselines, and System Hardening Standards**

---

## **1. Assignment Details**

| Field                | Information                                                |
| -------------------- | ---------------------------------------------------------- |
| **Workshop Title**   | Workshop 03 – Security Templates & Configuration Baselines |
| **Course Code**      | OSYS2020                                                   |
| **Course Title**     | Windows Security                                           |
| **Assignment Type**  | Guided Hands-On + Analytical Workshop                      |
| **Weight**           | Not Graded (Formative – Prepares for GPO Enforcement)      |
| **Estimated Effort** | 2–3 hours                                                  |
| **Delivery Mode**    | In-class / Remote (GNS3 + VPN)                             |
| **Prerequisite**     | Workshop 00, Workshop 02                                   |
| **Due**              | End of Week 3                                              |

---

## **2. Overview / Purpose / Objectives**

### **Overview**

In this workshop, you will examine **security templates**, **configuration baselines**, and **system hardening standards** to understand how organizations define and measure security at scale.

Rather than applying controls immediately, you will:

* Explore industry security standards
* Compare baseline recommendations to your domain systems
* Identify gaps between *default*, *patched*, and *hardened* configurations

This workshop emphasizes **analysis before enforcement**, a critical principle in professional security administration.

---

### **Purpose**

The purpose of this workshop is to help you move beyond individual configuration changes and begin thinking in terms of:

* **standards**
* **consistency**
* **measurable security posture**

Most real-world security failures occur not because controls do not exist, but because **standards were never clearly defined or enforced**.

---

### **Objectives**

By the end of this workshop, you will be able to:

* Explain the purpose of security templates and baselines
* Identify reputable system hardening standards
* Compare a Windows system against a baseline
* Identify configuration drift and security gaps
* Relate baseline compliance to security goals

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
* Fully patched systems (Workshop 02)

Management asks a new question:

> “How do we know our systems are *secure enough* — and how do we prove it?”

Your task is to **analyze security baselines** and compare them to your current environment in order to:

* identify risk
* support future policy decisions
* prepare for compliance and audits

---

## **5. Tasks / Instructions**

You will analyze the following systems:

* **OSYS-DC01** (Windows Server – Domain Controller)
* **OSYS-W11-01** (Domain-joined Windows 11 client)

---

### **Part A – Understand Security Baselines (Conceptual)**

Answer the following:

1. What is a **security template**?
2. What is a **configuration baseline**?
3. How do templates and baselines differ?
4. Why do organizations define hardening standards before enforcement?

Use examples from:

* Patch management (Workshop 02)
* Domain configuration (Workshop 00)

---

### **Part B – Explore Industry Hardening Standards**

Review **one** of the following baseline sources (as directed by your instructor):

* Microsoft Security Baselines
* CIS Windows Benchmarks
* Instructor-provided baseline excerpts

Identify recommendations related to:

* Password policies
* Account lockout
* Auditing
* User rights and privileges
* Security options

📌 You are not expected to read the entire document.

---

### **Part C – Baseline Comparison (Hands-On Analysis)**

On **each system**, explore:

* **Local Security Policy**

  * Password Policy
  * Account Lockout Policy
  * Audit Policy
* **Local Users and Groups**
* **Security Options**

Create a comparison table with **at least five (5)** settings:

| Setting | Baseline Recommendation | Current Setting | Compliant (Yes/No) |
| ------- | ----------------------- | --------------- | ------------------ |

---

### **Part D – Configuration Drift and Risk Analysis**

For **three (3)** non-compliant settings:

1. Explain why the baseline exists
2. Identify the risk created by non-compliance
3. Identify the affected security goal:

   * Confidentiality
   * Integrity
   * Availability
   * Accountability

Explain how **configuration drift** could cause these settings to change over time.

---

### **Part E – Domain Perspective**

Answer the following:

* Why is enforcing baselines more important in a **domain** than on standalone systems?
* Why should domain controllers have stricter baselines than clients?
* How do baselines support centralized security management?

Relate your answers to **future GPO enforcement**.

---

### **Part F – Reflection**

Write short reflective responses:

* Were you surprised by how many default settings differ from baselines?
* Why do vendors ship systems with permissive defaults?
* What could go wrong if baselines are enforced without testing?

---

## **6. Deliverables**

Submit **one document** (PDF or Word) containing:

* Baseline source used
* Comparison table
* Risk analysis
* Domain perspective responses
* Reflection responses

**File name format:**
`StudentID_OSYS2020_Workshop03_BaselineAnalysis`

---

## **7. Reflection Questions**

Include responses to:

* Why are baselines critical to enterprise security?
* How do baselines support audits and compliance?
* How does baseline analysis prepare you for GPO enforcement?

---

## **8. Assessment & Rubric**

### **Assessment Type**

* **Formative (Not Graded)**

### **Success Criteria**

* Accurate baseline comparison
* Logical risk reasoning
* Correct mapping to security goals
* Thoughtful reflection and analysis

Instructor feedback prepares you for:

* Group Policy enforcement
* User rights management
* Midterm domain hardening

---

## **9. Submission Guidelines**

* Submit via **Brightspace**
* One document per student
* Screenshots optional but encouraged
* Partial submissions accepted with documented blockers

---

## **10. Resources / Equipment**

* OSYS2020 Windows Domain (Workshop 00)
* Patched systems (Workshop 02)
* Local Security Policy tools
* Baseline documentation (as assigned)

---

## **11. Academic Policies**

* Collaboration encouraged for discussion
* Work must reflect your own analysis
* Academic integrity policies apply

---

## **12. Copyright Notice**

© Nova Scotia Community College
For educational use within OSYS2020 only.

---

## **Looking Ahead**

This workshop sets the stage for:

* **Workshop 04:** Local Security Policies, Users, and Privileges
* **Later Workshops:** Group Policy enforcement and compliance monitoring

You are now moving from:

> *“Is the system working?”*
> → *“Is the system consistently secure?”*

---
