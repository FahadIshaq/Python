from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os, base64

# Backend and salt setup (from previous task)
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
# Create Cipher Object
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)


# Encrypt Data
encryptor = cipher.encryptor()
mydata = b'1234567812345678'  # 16 bytes data (AES block size)
print("Original data:", mydata)
ciphertext = encryptor.update(mydata) + encryptor.finalize()
print("Encrypted (hex):", ciphertext.hex())

# Decrypt Data
decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext) + decryptor.finalize()
print("Decrypted (hex):", plaintext)

# Optionally print in base64
print("Key (base64):", base64.b64encode(key).decode())
print("IV (base64):", base64.b64encode(iv).decode())
print("Ciphertext (base64):", base64.b64encode(ciphertext).decode())
