from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from base64 import b64encode

data = bytearray(input("Enter your message: "), 'utf-8')
myhash = hashes.SHA256()
hasher = hashes.Hash(myhash, default_backend())
hasher.update(data)
digest = hasher.finalize()

password = 'password'
with open('ec_private_key.pem', 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=password.encode(),
        backend=default_backend()
    )

sig = private_key.sign(
    digest,
    ec.ECDSA(utils.Prehashed(myhash))
)

encoded_sig = b64encode(sig).decode('utf-8')
with open('message_signature.sig', 'w') as sig_file:
    sig_file.write(f"-----BEGIN SIGNATURE-----\n{encoded_sig}\n-----END SIGNATURE-----")

print("Signature generated and saved successfully.")
