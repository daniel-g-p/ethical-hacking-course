# Ethical Hacking Course

## 1. Networking

### IP Addresses

- IP = Internet Protocol (Logical Address: WHERE is the device)
- "ipconfig -all" command
- IP address classes
  - Class A: 10.0.0.0 (Mask 255.0.0.0)
  - Class B: 172.16.0.0 - 172.31.0.0 (Mask 255.255.0.0)
  - Class C: 192.168.0.0 - 192.168.255.255 (Mask 255.255.255.0)
  - Loopback: 127.0.0.1 - 127.0.0.7 (Mask 255.255.255.0)

### MAC Addresses

- MAC = Media Access Control (Physical Address: WHO is the device)

### Internet Protocols

- TCP = Transmission Control Protocol (connection-based, reliable)
- UDP = User Datagram Protocol (not connection-based, fast)
- TCP uses a three-way handshake (SYN => SYN ACK => ACK)

### Common Ports

- TCP
  - FTP (File Transfer Protocol, Port 21)
  - SSH (Secure Shell, Port 22)
  - Telnet (SSH without encryption, Port 23)
  - SMTP (Simple Mail Transfer Protocol, Port 25)
  - DNS (Domain Name System, Port 53)
  - HTTP (Hypertext Transfer Protocol, Port 80)
  - HTTPS (HTTP with encryption, 443)
  - POP3 (Post Office Protocol, Port 110)
  - SMB (Server Message Block, Port 139/445)
  - IMAP (Internet Message Access Protocol, Port 143)
- UDP
  - DNS (Domain Name System, Port 53)
  - DHCO (Dynamic Host Configuration Protocol, Port 67/68)
  - TFTP (Trivial File Transport Protocol, Port 69)
  - SNMP (Simple Network Management Protocol, Port 161)

### OSI Model

- Mnemonic: Please Do Not Throw Sausage Pizza Away (PDNTSPA)
- Layers
  1. Physical
  2. Data
  3. Network
  4. Transport
  5. Session
  6. Presentation
  7. Application

## 2. Subnetting

### Subnet Masks

- CIDR (/32, /24, /16, /8) defines the number of hosts that a network supports
- 00000000.00000000.00000000.00000000 (0.0.0.0) - 11111111.11111111.11111111.11111111 (255.255.255.255)
- Within a CIDR, the first IP address is used as Network ID and the last IP address as the Broadcast ID

## 3. Kali Linux

### Command Line Commands

- echo {OUTPUT} > {FILE}: Return output
- chmod {PERMISSIONS} {FILE}: Change file permissions
- adduser {USERNAME}: Add user
- sudo: Run command with root permissions
- su {USERNAME}: Switch user
- usermod -aG {GROUP} {USERNAME}: Add user to group
- ifconfig: Show IP address information
- iwconfig: SHow wireless connection information
- ip a: View all networking information
- ip n: 
- ip r: View routing table
- ping: Ping machine
- service {SERVICE} start: Start service
- service {SERVICE} stop: Stop service
- python3 -m http.server {PORT}: Serve current directory contents as web server
- apt install {PACKAGE}: Install a package
- apt update: Update packages' index files 
- apt upgrade: Update packages

### Important Files

- /etc/passwd (Users): {USERNAME}:{PASSWORD}:{USER_ID}:{GROUP_ID}:{USER_INFO}:{HOME_FOLDER}:{SHELL_BINARY}
- /etc/shadow (Passwords): {USERNAME}:{PASSWORD}:{LAST_UPDATE}:{MINIMUM_DAYS}:{MAXIMUM_DAYS}:{WARNING_DAYS}:{INACTIVE_DAYS}:{EXPIRATION_DATE}
- /etc/group (Groups): {GROUP}:{PASSWORD}:{GROUP_ID}:{GROUP_MEMBERS}

### Kali Linux Specialties

- Don't upgrade packages in Kali Linux, it potentially breaks its functionality
- pimpmykali (https://github.com/Dewalt-arch/pimpmykali): Package to customize Kali Linux

### Ping Sweeping

## 4. Ethical Hacking Introduction

### Ethical Hacking Cycle

- Stage 1: Information Gathering
- Stage 2: Scanning & Research
- Stage 3: Access Gaining
- Stage 4: Access Maintenance
- Stage 5: Cleanup

### Email Discovery

- Email discovery websites:
  - phonebook.cz
  - hunter.io
  - voilanorbert.com
  - clearbit.com
  - emailhippo.com
- Account Recovery process for email verification
- Data breach databases
  - dehashed.com

### Subdomain Listing

- sublist3r (Shell)
- crt.sh (Web)
- OWASP Amass (Shell)

### Tech Stack Scanning

- builtwith.com (Web)
- wappalyzer.com (Web)
- whatweb (Shell)

