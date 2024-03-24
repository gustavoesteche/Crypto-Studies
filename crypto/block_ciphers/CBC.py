from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

class CBCMode:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext, iv, encryption_function=None):
        if encryption_function == None:
            backend = default_backend()
            cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=backend)
            encryptor = cipher.encryptor()

            ciphertext = b""
            prev_block = iv

            for i in range(0, len(plaintext), 16):
                block = plaintext[i:i + 16]

                if len(block) < 16:
                    block += b"\x00" * (16 - len(block))

                block_xor = bytes(a ^ b for a, b in zip(block, prev_block))
                encrypted_block = encryptor.update(block_xor)
                ciphertext += encrypted_block
                prev_block = encrypted_block

            return ciphertext
        else: 
            ciphertext = b""
            prev_block = iv

            for i in range(0, len(plaintext), 16):
                block = plaintext[i:i + 16]

                if len(block) < 16:
                    block += b"\x00" * (16 - len(block))
                
                block_xor = bytes(a ^ b for a, b in zip(block, prev_block))
                encrypted_block = encryption_function(block_xor)
                cyphertext += encrypted_block
                prev_block = encrypted_block
            
            return ciphertext

    def decrypt(self, ciphertext, iv, dencryption_function=None):
        if dencryption_function != None:
            backend = default_backend()
            cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=backend)
            decryptor = cipher.decryptor()

            plaintext = b""
            prev_block = iv

            for i in range(0, len(ciphertext), 16):
                block = ciphertext[i:i + 16]

                decrypted_block = decryptor.update(block)
                plaintext += bytes(a ^ b for a, b in zip(decrypted_block, prev_block))
                prev_block = block

            return plaintext
        else: 
            plaintext = b""
            prev_block = iv

            for i in range(0, len(ciphertext), 16):
                block = ciphertext[i:i + 16]

                decrypted_block = dencryption_function(block)
                plaintext += bytes(a ^ b for a, b in zip(decrypted_block, prev_block))
                prev_block = block

            return plaintext

# Example usage using AES for standart method of encryptying and decrypting 128 bits blocks 

key, iv = os.urandom(16), os.urandom(16)  
cbc = CBCMode(key)

plaintext = b"Secret message" * 10
ciphertext = cbc.encrypt(plaintext, iv)
decrypted_text = cbc.decrypt(ciphertext, iv)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text)