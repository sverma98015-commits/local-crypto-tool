import base64

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7

from crypto.key_manager import derive_key


def decrypt_text(encrypted_text, password):

    data = base64.b64decode(encrypted_text)

    salt = data[:16]
    iv = data[16:32]
    ciphertext = data[32:]

    key = derive_key(password, salt)

    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv)
    )

    decryptor = cipher.decryptor()

    padded_plaintext = decryptor.update(ciphertext)
    padded_plaintext += decryptor.finalize()

    unpadder = PKCS7(128).unpadder()

    plaintext = unpadder.update(padded_plaintext)
    plaintext += unpadder.finalize()

    return plaintext.decode()
