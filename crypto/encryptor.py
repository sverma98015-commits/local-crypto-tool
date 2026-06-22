import os
import base64

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7

from crypto.key_manager import derive_key


def encrypt_text(text, password):

    salt = os.urandom(16)
    iv = os.urandom(16)

    key = derive_key(password, salt)

    padder = PKCS7(128).padder()
    padded_data = padder.update(text.encode()) + padder.finalize()

    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv)
    )

    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(padded_data)
    ciphertext += encryptor.finalize()

    encrypted = salt + iv + ciphertext

    return base64.b64encode(encrypted).decode()
