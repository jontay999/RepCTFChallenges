import random 
from ecdsa import curves
from hashlib import sha256
from random import getrandbits
from libnum import s2n

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
        return int(r),int(s)
    
    def verify(self, msg, sig):
         hash = int(sha256(msg).hexdigest(),16)
         r,s = sig
         s_inv = pow(s, -1, self.n)
         u1, u2 = (hash * s_inv) % self.n, (r * s_inv) % self.n
         test_r = (u1 * self.g + u2 * self.q).x() % self.n 
         return test_r == r

def encrypt_flag(secret_key):
    random.seed(secret_key)
    flag = b"REP{FAKE_FLAG}"
    otp = random.randbytes(len(flag))
    encrypted = bytes([b1 ^ b2 for b1, b2 in zip(flag,otp)])
    return s2n(encrypted)


if __name__ == "__main__":
    secret_key = getrandbits(254)
    msg = b"Did you know that Bitcoin uses ECDSA? I wonder if I can break into any Bitcoin wallets..."
    half_length = len(msg)//2
    msg1, msg2 = msg[:half_length], msg[half_length:]
    ecdsa = Ecdsa(secret_key)
    sig1 = ecdsa.sign(msg1)
    assert ecdsa.verify(msg1, sig1)
    sig2 = ecdsa.sign(msg2)
    assert ecdsa.verify(msg2, sig2)
    enc = encrypt_flag(secret_key)
    print(f"sig1 = {sig1}")
    print(f"sig2 = {sig2}")
    print(f"enc = {enc}")

