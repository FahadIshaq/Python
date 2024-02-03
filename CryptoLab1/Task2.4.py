from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

backend = default_backend()
key = os.urandom(16)  # Random key for AES

cipher_ecb = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)

# Data with repeated block
mydata = b'1234567812345678' * 2
print("Original data (ECB):", mydata)

# Encrypt
encryptor_ecb = cipher_ecb.encryptor()
ciphertext_ecb = encryptor_ecb.update(mydata) + encryptor_ecb.finalize()
print("Encrypted (ECB, hex):", ciphertext_ecb.hex())

# Decrypt
decryptor_ecb = cipher_ecb.decryptor()
plaintext_ecb = decryptor_ecb.update(ciphertext_ecb) + decryptor_ecb.finalize()
print("Decrypted (ECB, hex):", plaintext_ecb)
