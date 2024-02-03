from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

def main():
    backend = default_backend()

    user_input = input("Enter your message: ")
    data = bytearray(user_input, 'utf-8')

    myhash = hashes.SHA256()
    hasher = hashes.Hash(myhash, backend)

    hasher.update(data)

    digest = hasher.finalize()

    print("Original data:", user_input)
    print("Message Digest (SHA256):", digest.hex())

if __name__ == "__main__":
    main()
