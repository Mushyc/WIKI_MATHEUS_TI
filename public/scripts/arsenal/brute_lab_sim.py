import time

def banner():
    print("""
    #################################################
    #        KALI EXPERT - BRUTE FORCE SIM          #
    #        (Learning Lab Environment)             #
    #################################################
    """)

def simulate_brute(target_user, password_list):
    correct_pass = "admin123"
    print(f"[*] Starting brute force simulation on user: {target_user}")
    print(f"[*] Dictionary size: {len(password_list)} words\n")
    
    for password in password_list:
        print(f"[#] Trying: {password}...", end="\r")
        time.sleep(0.1) # Simulate network lag
        if password == correct_pass:
            print(f"\n[+] SUCCESS! Password found: {password}")
            return
    
    print("\n[-] FAILED. Password not in dictionary.")

if __name__ == "__main__":
    banner()
    user = input("Target Username: ")
    passwords = ["123456", "password", "qwerty", "admin123", "root", "p@ssword"]
    simulate_brute(user, passwords)
