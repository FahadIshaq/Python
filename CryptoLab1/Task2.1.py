import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend


backend = default_backend()

salt = os.urandom(16)
print("Salt (hex):", salt.hex()) #printing random salt

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
iv_seed = input("Enter IV seed: ").encode()  # Encoding string to bytes


key = kdf_key.derive(passwd)
iv = kdf_iv.derive(iv_seed)

print("Key (hex):", key.hex())
print("IV (hex):", iv.hex())
