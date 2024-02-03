from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    public_key = private_key.public_key()

    return private_key, public_key

def save_keys(private_key, public_key, password, private_key_filename, public_key_filename):
    pem_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
    )

    # Serialize the public key
    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open(private_key_filename, 'wb') as private_file:
        private_file.write(pem_private)

    with open(public_key_filename, 'wb') as public_file:
        public_file.write(pem_public)

def load_keys(private_key_filename, public_key_filename, password):
    with open(private_key_filename, 'rb') as private_file:
        private_key = serialization.load_pem_private_key(
            data=private_file.read(),
            password=password.encode(),
            backend=default_backend()
        )

    with open(public_key_filename, 'rb') as public_file:
        public_key = serialization.load_pem_public_key(
            data=public_file.read(),
            backend=default_backend()
        )

    return private_key, public_key

if __name__ == "__main__":
    password = "mypassword"  
    private_key_filename = "keystore/publickeys/Faisal_N_Alenezi_kr.pem"
    public_key_filename = "keystore/publickeys/Faisal_N_Alenezi_ku.pem"

    private_key, public_key = generate_keys()
    save_keys(private_key, public_key, password, private_key_filename, public_key_filename)

    loaded_private_key, loaded_public_key = load_keys(private_key_filename, public_key_filename, password)

    print("Keys generated, saved, and loaded successfully.")
