from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def generate_and_save_keys(backend):
    private_key = ec.generate_private_key(ec.SECP384R1(), backend)
    public_key = private_key.public_key()

    password = 'password'

    pem_kr = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
    )

    pem_ku = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    private_key_file = 'ec_private_key.pem'
    with open(private_key_file, 'wb') as f:
        f.write(pem_kr)

    public_key_file = 'ec_public_key.pem'
    with open(public_key_file, 'wb') as f:
        f.write(pem_ku)

    return private_key_file, public_key_file, password

def reload_keys(private_key_file, public_key_file, password, backend):
    with open(private_key_file, 'rb') as file:
        private_key = serialization.load_pem_private_key(
            data=file.read(), password=password.encode(), backend=backend)

    with open(public_key_file, 'rb') as file:
        public_key = serialization.load_pem_public_key(
            data=file.read(), backend=backend)

    return private_key, public_key

def main():
    backend = default_backend()
    private_key_file, public_key_file, password = generate_and_save_keys(backend)
    private_key, public_key = reload_keys(private_key_file, public_key_file, password, backend)

    print("Keys generated, serialized, saved, and reloaded successfully.")

if __name__ == "__main__":
    main()
