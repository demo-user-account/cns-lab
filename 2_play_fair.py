# Example to perform play fair cipher
# 1. Format the plain text
# 2. Generate a key matrix
# 3. Encrypt the plain text
# 4. Decrypt the cipher text

# Used to format the plain text
def format_plain_text(plain_text):
    plain_text = plain_text.replace(" ", "")
    plain_text = plain_text.upper()
    if len(plain_text) % 2 != 0:
        plain_text += "X"
    return plain_text

# Used to generate a key matrix
def generate_key(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = "".join(dict.fromkeys(key + alphabet))
    key = key.upper().replace("J", "I")
    matrix = []

    for i in range(5):
        matrix.append([])
        for j in range(5):
            matrix[i].append(key[i * 5 + j])
    
    return matrix

# Used to Find the position of a character in the key matrix
def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
            
# Used to encrypt the plain text
def encrypt(plain_text, key):
    plain_text = format_plain_text(plain_text)
    matrix = generate_key(key)
    cipher_text = ""
    
    for i in range(0, len(plain_text), 2):
        row1, col1 = find_position(matrix, plain_text[i])
        row2, col2 = find_position(matrix, plain_text[i + 1])
        
        if row1 == row2:
            cipher_text += matrix[row1][(col1 + 1) % 5]
            cipher_text += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += matrix[(row1 + 1) % 5][col1]
            cipher_text += matrix[(row2 + 1) % 5][col2]
        else:
            cipher_text += matrix[row1][col2]
            cipher_text += matrix[row2][col1]
            
    return cipher_text

# Used to decrypt the cipher text
def decrypt(cipher_text, key):
    matrix = generate_key(key)
    plain_text = ""
    
    for i in range(0, len(cipher_text), 2):
        row1, col1 = find_position(matrix, cipher_text[i])
        row2, col2 = find_position(matrix, cipher_text[i + 1])
        
        if row1 == row2:
            plain_text += matrix[row1][(col1 - 1) % 5]
            plain_text += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plain_text += matrix[(row1 - 1) % 5][col1]
            plain_text += matrix[(row2 - 1) % 5][col2]
        else:
            plain_text += matrix[row1][col2]
            plain_text += matrix[row2][col1]
            
    return plain_text

msg = input("Enter the plain text: ").replace(" ", "").upper()
key = input("Enter the key: ")
cipher_text = encrypt(msg, key)
print("Cipher Text: ", cipher_text)
plain_text = decrypt(cipher_text, key)
print("Plain Text: ", plain_text)
