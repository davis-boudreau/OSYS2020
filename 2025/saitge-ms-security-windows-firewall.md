## Reflective Practical Lab: Configuring Windows Firewall and Analyzing Event Logs

**Outcome 2: Students will create and test firewall rules and analyze security event logs to identify potential threats.**

**Estimated Time:** 2-3 hours

**Materials:**

* Windows 10/11 virtual machine or physical machine
* Administrator access
* Text editor (e.g., Notepad, Notepad++)
* (Optional) Network traffic monitoring tool (e.g., Wireshark)

**Introduction:**

Windows Firewall is a crucial component of system security, controlling network traffic entering and leaving your computer. Security event logs provide a detailed record of system activities, including logon attempts, resource access, and security-related events. This lab will guide you through configuring firewall rules and analyzing event logs to enhance your understanding of Windows security.

**Part 1: Configuring Windows Firewall Rules (Tutorial & Practical)**

**Tutorial:**

1.  **Access Windows Firewall:**
    * Open the Control Panel.
    * Navigate to System and Security > Windows Defender Firewall.
    * Click "Advanced settings" in the left pane.

2.  **Understanding Firewall Rules:**
    * Familiarize yourself with the inbound and outbound rules.
    * Understand the concepts of protocols (TCP, UDP, ICMP), ports, and actions (allow, block).

3.  **Creating a New Inbound Rule:**
    * In the "Windows Defender Firewall with Advanced Security" window, select "Inbound Rules."
    * Click "New Rule..." in the right pane.
    * Choose the rule type (e.g., Port, Program, Predefined).
    * Configure the rule details (e.g., port number, protocol, action).
    * Specify the profile (Domain, Private, Public).
    * Name and describe the rule.

4.  **Testing the Rule:**
    * Use a network utility (e.g., `telnet`, `ping`) or another machine to test the rule's effect.
    * For example, if you blocked port 80, attempt to connect to a web server on the machine and observe the failure. if you opened a port, confirm a connection can be established.

**Practical:**

1.  **Scenario 1: Block ICMP Echo Requests (Ping):**
    * Create an inbound rule to block ICMP echo requests.
    * Test the rule by pinging the machine from another device.
    * Reflect: Why is blocking ICMP sometimes useful? What are the potential drawbacks?

2.  **Scenario 2: Allow Remote Desktop Connection (RDP) from a Specific IP Address:**
    * Create an inbound rule to allow RDP connections (port 3389) only from a specific IP address.
    * Test the rule by attempting to connect from the allowed and disallowed IP addresses.
    * Reflect: What are the security benefits of restricting RDP access?

3.  **Scenario 3: Block a Specific Program's Outbound Internet Access:**
    * Locate a program on your computer that connects to the internet.
    * Create an outbound firewall rule to block the program's internet access.
    * Test the rule by running the program and observing its network behavior.
    * Reflect: When might you want to block a program's outbound access?

**Part 2: Analyzing Security Event Logs (Tutorial & Practical)**

**Tutorial:**

1.  **Access Event Viewer:**
    * Search for "Event Viewer" in the Windows search bar.
    * Open Event Viewer.

2.  **Navigate to Security Logs:**
    * In the left pane, expand "Windows Logs" and select "Security."

3.  **Understanding Event IDs:**
    * Familiarize yourself with common security event IDs (e.g., 4624 - successful logon, 4625 - failed logon, 4688 - process creation).
    * Use Microsoft's documentation to look up event ID's.

4.  **Filtering and Searching Logs:**
    * Use the "Filter Current Security Log..." option to filter events by event ID, time range, user, etc.
    * Use the "Find..." option to search for specific keywords.

**Practical:**

1.  **Scenario 1: Identify Failed Logon Attempts:**
    * Filter the security logs for event ID 4625 (failed logon).
    * Analyze the details of the failed logon attempts (e.g., user name, source IP address).
    * Reflect: What might multiple failed logon attempts indicate?

2.  **Scenario 2: Track Process Creation:**
    * Filter the security logs for event ID 4688 (process creation).
    * Examine the process names and user accounts associated with the created processes.
    * Reflect: How can process creation logs help detect malware or unauthorized activity?

3.  **Scenario 3: Analyze Firewall Events:**
    * Enable the Windows Firewall logging.
    * Filter the security logs for firewall related events.
    * Analyze the logs to find information about allowed or blocked connections.
    * Reflect: How can firewall logs aid in troubleshooting network issues and identifying security threats?

**Reflection:**

* What did you learn about configuring Windows Firewall rules?
* How did analyzing security event logs enhance your understanding of system security?
* What are some real-world applications of these skills?
* What challenges did you face, and how did you overcome them?
* How would you improve your security posture based on what you have learned?
