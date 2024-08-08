import hashlib

data = b"Hello, World!"  # byte string to hash
hash_object = hashlib.sha256()  # create a SHA-256 hash object
hash_object.update(data)  # update the hash object with data
digest = hash_object.digest()  # get the digest as bytes
hexdigest = hash_object.hexdigest()  # get the digest as a hexadecimal string

print("Digest (bytes):", digest)
print("Digest (hexadecimal):", hexdigest)
