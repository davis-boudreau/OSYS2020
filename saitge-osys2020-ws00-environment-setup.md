Perfect — below is the **complete, rewritten Workshop 00** with **everything kept intact**, **SPICE Guest Tools installed via web download**, **and Step 4 fully included and integrated**.

This is now a **single, authoritative, student-ready document** with:

* Clear sequencing
* No ISO/CD confusion
* Consistent DNS/DHCP logic
* Explicit checkpoints
* Strong instructional scaffolding

You can post this as **Workshop 00 (Final)**.

---

# **OSYS2020 – Windows Security**

## **Workshop 00: Build a Windows Domain in GNS3 (1 DC + DNS)**

---

## **1. Assignment Details**

| Field                | Information                                                 |
| -------------------- | ----------------------------------------------------------- |
| **Workshop Title**   | Workshop 00 – Windows Domain Setup in GNS3                  |
| **Course Code**      | OSYS2020                                                    |
| **Course Title**     | Windows Security                                            |
| **Type**             | Integrated Tutorial Workshop (Step-by-step + hands-on)      |
| **Weight**           | Not graded (required setup for all future labs/evaluations) |
| **Estimated Effort** | 1–2 hours                                                   |
| **Delivery Mode**    | In-class + Remote-capable (VPN)                             |
| **Due**              | End of Week 1 (or as directed by instructor)                |

---

## **2. Overview / Purpose / Objectives**

### Overview

In this Workshop 00, you will set up your **OSYS2020 lab domain** using **GNS3** with:

* **1 Windows Server (Domain Controller)** running **AD DS + DNS**
* **1 Windows 11 Client**
* A simple topology using a **NAT Cloud + GNS3 Switch**

### Purpose

This domain becomes your **case study environment** for the entire course (hardening, baselines, GPO, firewall, logging, incident handling).

### Objectives

By the end of this workshop, you will be able to:

* Connect the **GNS3 client** to the provided server
* Access Windows VM consoles using **Virt-Viewer**
* Install **SPICE Guest Tools** to improve VM usability
* Build a basic virtual network in GNS3
* Configure a Windows Server as a **Domain Controller** with **DNS**
* Join a Windows 11 client to the domain and validate connectivity

---

## **3. Learning Outcomes Addressed**

* **LO1:** Describe steps required to harden an operating system
* **LO2:** Interpret and manipulate Windows security components
* **LO3:** Implement Windows network security and security administration

---

## **4. Assignment Description / Use Case**

### Use Case

You are the junior Windows administrator for a small business. Your first job is to build the domain environment that all security controls will depend on.

If this foundation is incorrect, **every future security decision will be unreliable**.

You will produce:

* A working Windows domain (AD DS)
* Functional DNS resolution
* A working IPv4 network
* A joined Windows 11 client

---

## **5. Tasks / Instructions**

---

## **Step 1 — Install Tools and Connect to the GNS3 Server**

### **1.1 Install the latest GNS3 Client**

1. Download and install **GNS3 (latest)**.
2. Launch GNS3.
3. Choose **“Run appliances on a remote server.”**
4. Instructor will provide:

   * **GNS3 Server IP**
   * Port: **3080**
   * IPv4: **See Student Server IP Table**

✅ **Checkpoint:** GNS3 shows a connected remote server.

---

### **1.2 Remote Students: Connect to NSCC VPN**

1. Install **FortiClient VPN**.
2. Connect to the **NSCC VPN** as instructed.
3. Confirm access to the GNS3 server.

✅ **Checkpoint:** VPN connected and GNS3 connects successfully.

---

### **1.3 Install Virt-Viewer**

1. Install **Virt-Viewer (Remote Viewer)**.
2. Leave it installed—GNS3 will launch it automatically.

✅ **Checkpoint:** VM consoles open in Virt-Viewer.

---

## **Step 2 — Initial Setup on Each Windows Computer**

> Complete this section on **both** Windows VMs.

### **2.1 First-Boot Setup**

1. Open the VM console.
2. Complete:

   * Region and keyboard
   * License acceptance
   * Local Administrator password (Server)

✅ **Checkpoint:** You can log into both systems.

---

### **2.2 Windows 11 Local Account**

Create a **local** account on the Windows 11 VM:

* **Username:** `itadmin`
* **Password:** `3P7JDW2$`

✅ **Checkpoint:** You can log into Windows 11 as `itadmin`.

---

### **2.3 Rename Computers**

Rename for clarity:

* **Server:** `OSYS-DC01`
* **Client:** `OSYS-W11-01`

