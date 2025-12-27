import os
import subprocess
import datetime

def banner():
    print("""
    #################################################
    #        KALI EXPERT - AUTO RECON TOOL          #
    #        Developed for: MATHEUS TI              #
    #################################################
    """)

def run_recon(target):
    print(f"[*] Starting reconnaissance on: {target}")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"reports/recon_{target}_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)

    # 1. Nmap Scan Simple
    print("[+] Running Nmap Scan...")
    nmap_log = os.path.join(output_dir, "nmap_scan.txt")
    with open(nmap_log, "w") as f:
        subprocess.run(["nmap", "-sV", target], stdout=f, stderr=subprocess.PIPE, text=True)
    
    # 2. Whois
    print("[+] Running Whois...")
    whois_log = os.path.join(output_dir, "whois.txt")
    with open(whois_log, "w") as f:
        subprocess.run(["whois", target], stdout=f, stderr=subprocess.PIPE, text=True)

    print(f"\n[!] Reconnaissance complete! Reports saved in: {output_dir}")

if __name__ == "__main__":
    banner()
    target = input("Enter target IP or Domain: ")
    if target:
        run_recon(target)
    else:
        print("[-] Target missing. Exiting.")
