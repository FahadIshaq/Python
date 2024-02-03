import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend


backend = default_backend()
block_size = 16  # AES block size is 16 bytes


def get_key_and_iv(password, iv_seed, salt):
    # Create two separate instances of the KDF
    kdf_key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=16, salt=salt,
                         iterations=100000, backend=backend)
    kdf_iv = PBKDF2HMAC(algorithm=hashes.SHA256(), length=16, salt=salt,
                        iterations=100000, backend=backend)

    key = kdf_key.derive(password)
    iv = kdf_iv.derive(iv_seed)
    return key, iv


def encrypt_file(filename, output_filename, password, iv_seed):
    salt = os.urandom(block_size)
    key, iv = get_key_and_iv(password, iv_seed, salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()

    with open(filename, 'rb') as f_in, open(output_filename, 'wb') as f_out:
        f_out.write(salt)  # Write the salt to the output file
        while True:
            chunk = f_in.read(1024) 
            if not chunk:
                break 

            chunk_padded = padder.update(chunk)
            f_out.write(encryptor.update(chunk_padded))

        f_out.write(encryptor.update(padder.finalize()))
        f_out.write(encryptor.finalize())  # Handle potential output from encryptor.finalize()


def decrypt_file(filename, output_filename, password, iv_seed):
    with open(filename, 'rb') as f:
        salt = f.read(block_size)  # Read the salt
    key, iv = get_key_and_iv(password, iv_seed, salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(128).unpadder()

    with open(filename, 'rb') as f_in, open(output_filename, 'wb') as f_out:
        f_in.read(block_size)  # Skip the salt
        while True:
            chunk = f_in.read(1024)
            if not chunk:
                break
            
            f_out.write(unpadder.update(decryptor.update(chunk)))

        f_out.write(unpadder.update(decryptor.finalize()))
        f_out.write(unpadder.finalize())  

def main():
    choice = input("Choose (E)ncrypt or (D)ecrypt: ").upper()

    if choice == "E":
        filename = input("Enter the name of the file to encrypt: ")
        output_filename = input("Enter the name for the output encrypted file: ")
        password = bytes(input("Enter the password for encryption key: "), 'utf-8')
        iv_seed = bytes(input("Enter the password for IV: "), 'utf-8')
        encrypt_file(filename, output_filename, password, iv_seed)

    elif choice == "D":
        filename = input("Enter the name of the file to decrypt: ")
        output_filename = input("Enter the name for the output decrypted file: ")
        password = bytes(input("Enter the password for decryption key: "), 'utf-8')
        iv_seed = bytes(input("Enter the password for IV: "), 'utf-8')
        decrypt_file(filename, output_filename, password, iv_seed)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
