# Example for Row Tranposition Cipher

# Encryption
def encrypt(plain_text, key):
    num_cols = len(str(key))
    
    # Pad the plain text with extra characters
    padding = num_cols - len(plain_text) % num_cols
    plain_text += padding * 'X'
    
    matrix = []
    
    # Create the matrix
    for i in range(0, len(plain_text), num_cols):
        matrix.append(list(plain_text[i:i+num_cols]))
            
    # Sort the matrix according to the key with row
    sorted_matrix = []
    
    for i in range(0, len(matrix)):
        sorted_matrix.append([])
        for j in range(0, len(matrix[i])):
            sorted_matrix[i].append(matrix[i][int(str(key)[j])-1])

        
    # create the cipher text
    cipher_text = ""
    for i in range(0, len(sorted_matrix)):
        for j in range(0, len(sorted_matrix[i])):
            cipher_text += sorted_matrix[i][j]
        cipher_text += " "
    return cipher_text

# Decryption
def decrypt(cipher_text, key):
    cipher_text = cipher_text.replace(" ", "")
    num_cols = len(str(key))
    matrix = []
    
    # Create the matrix
    for i in range(0, len(cipher_text), num_cols):
        matrix.append(list(cipher_text[i:i+num_cols]))
            
    # Sort the matrix according to the key with row
    sorted_matrix = []
    
    for i in range(0, len(matrix)):
        sorted_matrix.append(['' for _ in range(num_cols)])
        for j in range(0, len(matrix[i])):
            sorted_matrix[i][int(str(key)[j])-1] = matrix[i][j]

    # create the cipher text
    plain_text = ""
    for i in range(0, len(sorted_matrix)):
        for j in range(0, len(sorted_matrix[i])):
            plain_text += sorted_matrix[i][j]
            
    return plain_text
        
# Example
plain_text= "TheSimplestPossibletranspositions"
key = 41532
cipher_text = encrypt(plain_text, key)
print("Cipher Text: ", cipher_text)
plain_text = decrypt(cipher_text, key)
print("Plain Text: ", plain_text)
