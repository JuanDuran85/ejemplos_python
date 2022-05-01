"""_summary_

    Using Crypto library

"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
import time

time.clock = time.time

try:
    code: str = "LinasParaRSA"
    key = RSA.generate(2048)
    encry_key = key.exportKey(passphrase=code, pkcs=8, protection="scryptAndAES128-CBC")
    with open("/my_key_private.bin", "wb") as file_key:
        file_key.write(encry_key)
    with open("/my_key_public.pem", "wb") as file_key:
        file_key.write(key.publickey().exportKey())
except Exception as e:
    print(e)