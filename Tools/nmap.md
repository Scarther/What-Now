# NMAP
  * nmap is a great tool for network recon. Working in a comand line/terminal only status. 
  * This terminal command can scan IPv4 and IPv6

# --help commands
```
TARGET SPECIFICATION:
  Can pass hostnames, IP addresses, networks, etc.
  Ex: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254
  -iL <inputfilename>: Input from list of hosts/networks
  -iR <num hosts>: Choose random targets
  --exclude <host1[,host2][,host3],...>: Exclude hosts/networks
  --excludefile <exclude_file>: Exclude list from file
HOST DISCOVERY:
  -sL: List Scan - simply list targets to scan
  -sn: Ping Scan - disable port scan
  -Pn: Treat all hosts as online -- skip host discovery
  -PS/PA/PU/PY[portlist]: TCP SYN, TCP ACK, UDP or SCTP discovery to given ports
  -PE/PP/PM: ICMP echo, timestamp, and netmask request discovery probes
  -PO[protocol list]: IP Protocol Ping
  -n/-R: Never do DNS resolution/Always resolve [default: sometimes]
  --dns-servers <serv1[,serv2],...>: Specify custom DNS servers
  --system-dns: Use OS's DNS resolver
  --traceroute: Trace hop path to each host
SCAN TECHNIQUES:
  -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
  -sU: UDP Scan
  -sN/sF/sX: TCP Null, FIN, and Xmas scans
  --scanflags <flags>: Customize TCP scan flags
  -sI <zombie host[:probeport]>: Idle scan
  -sY/sZ: SCTP INIT/COOKIE-ECHO scans
  -sO: IP protocol scan
  -b <FTP relay host>: FTP bounce scan
PORT SPECIFICATION AND SCAN ORDER:
  -p <port ranges>: Only scan specified ports
    Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
  --exclude-ports <port ranges>: Exclude the specified ports from scanning
  -F: Fast mode - Scan fewer ports than the default scan
  -r: Scan ports sequentially - don't randomize
  --top-ports <number>: Scan <number> most common ports
  --port-ratio <ratio>: Scan ports more common than <ratio>
SERVICE/VERSION DETECTION:
  -sV: Probe open ports to determine service/version info
  --version-intensity <level>: Set from 0 (light) to 9 (try all probes)
  --version-light: Limit to most likely probes (intensity 2)
  --version-all: Try every single probe (intensity 9)
  --version-trace: Show detailed version scan activity (for debugging)
SCRIPT SCAN:
  -sC: equivalent to --script=default
  --script=<Lua scripts>: <Lua scripts> is a comma separated list of
           directories, script-files or script-categories
  --script-args=<n1=v1,[n2=v2,...]>: provide arguments to scripts
  --script-args-file=filename: provide NSE script args in a file
  --script-trace: Show all data sent and received
  --script-updatedb: Update the script database.
  --script-help=<Lua scripts>: Show help about scripts.
           <Lua scripts> is a comma-separated list of script-files or
           script-categories.
OS DETECTION:
  -O: Enable OS detection
  --osscan-limit: Limit OS detection to promising targets
  --osscan-guess: Guess OS more aggressively
TIMING AND PERFORMANCE:
  Options which take <time> are in seconds, or append 'ms' (milliseconds),
  's' (seconds), 'm' (minutes), or 'h' (hours) to the value (e.g. 30m).
  -T<0-5>: Set timing template (higher is faster)
  --min-hostgroup/max-hostgroup <size>: Parallel host scan group sizes
  --min-parallelism/max-parallelism <numprobes>: Probe parallelization
  --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>: Specifies
      probe round trip time.
  --max-retries <tries>: Caps number of port scan probe retransmissions.
  --host-timeout <time>: Give up on target after this long
  --scan-delay/--max-scan-delay <time>: Adjust delay between probes
  --min-rate <number>: Send packets no slower than <number> per second
  --max-rate <number>: Send packets no faster than <number> per second
FIREWALL/IDS EVASION AND SPOOFING:
  -f; --mtu <val>: fragment packets (optionally w/given MTU)
  -D <decoy1,decoy2[,ME],...>: Cloak a scan with decoys
  -S <IP_Address>: Spoof source address
  -e <iface>: Use specified interface
  -g/--source-port <portnum>: Use given port number
  --proxies <url1,[url2],...>: Relay connections through HTTP/SOCKS4 proxies
  --data <hex string>: Append a custom payload to sent packets
  --data-string <string>: Append a custom ASCII string to sent packets
  --data-length <num>: Append random data to sent packets
  --ip-options <options>: Send packets with specified ip options
  --ttl <val>: Set IP time-to-live field
  --spoof-mac <mac address/prefix/vendor name>: Spoof your MAC address
  --badsum: Send packets with a bogus TCP/UDP/SCTP checksum
OUTPUT:
  -oN/-oX/-oS/-oG <file>: Output scan in normal, XML, s|<rIpt kIddi3,
     and Grepable format, respectively, to the given filename.
  -oA <basename>: Output in the three major formats at once
  -v: Increase verbosity level (use -vv or more for greater effect)
  -d: Increase debugging level (use -dd or more for greater effect)
  --reason: Display the reason a port is in a particular state
  --open: Only show open (or possibly open) ports
  --packet-trace: Show all packets sent and received
  --iflist: Print host interfaces and routes (for debugging)
  --append-output: Append to rather than clobber specified output files
  --resume <filename>: Resume an aborted scan
  --noninteractive: Disable runtime interactions via keyboard
  --stylesheet <path/URL>: XSL stylesheet to transform XML output to HTML
  --webxml: Reference stylesheet from Nmap.Org for more portable XML
  --no-stylesheet: Prevent associating of XSL stylesheet w/XML output
MISC:
  -6: Enable IPv6 scanning
  -A: Enable OS detection, version detection, script scanning, and traceroute
  --datadir <dirname>: Specify custom Nmap data file location
  --send-eth/--send-ip: Send using raw ethernet frames or IP packets
  --privileged: Assume that the user is fully privileged
  --unprivileged: Assume the user lacks raw socket privileges
  -V: Print version number
  -h: Print this help summary page.
EXAMPLES:
  nmap -v -A scanme.nmap.org
  nmap -v -sn 192.168.0.0/16 10.0.0.0/8
  nmap -v -iR 10000 -Pn -p 80
SEE THE MAN PAGE (https://nmap.org/book/man.html) FOR MORE OPTIONS AND EXAMPLES
```

