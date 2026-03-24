*Project Description
This project automates basic network scanning tasks using Python.  
It uses system tools like Ping, ARP, and Nmap and executes them using Python's subprocess module.  
The program can scan hosts, retrieve ARP table entries, and perform network scans using Nmap.

This project is developed as part of the Cybersecurity Assignment – Network Scanning Automation.



*Tools Used
- Python 3
- Nmap
- Ping (Built-in OS tool)
- ARP (Built-in OS tool)
- subprocess module
- platform module
- re module


*How to Install Nmap
1. Go to: https://nmap.org/download.html
2. Download the Windows installer (nmap-setup.exe)
3. Install Nmap
4. Make sure Npcap is installed during setup
5. Verify installation using command:nmap --version


*How to Run Each Program
1. Open Command Prompt.
2. Navigate to the project folder using:
cd "C:\Users\thanv\Assignment 3 Python files"
3. Run Ping Scanner:
Command: python ping_scanner.py
Enter IP address or hostname when prompted.
Example Input: 127.0.0.1
Output: Shows whether host is reachable and average response time.
4. Run ARP Scanner:
Command: python arp_scanner.py
Output: Displays IP and MAC address table and saves results to arp_results.txt.
5. Run Nmap Scanner:
Command: python nmap_scanner.py
Enter target IP when prompted.
Example Input: 127.0.0.1
Output: Displays open ports and services and saves results to nmap_results.txt.
6. Run Unified Network Scanner (Bonus):
Command: python network_scanner.py
Choose option:
1 - Ping Scan
2 - ARP Scan
3 - Nmap Scan


*Example Usage for Each Tool
1. Ping Example:
Command: python ping_scanner.py
Input: 127.0.0.1
Output: Host reachable and response time.
2. ARP Example:
Command: python arp_scanner.py
Output: List of IP and MAC addresses.
3. Nmap Example:
Command: python nmap_scanner.py
Input: 127.0.0.1
Output: List of open ports and services.
4. Unified Tool Example:
Command: python network_scanner.py
Select option 1, 2, or 3 to perform scan.