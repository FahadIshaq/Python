from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import os

with open("keystore/recipients_keys/nigel_ku.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

# Generate a symmetric  and IV
key = os.urandom(32)  # 256-bit key for AES
iv = os.urandom(16)   # AES block size for IV

with open("testfile.txt", "rb") as f:
    plaintext = f.read()

cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext) + encryptor.finalize()

# Save encrypted file
with open("encrypted_file.enc", "wb") as f:
    f.write(ciphertext)

# PEM format for symmetric key and IV
skiv = f"-----BEGIN SKEY-----\n{base64.b64encode(key).decode()}\n-----END SKEY-----\n-----BEGIN IV-----\n{base64.b64encode(iv).decode()}\n-----END IV-----"

# Encrypt SKIV with public key
encrypted_skiv = public_key.encrypt(
    skiv.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Save encrypted SKIV
with open("encrypted_skiv.enc", "wb") as f:
    f.write(base64.b64encode(encrypted_skiv))
