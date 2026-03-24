# ping_scanner.py
# This program pings a host and checks if it is reachable
# It also extracts the average response time

import subprocess   # To run system commands like ping
import platform     # To detect OS (Windows/Linux/Mac)
import re           # To extract time using regex

def ping_host(host):
    # Detect operating system
    os_type = platform.system().lower()
    
    # Windows uses -n, Linux/Mac uses -c
    if os_type == "windows":
        param = "-n"
    else:
        param = "-c"

    try:
        # Run ping command
        result = subprocess.run(
            ["ping", param, "4", host],  # Ping 4 times
            stdout=subprocess.PIPE,      # Capture output
            stderr=subprocess.PIPE,
            text=True,                   # Output as text
            timeout=10                   # Timeout after 10 sec
        )

        # If ping successful
        if result.returncode == 0:
            print(f"\nHost: {host}")
            print("Status: Reachable")

            # Extract average time (Windows format)
            avg_time = re.findall(r"Average = (\d+)ms", result.stdout)
            if avg_time:
                print("Average Response Time:", avg_time[0], "ms")
        else:
            print("Status: Not Reachable")

    except subprocess.TimeoutExpired:
        print("Request Timed Out")

# Main program
if __name__ == "__main__":
    print("=== Ping Scanner ===")
    
    choice = input("Ping multiple hosts? (y/n): ")

    if choice.lower() == 'y':
        hosts = input("Enter multiple IPs separated by space: ").split()
        for host in hosts:
            ping_host(host)
    else:
        host = input("Enter IP or Hostname: ")
        ping_host(host)
