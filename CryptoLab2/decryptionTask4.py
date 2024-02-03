from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

with open("keystore/recipients_keys/nigel_ku.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=b'password',  
        backend=default_backend()
    )

# Decrypt SKIV
with open("encrypted_skiv.enc", "rb") as f:
    encrypted_skiv = base64.b64decode(f.read())

decrypted_skiv = private_key.decrypt(
    encrypted_skiv,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Extract key and IV from decrypted SKIV
lines = decrypted_skiv.decode().split('\n')
key = base64.b64decode(lines[1])
iv = base64.b64decode(lines[4])

# Decrypt the file
with open("encrypted_file.enc", "rb") as f:
    ciphertext = f.read()

cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext) + decryptor.finalize()

# Save decrypted file
with open("decrypted_file.txt", "wb") as f:
    f.write(plaintext)
