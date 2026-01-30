# **OSYS2020 – Windows Security**

## **Workshop 00: Build a Windows Domain in GNS3 (1 DC + DNS + DHCP)**

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
* Build a basic virtual network in GNS3
* Configure a Windows Server as a **Domain Controller** with **DNS**
* Join a Windows 11 client to the domain and validate connectivity

---

## **3. Learning Outcomes Addressed**

* **LO1:** Describe steps required to harden an operating system (foundation environment for patching/baselines)
* **LO2:** Interpret and manipulate Windows security components (accounts, policies, domain security objects)
* **LO3:** Implement Windows network security and security administration (domain infrastructure foundation)

---

## **4. Assignment Description / Use Case**

### Use Case

You are the junior Windows administrator for a small business. Your first job is to build the domain environment that all security controls will depend on. If this foundation is incorrect, **every future security decision will be unreliable**.

You will produce:

* A working domain (AD DS)
* Working DNS resolution
* Working Network with IPv4 addressing
* A joined Windows 11 client

---

## **5. Tasks / Instructions**

## Step 1 — Install Tools and Connect to the GNS3 Server

### 1.1 Install the latest GNS3 Client

1. Download and install **GNS3 (latest)** on your computer.
2. Launch GNS3.
3. Choose **“Run appliances on a remote server”** (or equivalent).
4. Instructor will provide:

   * **GNS3 Server IP**
   * Port: 3080
   * IPv4: See Student Server IP Table

✅ **Checkpoint:** You can see the remote server status as connected.

---

### 1.2 Remote Students: Connect to NSCC VPN first

1. Install **FortiClient VPN** (as used in your VPN workshop).
2. Connect to the **NSCC VPN** as instructed by the instructor (required for remote access to the GNS3 server).
3. Confirm you can reach the GNS3 server IP (instructor may provide a test step).

✅ **Checkpoint:** VPN connected and you can connect the GNS3 client to the remote server.

---

### 1.3 Install Virt-Viewer (for VM console access)

You will use Virt-Viewer to open the console of Windows VMs.

1. Install **Virt-Viewer** (also called “Remote Viewer”).
2. After installation, keep it ready—GNS3 will launch it when you open a console.

✅ **Checkpoint:** Virt-Viewer is installed and opens normally.

---

## Step 2 — Initial Setup on Each Windows Computer (First Boot)

> You will do this **for both** the Windows Server VM and Windows 11 VM once they are powered on.

### 2.1 First-boot basics (both VMs)

1. Open the console in GNS3 (Virt-Viewer should launch).
2. Complete:

   * Region/Keyboard
   * Accept license terms (if prompted)
   * Set a local password for the initial administrator account (Server)

✅ **Checkpoint:** You can log in to each VM.

---

### 2.2 Windows 11 Local Account Requirement (Important)

For the **Windows 11 client**, create a local account:

* **Username:** `itadmin`
* **Password:** `3P7JDW2$`

> Use **exactly** this username/password for course consistency (future labs assume it).

✅ **Checkpoint:** You can log into Windows 11 as `itadmin`.

---

### 2.3 Rename machines (recommended for clarity)

Do this once you have access to Windows settings:

* Windows Server: `OSYS-DC01`
* Windows 11 Client: `OSYS-W11-01`

Windows path:

* **Settings → System → About → Rename this PC**

✅ **Checkpoint:** Both machines rebooted and show the correct names.

---

## Step 3 — Create GNS3 Project + Topology + Internet Connectivity

### 3.1 Create the GNS3 project

1. In GNS3: **File → New Project**
2. Name: `OSYS2020`

✅ **Checkpoint:** You are inside the OSYS2020 project workspace.

---

### 3.2 Import appliances (provided by instructor)

Instructor will provide two appliance files:

1. **Windows 11 Client**
2. **Windows Server**

Add them to GNS3 (exact steps depend on appliance type):

* **File → Import appliance** (or “New template” → choose appliance file)
* Ensure they register on the remote server

✅ **Checkpoint:** Both appliances appear in your node list and can be dragged onto the canvas.

---

### 3.3 Build the topology

Drag these onto the canvas:

* **NAT Cloud** (for internet access)
* **GNS3 Ethernet Switch**
* **Windows Server VM**
* **Windows 11 VM**

Connect:

* NAT Cloud → GNS3 Switch
* Windows Server → GNS3 Switch
* Windows 11 → GNS3 Switch

Topology (simple):

```
[NAT Cloud] --- [GNS3 Switch] --- [OSYS-DC01]
                          └------ [OSYS-W11-01]
```

✅ **Checkpoint:** All links show “green” (connected) when devices are powered on.

---

### 3.4 Power on and test internet connectivity (before domain setup)

1. Start all nodes.

2. On **Windows 11**:

   * Open Command Prompt
   * Run: `ipconfig`
   * Confirm it receives an IP from NAT (it will be something like 192.168.x.x depending on NAT)

3. Test internet:

   * `ping 8.8.8.8`
   * `ping google.com`

✅ **Checkpoint:** You have IP connectivity and DNS resolution works (at least via NAT’s DNS).

> If DNS name ping fails but IP ping works, that’s OK for now—once your DC becomes DNS, your client DNS will change.

---

## Step 4 — Set Up and Configure the Windows Domain (AD DS + DNS + DHCP)

### 4.1 Plan your internal domain network (recommended)

Use a simple private LAN for your domain. Example:

* **Domain Name (AD):** `osys.local`
* **Server (DC) Static IP:** `192.168.10.10/24`
* **Gateway:** (none required for internal-only, but recommended if you want internet)
* **DNS:** `192.168.10.10` (the DC points to itself)
* **DHCP Scope:** `192.168.10.100 – 192.168.10.200`
* **DHCP Options:**

  * DNS Server: `192.168.10.10`
  * Domain Name: `osys.local`

