#pip install cryptography
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa

# generate private/public key pair
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign(msg, pr_key):
    return pr_key.sign(
        msg,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

def verify(msg, signature, pu_key):
    try:
        pu_key.verify(
            signature,
            msg,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False
    
# Example
msg = input("Enter a message: ").encode()
pr_key, pu_key = generate_keys()
signature = sign(msg, pr_key)
print("Signature:", signature)
rev = input("Enter a message: ").encode()
print("Verification:", verify(rev, signature, pu_key))
