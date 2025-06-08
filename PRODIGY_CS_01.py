def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift within alphabet
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep non-alphabet characters unchanged
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    
    if choice not in ('E', 'D'):
        print("Invalid choice.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    if choice == 'E':
        encrypted = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", encrypted)
    else:
        decrypted = caesar_cipher_decrypt(message, shift)
        print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
