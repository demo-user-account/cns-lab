import random

def generate_keypair():
    # Step 1: Choose two large prime numbers, p and q
    p = 61
    q = 53

    # Step 2: Compute n = pq
    n = p * q

    # Step 3: Compute the totient (p-1)(q-1)
    totient = (p - 1) * (q - 1)

    # Step 4: Choose an integer e such that 1 < e < totient and gcd(e, totient) = 1
    while True:
        e = random.randrange(1, totient)
        if gcd(e, totient) == 1:
            break

    # Step 5: Compute d, the modular multiplicative inverse of e (mod totient)
    d = modinv(e, totient)

    # Public key is (e, n), private key is (d, n)
    return ((e, n), (d, n))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x

def encrypt(message, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

def decrypt(cipher, private_key):
    d, n = private_key
    message = ''.join([chr(pow(char, d, n)) for char in cipher])
    return message

# Example usage
public_key, private_key = generate_keypair()

print("Public key:", public_key)
print("Private key:", private_key)

message =  input("Enter a message to encrypt: ")
cipher_text = encrypt(message, public_key)
decrypted_message = decrypt(cipher_text, private_key)

print("Original message:", message)
print("Encrypted:", cipher_text)
print("Decrypted message:", decrypted_message)
