from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.exceptions import InvalidSignature
from base64 import b64decode

with open('alice2.txt', 'rb') as file:
    data = file.read()

myhash = hashes.SHA256()
hasher = hashes.Hash(myhash, default_backend())
hasher.update(data)
digest = hasher.finalize()

with open('Faisal_N_Alenezi_kr.pem', 'rb') as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

with open('alice2_signature.sig', 'r') as sig_file:
    sig_data = sig_file.read()
    sig_data = sig_data.replace('-----BEGIN SIGNATURE-----\n', '').replace('\n-----END SIGNATURE-----', '')
    sig_data = b64decode(sig_data)

try:
    public_key.verify(sig_data, digest, ec.ECDSA(utils.Prehashed(myhash)))
    print("Signature is valid.")
except InvalidSignature:
    print("Invalid signature.")
