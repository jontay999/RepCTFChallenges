# Elliptic Curve equations work by
# y^2 = x^3 + a * x + b mod N

import random 
from ecdsa import curves
from hashlib import sha256
from Crypto.Cipher import AES
from random import randbytes

# https://strm.sh/studies/bitcoin-nonce-reuse-attack/

class Ecdsa:
    # Bitcoin's curve should be secure right?
    def __init__(self,secret_key, curve=curves.SECP256k1):
        self.g = curve.generator
        self.n = curve.generator.order()
        self.k = random.randrange(1, self.n)
        
        # secret keys
        self.d = secret_key
        self.q = self.d * self.g
        
    def sign(self, msg):
        hash = int(sha256(msg).hexdigest(),16)
        r = (self.k * self.g).x() % self.n
        s = (hash + r * self.d) * pow(self.k, -1, self.n) % self.n
        return r,s
    
    def verify(self, msg, sig):
         hash = int(sha256(msg).hexdigest(),16)
         r,s = sig
         s_inv = pow(s, -1, self.n)
         u1, u2 = (hash * s_inv) % self.n, (r * s_inv) % self.n
         test_r = (u1 * self.g + u2 * self.q).x() % self.n 
         return test_r == r

if __name__ == "__main__":
    secret_key = randbytes(254)
    msg1 = b"Did you know that Bitcoin uses ECDSA?"
    ecdsa = Ecdsa(secret_key)
    sig = ecdsa.sign(msg1)
    assert ecdsa.verify(msg1, sig)




# Generate a cryptographically secure random number k between 1 and n-1.
# Important: Do not reuse k after a signature is made with it because there are flaws that enable an attacker to derive private keys from signed messages if they know the shared nonce k used in them.

# Compute (x, y) = k*G, where G is the generator point of the secp256k1 curve, which is 04 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8 in uncompressed form, however the compressed form can also be used.
# Compute r = x mod n. If r=0, generate another random k and start over.
# Compute s = k-1(z + r*dA) mod n. If s=0, generate another random k and start over.