Path:
**Settings → System → About → Rename this PC**

✅ **Checkpoint:** Both systems reboot with new names.

---

### **2.4 Install SPICE Guest Tools (Required on BOTH VMs)**

SPICE Guest Tools improve:

* Mouse integration
* Display performance
* Clipboard support
* Console responsiveness

You must install them on **both VMs**.

#### **A) Download SPICE Guest Tools**

On **each VM**:

1. Open a web browser.
2. Go to:
   **[https://www.spice-space.org/download.html](https://www.spice-space.org/download.html)**
3. Scroll to **Windows Binaries**.
4. Download **spice-guest-tools**.

✅ **Checkpoint:** Installer downloaded inside the VM.

---

#### **B) Install**

1. Run the downloaded installer.
2. Accept defaults.
3. Allow drivers if prompted.
4. Reboot when finished.

✅ **Checkpoint:** System reboots successfully.

---

#### **C) Verify**

* Confirm **SPICE Guest Tools** appear in installed programs.
* Mouse and display feel smooth.

✅ **Checkpoint:** SPICE tools installed and working on both VMs.

---

## **Step 3 — Create GNS3 Project, Topology, and Internet Connectivity**

### **3.1 Create Project**

* **File → New Project**
* Name: `OSYS2020`

---

### **3.2 Import Appliances**

Instructor provides:

* Windows Server appliance
* Windows 11 appliance

Import both and ensure they register on the remote server.

---

### **3.3 Build the Topology**

Add and connect:

* **NAT Cloud**
* **GNS3 Switch**
* **OSYS-DC01**
* **OSYS-W11-01**

```
[NAT Cloud] --- [GNS3 Switch] --- [OSYS-DC01]
                          └------ [OSYS-W11-01]
```

---

### **3.4 Test Internet Connectivity**

On Windows 11:

* `ipconfig`
* `ping 8.8.8.8`
* `ping google.com`

✅ **Checkpoint:** Internet connectivity confirmed.

---

## **Step 4 — Configure the Windows Domain (AD DS + DNS)**

### **4.1 Domain Network Plan**

Use the NAT network:

* **Domain:** `osys.local`
* **DC IP:** `192.168.100.2/24`
* **Gateway:** `192.168.100.1`
* **Server DNS:** `127.0.0.1`
* **Client DNS:** `192.168.100.2`
* **DHCP:** Provided by NAT (`192.168.100.129–190`)

---

### **4.2 Set Static IP on Domain Controller**

On **OSYS-DC01**:

* IP: `192.168.100.2`
* Subnet: `255.255.255.0`
* DNS1: `127.0.0.1`
* DNS2: `8.8.8.8`
* Gateway: `192.168.100.1`

---

### **4.3 Install AD DS and DNS**

* Server Manager → Add Roles
* Install **AD DS** and **DNS Server**

---

### **4.4 Promote to Domain Controller**

* Add new forest
* Domain: `osys.local`
* Set DSRM password
* Reboot

---

### **4.5 Configure Client DNS**

On **OSYS-W11-01**:

* Use DHCP
* Override DNS:

  * `192.168.100.2`
  * `8.8.8.8`

---

### **4.6 Join Domain**

* Join domain: `osys.local`
* Use domain credentials
* Reboot

---

### **4.7 Validation**

On Windows 11:

* `ping osys-dc01`
* Confirm domain join
* `ipconfig /all` shows DC as DNS

---

## **6. Deliverables**

Submit **one document** containing:

* GNS3 topology screenshot
* DC IP config + domain proof
* Client IP config + domain join proof
* Validation command output

File name:
`StudentID_OSYS2020_Workshop00_DomainSetup`

---

## **7. Reflection Questions**

1. What step was most challenging?
2. Why is DNS critical to Active Directory?
3. What would fail first if the DC were misconfigured?
4. How does this environment support future hardening work?

---

## **8. Assessment & Rubric**

**Formative (Not Graded)**

**Success Criteria**

* Correct topology
* SPICE tools installed
* DC promoted with DNS
* Client joins domain successfully

---

## **9. Submission Guidelines**

* Submit via Brightspace
* Partial submissions allowed with documented blockers

---

## **10. Resources / Equipment**

* GNS3 Client
* NSCC VPN
* Virt-Viewer
* SPICE Guest Tools (web download)
* Instructor-provided appliances

---

## **11. Academic Policies**

* Collaboration allowed
* Work must reflect your own environment

---

## **12. Copyright**

© Nova Scotia Community College
For educational use within OSYS2020 only.

---
