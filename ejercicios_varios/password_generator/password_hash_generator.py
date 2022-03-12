import os
import hashlib

password: str = "ClaveSecretaDeUsuario"

salt = os.urandom(16)
password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
print(f"Password hash: {password_hash}")