# Basic Commands
*We will say that the test IP is 192.168.1.1*
**You can scan IPv4, IPv6 and domains (websites)**

Scan top 1,000 TCP ports on target IP
```
nmap 192.168.1.1
```
Scan Specific Ports
```
nmap -p 80,443,22 192.168.1.1
```
Scan Ranges - Identifies software versions running on ports
```
nmap -p 1-1000 192.168.1.1
```
Aggressive scan - Enables OS detection, version detection, script scanning and traceroute
```
nmap -A 192.168.1.1
```
Ping Scan (Host Directory) - Lists active devices without port scanning
```
nmap -sn 192.168.1.0/24
```
Fast Scan
```
nmap -F 192.168.1.1
```

# WTF is this Port? 
Now that we have some basics down, we need to look into what these open ports are and what they do.

*This can help with Identifying Ports*

[Speed Guide - Port Identificaiton](https://www.speedguide.net/ports.php)
[iana port assignments](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt)


# What Now?
So, you get on your neighbors wifi, or have an IP that you want to see whats on the network. These scans are for if you are already on the network. 
*Whether it be open networks or local password protected you just came across ;)*


### 1) Discovery of all devices on local network
Lets start with a fast and sneaky scan using the IPv4 and IPv6 of the network
```
nmap -sn 192.168.1.0/24
```

```
nmap -sn -6 fe80::/10
```
**Remmeber**
* Change the IP and the subnet. The example subnet is 24 and 10

### 2) Scan a specific target for open ports and services
***IF*** you are on the WiFi after getting a successful handshake and want to see whats on it, use the following command
```
nmap -6 -sV -O -p- -e wlan0 fe80::
```
For IPv4 use the following
```
nmap -sV -O -p- -e wlan0 192.168.1.1
```

If we look at the top of the *--help*, we can see what the following commands do

