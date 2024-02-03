import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Generate key and IV for AES
key = os.urandom(32)  # AES-256
iv = os.urandom(16)   # For modes like CFB or CBC

# Encrypt alice2.txt
with open("alice2.txt", "rb") as file:
    plaintext = file.read()

cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext) + encryptor.finalize()

# Save encrypted data
with open("alice2.enc", "wb") as file:
    file.write(ciphertext)

# Save key and IV in PEM format
skiv = f"-----BEGIN SKEY-----\n{base64.b64encode(key).decode()}\n-----END SKEY-----\n-----BEGIN IV-----\n{base64.b64encode(iv).decode()}\n-----END IV-----"
with open("alice2.skiv", "w") as file:
    file.write(skiv)
