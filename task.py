def caesar_cipher_encrypt(plaintext, shift): 
    encrypted = ""
    for char in plaintext:
        if char.isalpha():  
            offset = 65 if char.isupper() else 97
            encrypted += chr((ord(char) + shift - offset) % 26 + offset)
        else:
            encrypted += char
    return encrypted

def caesar_cipher_decrypt(ciphertext, shift):
    """Decrypt a ciphertext using a Caesar shift cipher."""
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():  
            offset = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - shift - offset) % 26 + offset)
        else:
            decrypted += char
    return decrypted

# Example given:
original_text = "if we all unite we will cause the rivers to stain the great waters with her blood"
shift_key = 3 #shift key value

# Example Encrypt the original text
encrypted_text = caesar_cipher_encrypt(original_text, shift_key)
print(f"Encrypted text: {encrypted_text}")

# Example Decrypt the encrypted text
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift_key)
print(f"Decrypted text: {decrypted_text}")
