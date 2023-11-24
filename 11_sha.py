import hashlib

data = input("Enter: ")
sha = hashlib.sha512()
sha.update(data.encode('utf-8'))
hex = sha.hexdigest()

print("The hashed data using SHA512 is: ", hex)
