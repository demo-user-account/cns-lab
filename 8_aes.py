from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

def pad(text):
    while len(text) % AES.block_size != 0:
        text += b'\x00'
    return text

def des_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext_bytes  = plaintext.encode('utf-8')
    padded_plaintext = pad(plaintext_bytes)
    ciphertext       = cipher.encrypt(padded_plaintext)
    return ciphertext

def des_decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    return padded_plaintext.rstrip(b'\x00').decode('utf-8')

key = get_random_bytes(16)
print("Key: ", key.hex())

plaintext = input("Enter the plaintext:")
ciphertext = des_encrypt(key, plaintext)
decrypted_text = des_decrypt(key, ciphertext)

print("Plaintext: ", plaintext)
print("Ciphertext: ", ciphertext.hex())
print("Decrypted text: ", decrypted_text)
