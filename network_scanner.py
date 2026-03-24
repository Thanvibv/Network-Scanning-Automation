# network_scanner.py
# Unified tool combining Ping, ARP, and Nmap

import subprocess
import platform
import re

# Ping Function
def ping_host(host):
    os_type = platform.system().lower()
    param = "-n" if os_type == "windows" else "-c"

    result = subprocess.run(["ping", param, "2", host], stdout=subprocess.PIPE, text=True)

    if result.returncode == 0:
        print(host, "is Reachable")
    else:
        print(host, "is Not Reachable")

# ARP Function
def arp_scan():
    result = subprocess.run("arp -a", stdout=subprocess.PIPE, text=True)
    pattern = r"(\d+\.\d+\.\d+\.\d+)\s+([a-f0-9-]+)"
    matches = re.findall(pattern, result.stdout)

    print("IP\t\tMAC")
    for ip, mac in matches:
        print(ip, "\t", mac)

# Nmap Function
def nmap_scan(target):
    result = subprocess.run(["nmap", target], stdout=subprocess.PIPE, text=True)
    print(result.stdout)

# Main Menu
if __name__ == "__main__":
    while True:
        print("\n=== Network Scanner ===")
        print("1. Ping Scan")
        print("2. ARP Scan")
        print("3. Nmap Scan")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            host = input("Enter IP: ")
            ping_host(host)
        elif choice == "2":
            arp_scan()
        elif choice == "3":
            target = input("Enter target IP: ")
            nmap_scan(target)
        elif choice == "4":
            break
        else:
            print("Invalid choice")
