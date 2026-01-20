# **OSYS2020 – Week 2 Presentation**

## **Windows Operating System Hardening: Patch Management, Updates, and Service Packs**

---

## **Slide 1 – Week 2 Overview**

### **Topic**

Windows Operating System Hardening
Patch Management, Updates, and Service Packs

### **Why this matters**

Most successful Windows attacks do **not** require advanced hacking skills.

They require:

* One missing update
* One unpatched vulnerability
* One delayed restart

> **Patch management is the first and most important security control.**

---

## **Slide 2 – Connection to Week 1**

Last week, you:

* Identified insecure Windows settings
* Mapped misconfiguration to threats
* Saw how insecurity often already exists

This week, you move from:

> **“What is wrong?” → “How do we reduce risk?”**

Patch management is usually:

* The **first fix**
* The **largest risk reduction**
* The **most neglected task**

---

## **Slide 3 – Learning Outcomes for This Week**

By the end of this week, you will be able to:

* Explain what operating system hardening means
* Describe the role of patch management in security
* Distinguish between updates, cumulative updates, and service packs
* Evaluate patching risks and trade-offs
* Apply patching strategies in a Windows environment

Supports:

* **LO1:** OS hardening
* **LO2:** Understanding Windows security mechanisms

---

## **Slide 4 – What Is OS Hardening?**

### **Operating System Hardening**

The process of:

* Reducing attack surface
* Removing unnecessary risk
* Applying secure configuration standards

Hardening includes:

* Patching
* Disabling unused services
* Removing unnecessary software
* Enforcing security policies

> **Patching is the foundation of all other hardening efforts.**

---

## **Slide 5 – Why Unpatched Systems Are Dangerous**

Unpatched systems:

* Contain known vulnerabilities
* Are documented publicly
* Often have working exploit code available

Attackers don’t need to “discover” flaws.

They simply:

1. Scan the system
2. Match OS version
3. Exploit known weaknesses

> **If a vulnerability has a CVE, attackers already know about it.**

---

## **Slide 6 – Real-World Example: WannaCry**

### WannaCry Ransomware (2017)

* Exploited a Windows SMB vulnerability
* Patch was released **two months earlier**
* Thousands of organizations were still unpatched

Impact:

* Hospitals shut down
* Businesses offline
* Millions in losses

Key lesson:

> The patch already existed — the failure was management, not technology.

---

## **Slide 7 – What Is Patch Management?**

Patch management is not “install updates sometimes.”

It is a **process** that includes:

* Identifying updates
* Testing patches
* Deploying patches
* Verifying installation
* Documenting changes

> Patch management is **administrative discipline**, not a technical feature.

---

## **Slide 8 – Types of Windows Updates**

Windows uses multiple update types:

### 1. **Security Updates**

* Fix vulnerabilities
* High priority
* Often released monthly (Patch Tuesday)

### 2. **Quality Updates**

* Bug fixes
* Stability improvements

### 3. **Feature Updates**

* New Windows versions
* Major system changes

### 4. **Driver Updates**

* Hardware compatibility fixes

Not all updates carry equal risk or urgency.

---

## **Slide 9 – What Are Service Packs?**

Historically:

* Service Packs bundled many updates
* Installed as a single large update

Modern Windows:

* Uses **cumulative updates** instead
* Each update includes previous fixes

Important concept:

> If you miss several updates, the next cumulative update includes them all.

---

## **Slide 10 – Patch Tuesday**

Microsoft releases most security updates on:

* **Second Tuesday of each month**

Why this matters:

* Administrators can plan patch cycles
* Attackers also plan around it

After Patch Tuesday:

* Vulnerability details become public
* Exploit development accelerates

> The days immediately after Patch Tuesday are high-risk periods.

---

## **Slide 11 – The Patch Management Dilemma**

Administrators must balance:

| Risk              | Example                       |
| ----------------- | ----------------------------- |
| Security risk     | Leaving systems unpatched     |
| Operational risk  | Updates breaking applications |
| Availability risk | Reboots during business hours |

This is why:

* Testing environments exist
* Staged deployments are used

Security decisions always involve trade-offs.

---

## **Slide 12 – Common Patch Management Mistakes**

* “We’ll update later”
* No reboot after updates
* Updates disabled for convenience
* Assuming automatic updates are enough
* No verification that patches installed

> **An update downloaded is not an update applied.**

---

## **Slide 13 – Windows Update Architecture (High-Level)**

Windows Update can be managed through:

* Local Windows Update
* Windows Update for Business
* WSUS (Windows Server Update Services)
* Intune / Endpoint Manager

In this course:

* You will focus on **local and domain-based patching concepts**

Understanding architecture matters before automation.

---

## **Slide 14 – Patch Management in a Domain Environment**

In business environments:

* Centralized control is preferred
* Administrators decide:

  * When updates install
  * When reboots occur
  * Which systems update first

Why?

* Predictability
* Stability
* Reduced downtime

> Domains exist to control change — not to prevent it.

---

## **Slide 15 – Security Goals and Patching**

Patch management directly supports:

* **Confidentiality**
  Prevents data exposure vulnerabilities

* **Integrity**
  Prevents unauthorized modification

* **Availability**
  Reduces ransomware risk

* **Accountability**
  Enables change tracking and auditing

Patching supports **all four security goals**.

---

## **Slide 16 – Threats Prevented by Patching**

Patching helps defend against:

* Malware exploitation
* Remote code execution
* Privilege escalation
* Worms and ransomware
* Lateral movement

Many attacks fail entirely when systems are patched.

---

## **Slide 17 – Assessment Activity: Risk Ranking**

### Group Discussion

Rank the following risks from highest to lowest:

* Missing security updates
* Weak passwords
* Disabled firewall
* Excessive admin privileges

There is no single correct answer —
only defensible reasoning.

This mirrors real-world decision-making.

---

## **Slide 18 – Re-Assessment Checkpoint**

Quick self-check:

* Can you explain why patching is more important than antivirus?
* Do you understand the difference between feature and security updates?
* Can you explain why patches are delayed in businesses?

If not — that’s okay.
That’s what labs are for.

---

## **Slide 19 – Hands-On Preview (Lab Connection)**

This week’s lab will have you:

* Check patch status on a Windows system
* Identify missing updates
* Determine if updates are installed but pending reboot
* Assess patch-related risk

> You will not just “click update” — you will evaluate patch health.

---

## **Slide 20 – Closure: 3–2–1 Reflection**

Before next class:

* **3 things** you learned about patching
* **2 risks** caused by delayed updates
* **1 question** you still have

These reflections prepare you for:

* Hardening labs
* Midterm domain security
* Final project decisions

---

## **Slide 21 – Looking Ahead to Week 3**

### Next Topic:

**Security Templates & Configuration Baselines**

