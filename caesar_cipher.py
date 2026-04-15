# Caesar Cipher with User Choice (Encrypt / Decrypt / Brute Force)

def encrypt(text, key):
    result = ""
    
    for char in text:
        if char.isalpha():
            shift = key % 26
            
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
            
    return result


def decrypt(text, key):
    return encrypt(text, -key)


def brute_force(cipher_text):
    print("\nBrute Force Results:\n")
    for key in range(1, 26):
        print(f"Key {key}: {decrypt(cipher_text, key)}")


# 🔹 Menu
print("=== Caesar Cipher Tool ===")
print("1. Encrypt")
print("2. Decrypt")
print("3. Brute Force Attack")

choice = input("Enter your choice (1/2/3): ")

# 🔹 User Input
text = input("Enter your text: ")

if choice == "1":
    key = int(input("Enter key (number): "))
    print("\nEncrypted Text:", encrypt(text, key))

elif choice == "2":
    key = int(input("Enter key (number): "))
    print("\nDecrypted Text:", decrypt(text, key))

elif choice == "3":
    brute_force(text)

else:
    print("Invalid choice ❌")
