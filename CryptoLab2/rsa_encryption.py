from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def generate_keys(private_key_filename, public_key_filename, password):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    pem_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
    )

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

def encrypt_decrypt_data(private_key, public_key, data):
    ciphertext = public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return plaintext

if __name__ == "__main__":
    private_key_filename = "keystore/publickeys/Faisal_N_Alenezi_kr.pem"
    public_key_filename = "keystore/publickeys/Faisal_N_Alenezi_ku.pem"
    password = "password"  

    generate_keys(private_key_filename, public_key_filename, password)

    private_key, public_key = load_keys(private_key_filename, public_key_filename, password)

    original_data = b'some test data'

    decrypted_data = encrypt_decrypt_data(private_key, public_key, original_data)

    if decrypted_data == original_data:
        print("Encryption and decryption successful. Plaintext matches the original data.")
    else:
        print("Encryption and decryption failed. Plaintext does not match the original data.")
