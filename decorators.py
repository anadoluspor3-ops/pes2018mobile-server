from functools import wraps
import gzip
import msgpack
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad
from binascii import unhexlify
import os
from flask import Response

KEY_HEX = "a2df2319c1e5ec1e206a724b5709de77b728609eedbbfaaa939ab3d7bb4d7f77c135147cb76b4c2efa0249fad843a9d5cc38cae19cc41c90"
KEY = unhexlify(KEY_HEX)

IV_LENGTH = 8

def encrypt_response(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data = f(*args, **kwargs)
        # 1. msgpack
        packed = msgpack.packb(data, use_bin_type=True)
        # 2. zlib
        compressed = gzip.compress(packed)
        # 3. encrypt
        iv = os.urandom(8)
        cipher = Blowfish.new(KEY, Blowfish.MODE_CBC, iv=iv)
        compressed_padded = pad(compressed, Blowfish.block_size)
        ciphertext = cipher.encrypt(compressed_padded)

        response = Response(iv + ciphertext, content_type="application/json")

        return response
    return decorated
