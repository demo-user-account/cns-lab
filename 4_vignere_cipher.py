# Example for Vigènere Cipher

# used to get the shift list for the key
def get_shift_list(key):
    shift_list = []
    for i in range(len(key)):
        shift_list.append(ord(key[i]) % 65)
    return shift_list

# used to encrypt the plain text
def encrypt(plain_text, key):
    cipher_text = ""
    shift_list = get_shift_list(key)
    for i in range(len(plain_text)):
        cipher_text += chr((ord(plain_text[i]) + shift_list[i % len(shift_list)]) % 26 + 65)
    return cipher_text

# used to decrypt the cipher text
def decrypt(cipher_text, key):
    plain_text = ""
    shift_list = get_shift_list(key)
    for i in range(len(cipher_text)):
        plain_text += chr((ord(cipher_text[i]) - shift_list[i % len(shift_list)]) % 26 + 65)
    return plain_text

# Example
plain_text = input("Enter the plain text: ").upper().replace(" ", "")
key = input("Enter the key: ")
cipher_text = encrypt(plain_text, key)
print("Cipher Text: ", cipher_text)
plain_text = decrypt(cipher_text, key)
print("Plain Text: ", plain_text)
