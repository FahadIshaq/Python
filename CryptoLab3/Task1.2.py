from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

def get_hasher(algorithm_name):
    
    if algorithm_name == 'MD5':
        return hashes.Hash(hashes.MD5(), default_backend())
    elif algorithm_name == 'SHA1':
        return hashes.Hash(hashes.SHA1(), default_backend())
    elif algorithm_name == 'SHA256':
        return hashes.Hash(hashes.SHA256(), default_backend())
    elif algorithm_name == 'SHA384':
        return hashes.Hash(hashes.SHA384(), default_backend())
    elif algorithm_name == 'SHA512':
        return hashes.Hash(hashes.SHA512(), default_backend())
    else:
        raise ValueError("Unsupported algorithm")

def main():
    user_input = input("Enter your message: ")
    data = bytearray(user_input, 'utf-8')

    print("Choose the hashing algorithm: MD5, SHA1, SHA256, SHA384, SHA512")
    algorithm = input("Enter the algorithm name: ")

    hasher = get_hasher(algorithm)

    hasher.update(data)

    digest = hasher.finalize()

    print("Original data:", user_input)
    print(f"Message Digest ({algorithm}):", digest.hex())

if __name__ == "__main__":
    main()
