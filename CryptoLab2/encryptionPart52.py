from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from jax import default_backend

# Load Nigel's public key
with open("keystore/recipients_keys/nigel_ku.pem", "rb") as file:
    public_key = serialization.load_pem_public_key(file.read(), backend=default_backend())

# Encrypt alice2.skiv
with open("alice2.skiv", "rb") as file:
    skiv_data = file.read()

encrypted_skiv = public_key.encrypt(
    skiv_data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Save encrypted SKIV
with open("alice2_skiv.enc", "wb") as file:
    file.write(encrypted_skiv)
