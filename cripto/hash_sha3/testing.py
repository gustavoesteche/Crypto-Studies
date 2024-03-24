from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

def sha3_hash(input_string):
    digest = hashes.Hash(hashes.SHA3_256(), backend=default_backend())
    digest.update(input_string.encode('utf-8'))
    hash_value = digest.finalize()
    return hash_value.hex()

input_string = "Oh my dear god, this is a message to be hashed, that should be much longer."
hashed_value = sha3_hash(input_string)
print(hashed_value, len(hashed_value)* 8) # 512 bits of output 
