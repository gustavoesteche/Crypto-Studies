from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# implementation using CBC mode for encrypting block ciphers 
# encrypt Xoring the previous encrypted text e(x_i ^ y_i-1)
# for the first one use IV vector ONCE (nonce)


def encrypt_aes(key, plaintext):
    # Generate a random IV (Initialization Vector)
    iv = os.urandom(16) # 128 bits of IV vector, for XORing

    # Pad the plaintext using PKCS7 padding, for completing the 128 bits multiple
    padder = padding.PKCS7(128).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    # Create an AES cipher object with CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())

    # Encrypt the plaintext
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    return iv + ciphertext

def decrypt_aes(key, ciphertext):
    # Extract the IV from the ciphertext
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]

    # Create an AES cipher object with CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())

    # Decrypt the ciphertext
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the plaintext
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext

'''
# Example usage:
key = os.urandom(32)  # 256-bit key     
plaintext = b"Hello, Humans"

print(key)

# Encrypt
ciphertext = encrypt_aes(key, plaintext)
print(f"Ciphertext: {ciphertext.hex()}")

# Decrypt
decrypted_text = decrypt_aes(key, ciphertext)
print(f"Decrypted Text: {decrypted_text.decode('utf-8')}")
'''