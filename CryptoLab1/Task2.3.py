from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os, base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

backend = default_backend()
salt = os.urandom(16)

kdf_key = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=16,
    salt=salt,
    iterations=100000,
    backend=backend
)

kdf_iv = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=16,
    salt=salt,
    iterations=100000,
    backend=backend
)

passwd = input("Enter password: ").encode() 
iv_seed = input("Enter IV seed: ").encode()  


key = kdf_key.derive(passwd)
iv = kdf_iv.derive(iv_seed)

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

# Padding setup
padder = padding.PKCS7(128).padder()
unpadder = padding.PKCS7(128).unpadder()

# Example data
mydata = b'123456781234567'  # 15 bytes data
print("Original data:", mydata)

# Pad the data
mydata_padded = padder.update(mydata) + padder.finalize()
print("Padded data (hex):", mydata_padded.hex())

# Encrypt
encryptor = cipher.encryptor()
ciphertext = encryptor.update(mydata_padded) + encryptor.finalize()
print("Encrypted (hex):", ciphertext.hex())

# Decrypt
decryptor = cipher.decryptor()
padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

# Unpad decrypted data
plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
print("Decrypted (hex):", plaintext)

# Optionally print in base64
print("Key (base64):", base64.b64encode(key).decode())
print("IV (base64):", base64.b64encode(iv).decode())
print("Ciphertext (base64):", base64.b64encode(ciphertext).decode())