**-6**
This is for IPv6 specific
**-sV**
Probe open ports to determine service and version info
**-O**
Detect the operating system
**-p-**
Scan all 65,535 ports on the network - *This will take some time, use **-p** for a faster stan*
**-e wlan0**
Specify the interface that you are scanning from. Usually on Linux systems, the connected WiFi will be *wlan0*, ethernet is *eth0*

### 3) Look for Vulnerabilities with Nmap Scripts
IPv4 scan
```
nmap -sV --script default,safe,vuln -e wlan0 192.168.1.1
```

```
nmap -6 -sV --script default,safe,vuln -e wlan0 fe80::
```

This scan will run *Default*, *Safe*, and *Vulnerability* Scripts on the target network for IPv4 and IPv6.
**What you'll see:**Nmap will execute its suite of scripts against the target network and report any cindings. These will look for weak SSL ciphers or potential vulnerabilities.

### 4) Target Specific Services
This would be for specific ports

You can run scripts against specific services you discovered. These are examples of ports that were discovered as open or in use that you can specifically target. 

***This will find an open web server (port 80/443)***
*443* is usually encrypted but local web servers will be on these ports like the wifi router for example
```
nmap -p 80,443 --script http-enum,http-vuln* -e wlan0 192.168.1.1
```

```
nmap -6 -p 80,443 --script http-enum,http-vuln* -e wlan0 fe80::
```

***This will find an open SMB/Windows Share (port 445)***
```
nmap -p 445 --script smb-enum-shares, smb-enum-users -r wlan0 192.168.1.1
```

```
nmap -6 -p 445 --script smb-enum-shares,smb-enum-users -r wlan0 fe80::
```

***This will find open MySQL/MariaDB database (port 3306)***
```
nmap -p 4406 --script mysql-empty-password,mysql-brute -e wlan0 192.169.1.1
```

```
nmap -6 -p 4406 --script mysql-empty-password,mysql-brute -e wlan0 fe80::
```

# Alternative & Complementary Discovery Tools
***These are tools to go with nmap and compliment discoveries***

### 1) Ping6
```
ping6 -I wlan0 -c 4 fe80::
```

```
ping6 -I wlan0 -c 4 192.168.1.1
```

*There is no needed specific command needed for IPv6 or IPv4*

**Ping the IP all-nodes multicast address**
***-I wlan0*** - Specify the interface
***-c 4*** - Send 4 pings

**What you'll see:** Responses from every device on the local link, showing you their IP addresses

### 2) ndisc6
***This is for Neighbor Discovery***
Specificy a tool for IPv6

*This will discover the link-layer address (MAC) of an IPv6 host*
```
ndisc6 fe80:: wlan0
```
*Discover all neighbors on the interface*
```
rdisc6 wlan0
```

# Oh Yeah... It's All Coming Together:
This Nmap Command is the quick catch all ***Recon Command***
*IPv4*
```
nmap -sn 192.168.1.0/24 -e wlan0 | awk '/is up/ {print $2}' | nmap -iL - --script default,safe -e wlan0
```
*IPv6*
```
nmap -6 -sn fe80::/10 -e wlan0 | awk '/is up/ {print $2}' | nmap -6 -iL - --script default,safe -e wlan0
```

## Know the difference between IPv4 and IPv6
* **Not Network Scanning:** Forget trying to scan a 2001:db8::/64 range. Its computationally impossible and not how things are done. *Focus on local link discovery*
* **Link-Local is Key:** The fe80::/10 address is your primary target for initial discovery on a network you've just joined. This also goes with the IPv4 address. Local IP's give more information.
* **Interface Specification:** Always remember to use *-3 <interface>* when scanning link-local addresses. This is the path that you are connected to the network.
* **Privacy Addresses:** Many devices generate temporary, random global IPv6 addresses to enhance privacy. This means a single device can have multiple active IPv6 addresses, making host tracking more difficult. This could be proxies or the Internet Service Provider that has IP changes and periodic changes to the address.
* **Firewalls:** IPv6 firewalls *(ipv6tables)* can be just as restrictive as IPv4 ones, blocking ports and ICMPv6 messages, which can make discovery harder.
