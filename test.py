from Crypto.Cipher import Blowfish

# Full 56-byte key (paste the captured hex)
key = bytes.fromhex("a2df2319c1e5ec1e206a724b5709de77b728609eedbbfaaa939ab3d7bb4d7f77c135147cb76b4c2efa0249fad843a9d5cc38cae19cc41c90")

# Block conversion helpers
def le_to_be_block(block_8bytes):
    left  = int.from_bytes(block_8bytes[0:4], 'little')
    right = int.from_bytes(block_8bytes[4:8], 'little')
    return left.to_bytes(4, 'big') + right.to_bytes(4, 'big')

def be_to_le_block(block_8bytes):
    left  = int.from_bytes(block_8bytes[0:4], 'big')
    right = int.from_bytes(block_8bytes[4:8], 'big')
    return left.to_bytes(4, 'little') + right.to_bytes(4, 'little')

# Test first block
plaintext_mem = bytes.fromhex("78daeb589a5b9c9e")  # little-endian from memory
plaintext_be  = le_to_be_block(plaintext_mem)

cipher = Blowfish.new(key, Blowfish.MODE_ECB)
ciphertext_be = cipher.encrypt(plaintext_be)
ciphertext_mem = be_to_le_block(ciphertext_be)

# The expected little-endian ciphertext from your trace
expected = bytes.fromhex("a3b52a618b3a2d9c")

print("Computed:", ciphertext_mem.hex())
print("Expected:", expected.hex())
print("Match:", ciphertext_mem == expected)
