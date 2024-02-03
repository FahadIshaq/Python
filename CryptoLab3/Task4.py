from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, utils
from cryptography.exceptions import InvalidSignature
from base64 import b64encode
import os

def encrypt_file(input_file_path, output_file_path, key):
    iv = os.urandom(16)  
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(input_file_path, 'rb') as infile, open(output_file_path, 'wb') as outfile:
        outfile.write(iv)
        chunk = infile.read(1024)
        while chunk:
            ciphertext = encryptor.update(chunk)
            outfile.write(ciphertext)
            chunk = infile.read(1024)
        outfile.write(encryptor.finalize())

def load_private_key(key_file, password):
    with open(key_file, 'rb') as kf:
        return serialization.load_pem_private_key(kf.read(), password=password, backend=default_backend())

def hash_file(file_path):
    hasher = hashes.Hash(hashes.SHA256(), backend=default_backend())
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.finalize()

def sign_data(private_key, data):
    return private_key.sign(data, ec.ECDSA(utils.Prehashed(hashes.SHA256())))

def main():
    input_file_path = 'alice2.txt'  
    encrypted_file_path = 'encrypted_file.enc'
    secret_key = os.urandom(32)  

    encrypt_file(input_file_path, encrypted_file_path, secret_key)

    private_key = load_private_key('ec_private_key.pem', b'password')  

    digest = hash_file(encrypted_file_path)

    signature = sign_data(private_key, digest)
    encoded_signature = b64encode(signature).decode('utf-8')

    with open('file_signature.sig', 'w') as f:
        f.write(f"-----BEGIN SIGNATURE-----\n{encoded_signature}\n-----END SIGNATURE-----")

    print("File encrypted and signature generated.")

if __name__ == '__main__':
    main()
