"""
=======================================================
 Project 2: Text Encryption and Decryption Tool
 Concept   : Strings, User-Defined Functions
 Course    : B.Tech CSE - 3rd Semester
=======================================================

This program encrypts and decrypts text using two classic
substitution ciphers: the Caesar Cipher and the Vigenere
Cipher. Built entirely with user-defined functions and
Python's string/character operations (ord, chr).
"""


# ---------------- CAESAR CIPHER ----------------

def caesar_encrypt(text, shift):
    """Encrypt text using the Caesar Cipher by shifting letters forward."""
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    """Decrypt Caesar Cipher text by shifting letters backward."""
    return caesar_encrypt(text, -shift)


# ---------------- VIGENERE CIPHER ----------------

def vigenere_encrypt(text, key):
    """Encrypt text using the Vigenere Cipher with the given keyword."""
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        else:
            result += char
    return result


def vigenere_decrypt(text, key):
    """Decrypt Vigenere Cipher text using the same keyword."""
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.isupper():
                result += chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            key_index += 1
        else:
            result += char
    return result


# ---------------- VALIDATION FUNCTIONS ----------------

def is_valid_shift(shift_str):
    """Check whether the provided shift value is a valid integer."""
    try:
        int(shift_str)
        return True
    except ValueError:
        return False


def is_valid_key(key):
    """Check whether the provided Vigenere key contains only letters."""
    return key.isalpha() and len(key) > 0


# ---------------- MENU HANDLERS ----------------

def caesar_menu():
    """Handle user interaction for the Caesar Cipher option."""
    text = input("Enter the text: ")
    shift_str = input("Enter shift value (integer): ")

    if not is_valid_shift(shift_str):
        print("Invalid shift value. Please enter an integer.")
        return

    shift = int(shift_str)
    choice = input("Encrypt or Decrypt? (E/D): ").strip().upper()

    if choice == "E":
        print("Encrypted Text:", caesar_encrypt(text, shift))
    elif choice == "D":
        print("Decrypted Text:", caesar_decrypt(text, shift))
    else:
        print("Invalid choice. Please enter E or D.")


def vigenere_menu():
    """Handle user interaction for the Vigenere Cipher option."""
    text = input("Enter the text: ")
    key = input("Enter keyword (letters only): ").strip()

    if not is_valid_key(key):
        print("Invalid key. Please enter alphabetic characters only.")
        return

    choice = input("Encrypt or Decrypt? (E/D): ").strip().upper()

    if choice == "E":
        print("Encrypted Text:", vigenere_encrypt(text, key))
    elif choice == "D":
        print("Decrypted Text:", vigenere_decrypt(text, key))
    else:
        print("Invalid choice. Please enter E or D.")


# ---------------- MAIN DRIVER FUNCTION ----------------

def main():
    print("=" * 50)
    print("     TEXT ENCRYPTION AND DECRYPTION TOOL")
    print("=" * 50)

    while True:
        print("\n1. Caesar Cipher")
        print("2. Vigenere Cipher")
        print("3. Exit")

        option = input("Choose an option (1/2/3): ").strip()

        if option == "1":
            caesar_menu()
        elif option == "2":
            vigenere_menu()
        elif option == "3":
            print("Thank you for using the tool. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
