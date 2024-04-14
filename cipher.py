# $ python -m pip install PyCryptodome

from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

import pyperclip
import sys

iv = b'\x62\x96\xF5\xE6\xBA\x84\x29\x16\xDD\xD7\xA4\x7F\x1F\x76\xE5\xA3'
pwd = b'tv5dytzw0rjwdmbe3odi5mqweryo7c4g'

BUFFER_SIZE = 512
OPERATION_SIZE = 3

class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data: str) -> str:
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(self.cipher.encrypt(pad(data.encode('utf-8'), AES.block_size)))

    def decrypt(self, data: str) -> str:
        raw = b64decode(data)
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(self.cipher.decrypt(raw), AES.block_size)

def check_op(op: str, value: str) -> int:
    if op ==  "enc":
        tmp = AESCipher(pwd).encrypt(value).decode('utf-8')
        pyperclip.copy(tmp)
        print('\n{}'.format(tmp))
        print("\nCopiado al portapapeles!\n")
        return 0
    elif op ==  "des":
         tmp = AESCipher(pwd).decrypt(value).decode('utf-8')
         pyperclip.copy(tmp)
         print('\n{}'.format(tmp))
         print("\nCopiado al portapapeles!\n")
         return 0
    else:
        print(f"{op} no soportada");
        return 1

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("\npython cipher.py (enc|des) valor\n")
        exit(1)
    
    if len(sys.argv[1]) > OPERATION_SIZE:
        print("\nop no soportada\n")
        exit(1)

    if len(sys.argv[2]) > BUFFER_SIZE:
        print("valor mayor a {}".format(BUFFER_SIZE))
        exit(1)

    op = sys.argv[1]
    value = sys.argv[2]

    result = check_op(op, value)
    exit(result)