# **OSYS2020 – Windows Security**

## **Week 1 Lab: Identify Insecure Windows Settings**

---

## **1. Assignment Details**

| Field                | Information                                           |
| -------------------- | ----------------------------------------------------- |
| **Assignment Title** | Week 1 Lab – Identify Insecure Windows Settings       |
| **Course Code**      | OSYS2020                                              |
| **Course Title**     | Windows Security                                      |
| **Assignment Type**  | Guided Practical Lab (Formative → Portfolio Artifact) |
| **Weight**           | Not graded (prepares for graded labs and quizzes)     |
| **Estimated Effort** | 2–3 hours                                             |
| **Delivery Mode**    | In-Class / Lab + Independent Work                     |
| **Due**              | End of Week 1                                         |

---

## **2. Overview / Purpose / Objectives**

### **Overview**

In this lab, you will examine a **Windows system that has not been properly secured** and identify settings that increase security risk. This mirrors how many real-world systems exist before a security incident occurs.

### **Purpose**

The purpose of this lab is to help you:

* Recognize **insecure configurations**
* Connect misconfiguration to **real-world threats**
* Begin thinking like a **Windows security administrator**

### **Objectives**

By completing this lab, you will be able to:

* Identify insecure Windows settings
* Explain why those settings are risky
* Map insecure settings to security goals and threat types

---

## **3. Learning Outcomes Addressed**

This lab supports the following course learning outcomes:

* **LO1:** Harden a Windows operating system using industry best practices
* **LO2:** Interpret and manipulate Windows security components

---

## **4. Assignment Description / Use Case**

### **Scenario**

You have been asked to review a **Windows workstation** used in a small business environment. The system “works fine,” but there are concerns about security.

Your task is **not to fix the system yet**, but to **identify weaknesses** and explain why they matter.

> This reflects real-world security work:
> **You must understand what is wrong before you can secure it.**

---

## **5. Tasks / Instructions**

### **Part A – System Review (Hands-On)**

Using the provided Windows virtual machine (local VM or GNS3):

Review the following areas and take notes:

1. **User Accounts**

   * Are users members of the Administrators group?
   * Is there a clear separation between admin and standard users?

2. **Password & Account Policies**

   * Password length and complexity
   * Account lockout settings
   * Guest account status

3. **Windows Updates**

   * Are updates enabled?
   * Is the system fully patched?

4. **Firewall Status**

   * Is Windows Firewall enabled?
   * Are inbound rules overly permissive?

5. **Defender / Antivirus**

   * Is real-time protection enabled?
   * Are definitions up to date?

6. **File & Folder Permissions**

   * Are sensitive folders broadly accessible?
   * Are permissions inherited unnecessarily?

---

### **Part B – Risk Identification (Analysis)**

For **at least five (5)** insecure settings you identify:

For each one, document:

* What the setting is
* Why it is insecure
* Which **security goal** it impacts:

  * Confidentiality
  * Integrity
  * Availability
  * Accountability
* What **threat type** could exploit it:

  * Malware
  * Credential attack
  * Misconfiguration
  * Privilege abuse
  * Insider threat

---

### **Part C – Reflection (Portfolio-Oriented)**

Answer the following questions:

1. Which insecure setting surprised you the most?
2. Which setting do you think is **most commonly misconfigured** in small businesses?
3. Why do you think insecure systems often remain in use?

---

## **6. Deliverables**

Submit **one document** (PDF or Word) containing:

* A short table or list of identified insecure settings
* Your analysis from Part B
* Your written reflection from Part C

📌 Screenshots are encouraged but optional.

---

## **7. Reflection Questions**

Include responses to these reflection prompts:

* How does misconfiguration relate to real-world security incidents?
* How do security goals help prioritize what to fix first?
* How did this lab change how you view “default settings”?

---

## **8. Assessment & Rubric**

### **Assessment Type**

* **Formative (Not Graded)**
* Instructor feedback provided

### **Success Criteria**

* Clear identification of insecure settings
* Logical explanation of risk
* Correct mapping to security goals and threats
* Thoughtful reflection

---

## **9. Submission Guidelines**

* Submit via **Brightspace**
* File naming format:
  `StudentID_OSYS2020_Week1_Lab`
* Late submissions accepted (feedback-focused activity)

---

## **10. Resources / Equipment**

* Windows Workstation VM (provided)
* Course slides (Week 1)
* Microsoft Learn (Windows Security Fundamentals)
* Built-in Windows tools:

  * Settings
  * Local Users & Groups
  * Windows Security Center
  * Windows Firewall

---

## **11. Academic Policies**

* This lab must reflect **your own observations**
* Collaboration is allowed for discussion, not copying
* Academic integrity policies apply

---

## **12. Copyright Notice**

© Nova Scotia Community College
This document is provided for educational use within OSYS2020.

