# Vigenère Cipher in Python

def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def encrypt(text, key):
    result = ""
    key = generate_key(text, key)
    
    for i in range(len(text)):
        char = text[i]
        
        if char.isalpha():
            shift = ord(key[i].lower()) - ord('a')
            
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
            
    return result


def decrypt(cipher_text, key):
    result = ""
    key = generate_key(cipher_text, key)
    
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        
        if char.isalpha():
            shift = ord(key[i].lower()) - ord('a')
            
            if char.islower():
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            result += char
            
    return result


# 🔹 User Input
text = input("Enter text: ")
key = input("Enter key (word): ")

# 🔹 Encryption
encrypted = encrypt(text, key)
print("\nEncrypted:", encrypted)

# 🔹 Decryption
decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)