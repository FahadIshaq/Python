from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def load_private_key(private_key_filename, password):
    with open(private_key_filename, 'rb') as file:
        private_key = serialization.load_pem_private_key(
            data=file.read(),
            password=password.encode(),
            backend=default_backend()
        )
    return private_key

def load_recipient_public_key(public_key_filename):
    # Load the recipient's public key (Nigel's public key)
    with open(public_key_filename, 'rb') as file:
        recipient_public_key = serialization.load_pem_public_key(
            data=file.read(),
            backend=default_backend()
        )
    return recipient_public_key

def encrypt_message(recipient_public_key, message):
    # Encrypt the message with the recipient's public key
    ciphertext = recipient_public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

if __name__ == "__main__":
    private_key_filename = 'keystore/publickeys/Faisal_N_Alenezi_kr.pem'
    recipient_public_key_filename = 'keystore/recipients_keys/nigel_ku.pem'
    password = 'password'  

    your_private_key = load_private_key(private_key_filename, password)

    nigel_public_key = load_recipient_public_key(recipient_public_key_filename)

    message = b'Some secret message for Nigel'

    ciphertext = encrypt_message(nigel_public_key, message)

    # Print or save the ciphertext to share with Nigel
    print("Ciphertext:", ciphertext.hex())
