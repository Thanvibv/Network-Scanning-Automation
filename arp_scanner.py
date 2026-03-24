# arp_scanner.py
# This program retrieves ARP table and extracts IP-MAC mapping

import subprocess
import re

def arp_scan():
    print("=== ARP Scanner ===")
    print("Scanning ARP table...\n")

    # Run arp command
    result = subprocess.run("arp -a", stdout=subprocess.PIPE, text=True)
    output = result.stdout

    # Regex pattern to extract IP and MAC address
    pattern = r"(\d+\.\d+\.\d+\.\d+)\s+([a-f0-9-]+)"
    matches = re.findall(pattern, output)

    print("IP Address\t\tMAC Address")
    print("----------------------------------------")

    # Display results
    for ip, mac in matches:
        print(f"{ip}\t\t{mac}")

    print("\nTotal Entries:", len(matches))

    # Save results to file (bonus marks feature)
    with open("arp_results.txt", "w") as f:
        f.write("IP Address - MAC Address\n")
        for ip, mac in matches:
            f.write(f"{ip} - {mac}\n")

    print("\nResults saved to arp_results.txt")

# Main
if __name__ == "__main__":
    arp_scan()
