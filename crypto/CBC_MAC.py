from AES_criptography import encrypt_aes, decrypt_aes
import os 
from cryptography.hazmat.primitives import padding


def cbc_mac(message:str, key, l):
    def xor_bytes(byte_string1, byte_string2):
        # Perform XOR operation byte by byte
        result = bytes([a ^ b for a, b in zip(byte_string1, byte_string2)])
        return result
    
    n = 256
    padder = padding.PKCS7(l * n).padder()
    padded_plaintext = padder.update(message) + padder.finalize()

    
    ola = [padded_plaintext[i:i+32] for i in range(0, len(padded_plaintext), 32)]
    t = b'0'
    for i in range(l):
        t = encrypt_aes(key,xor_bytes(t, ola[i]))
    
    return t 

message = b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
key = os.urandom(32)
print(cbc_mac(message, key, 2))