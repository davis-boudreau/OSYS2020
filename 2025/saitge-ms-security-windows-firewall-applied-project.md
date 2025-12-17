## OSYS2020: Windows Security - Applied Project Assignment

**Security Monitoring and Response (5/100, Outcome 2)**

**Objective:** To demonstrate the ability to set up basic security monitoring in a Windows environment and respond to simulated security events.

**Scenario:**

Your organization has experienced a series of suspicious activities, including unusual logon attempts and potential unauthorized network access. You are tasked with implementing basic security monitoring procedures and responding to these simulated incidents.

**Tasks:**

1.  **Firewall Logging Setup:**
    * Configure Windows Firewall to log dropped packets and successful connections.
    * Document the steps taken to enable logging, including screenshots.
2.  **Event Log Monitoring:**
    * Configure Event Viewer to monitor security-related events, specifically:
        * Failed logon attempts (Event ID 4625)
        * Successful logon attempts (Event ID 4624)
        * Process creation (Event ID 4688)
    * Create custom views or filters to streamline monitoring.
    * Document the steps taken, including screenshots of your configured event viewer.
3.  **Simulated Security Events:**
    * **Failed Logon Attempts:**
        * Simulate multiple failed logon attempts to a local user account.
        * Capture screenshots of the corresponding events in the security event logs.
    * **Unauthorized Network Access:**
        * Configure remote desktop access to the machine.
        * Remember only users who are part of the administators group will be able to log-in via Remote Desktop Connection (RDC).
        * Create a firewall rule that blocks a TCP port 3389 (The RDC port).
        * Attempt to connect to that port from another machine or using Remote Desktop Connection.
        * Capture screenshots of the blocked connection attempt and the corresponding firewall log entries.
    * **Suspicious Process Creation:**
        * Create a text file, and then rename it to a .exe file.
        * Execute the file.
        * Capture screenshots of the process creation event in the security event logs.
4.  **Incident Response:**
    * For each simulated security event, write a brief incident report that includes:
        * Description of the event.
        * Steps taken to identify the event.
        * Recommended response or mitigation measures.
5.  **Reflection:**
    * Write a short reflection (200-300 words) discussing:
        * The challenges you faced during the project.
        * The importance of security monitoring.
        * How you would improve your monitoring and response procedures in a real-world scenario.

**Deliverables:**

1.  **Documentation:** A document (PDF or Word) containing:
    * Screenshots of firewall logging setup.
    * Screenshots of Event Viewer configuration.
    * Screenshots of simulated security events.
    * A simple Incident reports for each simulated event.
    * A brief paragraph for Reflection.  
2.  **Firewall Configuration:** Export your firewall configuration as a `.wfw` file.

**Evaluation Criteria:**

* Accuracy and completeness of monitoring setup.
* Effectiveness of simulated security events.
* Clarity and thoroughness of incident reports.
* Insightfulness of the reflection.
* Quality of documentation.

**Submission:**

* Submit your documentation and firewall configuration file (if applicable) through the course's submission platform.

**Due Date:**

* See BrightSpace

**Important Notes:**

* Use a virtual machine for this project to avoid disrupting your primary system.
* Ensure you have administrator privileges on your Windows machine.
* Document your steps clearly and concisely.
* This project is designed to give you a basic understanding of security monitoring. Real world security monitoring is much more in depth.
