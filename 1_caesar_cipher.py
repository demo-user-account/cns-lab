# Caesar Cipher Encryption
def encryption(plaintext, key):
    cipher_text = ""
    for i in range(len(plaintext)):
        cipher_text += chr((ord(plaintext[i]) + key - 65) % 26 + 65)
    return cipher_text

# Caesar Cipher Decryption
def decryption(cipher_text, key):
    plaintext = ""
    for i in range(len(cipher_text)):
        plaintext += chr((ord(cipher_text[i]) - key - 65) % 26 + 65)
    return plaintext

msg = input("Enter the message: ").upper().replace(" ", "")
key = int(input("Enter the key: "))
enc = encryption(msg, key)
dec = decryption(enc, key)
print("Encrypted message: ", enc)
print("Decrypted message: ", dec)