> Note: Your NAT network may differ. The key is: once the domain is up, your client must use **the DC as DNS**.

---

### 4.2 Set a static IP on the Domain Controller (Windows Server)

On **OSYS-DC01**:

1. Open **Network Connections**
2. Right-click Ethernet → Properties → IPv4
3. Set:

   * IP: `192.168.10.10`
   * Subnet: `255.255.255.0`
   * DNS: `192.168.10.10`
   * Gateway: leave blank (or set if your instructor requires NAT routing)

✅ **Checkpoint:** `ipconfig` shows the static address.

---

### 4.3 Install AD DS and DNS roles

1. Open **Server Manager**
2. **Add Roles and Features**
3. Select:

   * **Active Directory Domain Services (AD DS)**
   * **DNS Server** (usually included/selected)
4. Install

✅ **Checkpoint:** Roles install successfully.

---

### 4.4 Promote the server to Domain Controller

1. In Server Manager, click the notification flag → **Promote this server to a domain controller**
2. Choose: **Add a new forest**
3. Domain name: `osys.local`
4. Set DSRM password (record it securely for lab use)
5. Complete the wizard and reboot

✅ **Checkpoint:** After reboot, you can log in as a domain administrator (e.g., `OSYS\Administrator`).

---

### 4.5 Install and configure DHCP

1. Server Manager → Add Roles and Features
2. Install: **DHCP Server**
3. Complete post-install configuration (DHCP authorization wizard)

Create a DHCP scope:

* Name: `OSYS-LAN`
* Range: `192.168.10.100` to `192.168.10.200`
* Subnet: `255.255.255.0`
* DNS Server option: `192.168.10.10`
* Domain Name option: `osys.local`
* Activate scope

✅ **Checkpoint:** DHCP scope is active and authorized.

---

### 4.6 Configure Windows 11 client to use DHCP (and the domain DNS)

On **OSYS-W11-01**:

1. Ensure network adapter is set to **DHCP**
2. Run:

   * `ipconfig /release`
   * `ipconfig /renew`
3. Confirm:

   * IP is in `192.168.10.x`
   * DNS server is `192.168.10.10`

✅ **Checkpoint:** `ipconfig /all` shows the DC as DNS.

---

### 4.7 Join Windows 11 to the domain

On Windows 11:

1. **Settings → System → About → Domain or workgroup**
2. **Join a domain**: `osys.local`
3. When prompted, use domain credentials (Administrator or a created domain join account)
4. Reboot

✅ **Checkpoint:** Login screen shows domain, and you can log in with domain credentials.

---

### 4.8 Validation Tests (Required)

Run these tests on Windows 11:

1. **DNS resolution**

   * `ping osys-dc01` (or ping by server name)
2. **Domain membership**

   * Settings shows domain joined
3. **DHCP**

   * `ipconfig /all` shows DHCP + DNS from DC
4. **AD tools (optional check)**

   * On DC, confirm the client appears in **Active Directory Users and Computers**

✅ **Checkpoint:** All four checks pass.

---

## **6. Deliverables**

Submit **one document** (PDF or Word) that includes:

1. Screenshot or notes showing:

   * Your GNS3 topology (canvas screenshot)
2. Evidence the DC is configured:

   * Server name + IP config
   * AD DS installed and domain created (`osys.local`)
   * DHCP scope active
3. Evidence the client is joined:

   * Client IP config (shows DHCP + DNS = DC)
   * Domain join confirmation
4. Validation tests output (copy/paste or screenshots)

File name:
`StudentID_OSYS2020_Workshop00_DomainSetup`

---

## **7. Reflection Questions**

Answer briefly:

1. What was the most challenging step and why?
2. Why is DNS critical to Active Directory?
3. What would break first if the DC were unpatched or misconfigured?
4. How does this domain environment support future security hardening work?

---

## **8. Assessment & Rubric**

### Assessment Type

**Formative (Not Graded)** — completion is required for future labs.

### Success Criteria (Checklist)

* Topology built correctly (NAT + switch + 2 VMs)
* Client and Server boot and are accessible via Virt-Viewer
* DC has static IP and is promoted to a domain controller
* DNS functional (client uses DC as DNS)
* DHCP scope functional (client receives correct IP settings)
* Windows 11 successfully joins domain

---

## **9. Submission Guidelines**

* Submit via **Brightspace**
* One document per student
* If you get stuck, submit partial progress with a “Blockers” section:

  * What you tried
  * What error occurred
  * Screenshots of the error

---

## **10. Resources / Equipment**

* GNS3 Client (latest)
* NSCC VPN client (remote students)
* Virt-Viewer (Remote Viewer)
* Instructor-provided appliances:

  * Windows Server
  * Windows 11 Client

---

## **11. Academic Policies**

* You may collaborate and troubleshoot together
* Your submission must reflect your own environment and results
* Academic integrity policies apply

---

## **12. Copyright Notice**

© Nova Scotia Community College
For educational use within OSYS2020 only.

---

## Quick Troubleshooting

**Virt-Viewer doesn’t open:**

* Confirm Virt-Viewer installed; try opening console again from GNS3.

**Client can’t get an IP:**

* Check links are connected to the switch
* Confirm DHCP role is installed + scope is activated
* `ipconfig /release` and `/renew`

**Domain join fails (DNS-related):**

* Client DNS must point to DC (not 8.8.8.8, not NAT DNS)
* Confirm DC DNS role installed and running

**Can’t resolve domain name:**

* On client: `nslookup osys.local` should point to DC DNS

---
