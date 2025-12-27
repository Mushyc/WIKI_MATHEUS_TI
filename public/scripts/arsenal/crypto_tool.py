import base64

def banner():
    print("""
    #################################################
    #        KALI EXPERT - CRYPTO TOOL              #
    #        (Educational Purpose Only)             #
    #################################################
    """)

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            s = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - start + s) % 26 + start)
        else:
            result += char
    return result

def main():
    banner()
    print("1. Base64 Encode")
    print("2. Base64 Decode")
    print("3. Caesar Cipher (Rotate)")
    choice = input("\nChoice: ")

    if choice == '1':
        text = input("Text to encode: ")
        print(f"Result: {base64.b64encode(text.encode()).decode()}")
    elif choice == '2':
        text = input("Base64 to decode: ")
        try:
            print(f"Result: {base64.b64decode(text).decode()}")
        except:
            print("[-] Invalid Base64")
    elif choice == '3':
        text = input("Text: ")
        shift = int(input("Shift (1-25): "))
        mode = input("Mode (encrypt/decrypt): ").strip().lower()
        print(f"Result: {caesar_cipher(text, shift, mode)}")
    else:
        print("[-] Invalid choice.")

if __name__ == "__main__":
    main()
