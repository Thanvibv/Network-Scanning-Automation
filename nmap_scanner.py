# nmap_scanner.py
# This program runs different types of Nmap scans

import subprocess

# Check if Nmap is installed
def check_nmap():
    try:
        subprocess.run(["nmap", "--version"], stdout=subprocess.PIPE)
        return True
    except:
        return False

# Run different Nmap scans
def run_nmap(target, choice):
    if choice == "1":
        command = ["nmap", "-sn", target]   # Host discovery
    elif choice == "2":
        command = ["nmap", target]          # Port scan
    elif choice == "3":
        command = ["nmap", "-sV", target]   # Service version
    elif choice == "4":
        command = ["nmap", "-O", target]    # OS detection
    else:
        print("Invalid choice")
        return

    print("\nScanning... Please wait...\n")
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)

    print("Scan Results:")
    print("====================================")
    print(result.stdout)

    # Save results to file (bonus feature)
    with open("nmap_results.txt", "w") as f:
        f.write(result.stdout)

    print("Results saved to nmap_results.txt")

# Main
if __name__ == "__main__":
    print("=== Nmap Scanner ===")

    if check_nmap():
        print("Nmap is installed")

        target = input("Enter target IP or Network: ")

        print("\nSelect Scan Type:")
        print("1. Host Discovery")
        print("2. Port Scan")
        print("3. Service Version Detection")
        print("4. OS Detection")

        choice = input("Enter choice (1-4): ")
        run_nmap(target, choice)
    else:
        print("Nmap is not installed")
