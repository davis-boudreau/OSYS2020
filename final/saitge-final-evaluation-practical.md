# **OSYS2020 – Windows Security**

# **Final Practical Exam**

**Instructor:** Davis Boudreau
**Duration:** 2-3 Hours
**Components:**

* **Part A – Practical Investigation (VM-based)**
* **Part B – Knowledge Exam (20 MC Questions)**

---

# **PART A – PRACTICAL INVESTIGATION (VM SCENARIOS)**

## **Instructions**

You will be provided with **multiple virtual machines**, each containing a **pre-configured security fault**.

For each scenario, you must:

1. **Identify the issue**
2. **Explain the root cause**
3. **Fix the problem**
4. **Validate your solution**
5. **Document your findings**

---

## **Deliverable Format**

For each scenario:

```text
1. Issue Identified
2. Root Cause Analysis
3. Evidence (logs, configs, screenshots)
4. Resolution Steps
5. Validation (proof it works)
```

---

# **Scenario 1 – NTFS Permission Failure**

## **Problem**

A user can open the HR folder but cannot access files inside.

---

## **Student Tasks**

* Identify permission issue
* Analyze inheritance
* Evaluate effective permissions
* Correct configuration

---

## **Expected Concepts**

* NTFS inheritance
* “This folder only” vs propagation
* RBAC

---

---

# **Scenario 2 – Firewall Misconfiguration**

## **Problem**

A web server (IIS) works locally but not from remote machines.

---

## **Student Tasks**

* Identify firewall rules
* Analyze inbound traffic behavior
* Modify rule configuration

---

## **Expected Concepts**

* Inbound vs outbound rules
* Port 80
* Profile behavior

---

---

# **Scenario 3 – Excessive Privileges**

## **Problem**

A standard user has administrative capabilities.

---

## **Student Tasks**

* Identify group membership
* Analyze privileges (Event ID 4672)
* Remove excessive permissions

---

## **Expected Concepts**

* Built-in groups
* Privilege assignment
* Least privilege principle

---

---

# **Scenario 4 – Suspicious Login Activity**

## **Problem**

Multiple failed login attempts followed by successful login.

---

## **Student Tasks**

* Identify Event IDs (4625, 4624)
* Analyze timeline
* Determine if attack occurred

---

## **Expected Concepts**

* Event logs
* brute-force detection
* correlation

---

---

# **Scenario 5 – Endpoint Protection Failure**

## **Problem**

Malicious file exists on system but was not blocked.

---

## **Student Tasks**

* Check Defender status
* Analyze protection settings
* Enable/restore protection

---

## **Expected Concepts**

* real-time protection
* threat detection
* Defender configuration

---

---

# **Scenario 6 – Broken Group Policy Enforcement**

## **Problem**

Security settings are not being applied to users.

---

## **Student Tasks**

* Analyze GPO linkage
* Check OU structure
* Verify policy application

---

## **Expected Concepts**

* GPO processing
* OU hierarchy
* SYSVOL

---

---

# **Scenario 7 – Incident Reconstruction**

## **Problem**

System shows signs of compromise.

---

## **Student Tasks**

* Correlate events
* identify attack sequence
* build timeline

---

## **Expected Concepts**

* event correlation
* attack lifecycle
* IoCs

---

---

# **Scenario 8 – Automation Validation**

## **Problem**

Security script is incomplete and does not properly audit system.

---

## **Student Tasks**

* analyze script
* improve automation
* validate output

---

## **Expected Concepts**

* PowerShell
* automation verification
* security auditing

---

