with open('crackme.txt', 'r') as f:
    lines = f.readlines()

hashed_info = {}
for line in lines:
    parts = line.strip().split(":")
    username, hash_info = parts[0], parts[1]
    salt = hash_info.split("$")[2]
    hashed_info[username] = {"salt": salt, "full_hash": hash_info}




