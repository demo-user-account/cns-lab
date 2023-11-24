# Example Program for Hill Cipher
# install sympy using pip install sympy

from sympy import Matrix

# Find inverse of matrix
def matrix_modulo_inverse(matrix, modulus):
    return Matrix(matrix).inv_mod(modulus).tolist()

# Generate key matrix for encryption
# key is string like GYBNQKURP 3 x 3
def generate_key_matrix(key):
    matrix = []
    for i in range(3):
        matrix.append([])
        for j in range(3):
            matrix[i].append(ord(key[i * 3 + j]) % 65)
    return matrix

# Encrypt the plain text
def encrypt(plain_text, key):
    plain_text = plain_text.upper().replace(" ", "")
    key_matrix = generate_key_matrix(key)
    cipher_text = ""
    for i in range(0, len(plain_text), 3):
        vector = [[ord(plain_text[i]) % 65], [ord(plain_text[i + 1]) % 65], [ord(plain_text[i + 2]) % 65]]
        product = Matrix(key_matrix) * Matrix(vector)
        for j in range(3):
            cipher_text += chr(int(product[j] % 26 + 65))
    return cipher_text

# Decrypt the cipher text
def decrypt(cipher_text, key):
    key_matrix = generate_key_matrix(key)
    key_matrix = matrix_modulo_inverse(key_matrix, 26)
    plain_text = ""
    for i in range(0, len(cipher_text), 3):
        vector = [[ord(cipher_text[i]) % 65], [ord(cipher_text[i + 1]) % 65], [ord(cipher_text[i + 2]) % 65]]
        product = Matrix(key_matrix) * Matrix(vector)
        for j in range(3):
            plain_text += chr(int(product[j] % 26 + 65))
    return plain_text

# make plain text is multiple of 3
def format_plain_text(plain_text):
    plain_text = plain_text.upper().replace(" ", "")
    if len(plain_text) % 3 != 0:
        plain_text += "X" * (3 - len(plain_text) % 3)
    return plain_text

# Example
plain_text = input("Enter the plain text: ").upper().replace(" ", "")
plain_text = format_plain_text(plain_text)
key = input("Enter the key: ")
cipher_text = encrypt(plain_text, key)
print("Cipher Text: ", cipher_text)
plain_text = decrypt(cipher_text, key)
print("Plain Text: ", plain_text)
