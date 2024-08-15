from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from random import choice
from libnum import s2n

def generate_AES_key():
    hex_chars = "0123456789abcdef"
    four_random_chars = "".join(choice(hex_chars) for _ in range(5))
    key = pad(bytes(four_random_chars, encoding="utf-8"), 16)
    return key

cipher1 = AES.new(generate_AES_key(), mode = AES.MODE_ECB)
cipher2 = AES.new(generate_AES_key(), mode = AES.MODE_ECB)


known_plaintext = b"Brute-force is too easy..."
def encrypt_twice(plaintext):
    padded_plaintext = pad(plaintext, 16)
    encrypted_once = cipher1.encrypt(padded_plaintext)
    encrypted_twice = cipher2.encrypt(encrypted_once)
    return encrypted_twice

def format(encrypted_text):
    return str(s2n(encrypted_text))

if __name__ == "__main__":
    flag = open('flag.txt', 'rb').read().strip()
    encrypted_text = format(encrypt_twice(known_plaintext))
    encrypted_flag = format(encrypt_twice(flag))
    with open("encrypted.txt", "w") as f:
        f.write(encrypted_text +"\n")
        f.write(encrypted_flag)

"""
=?)u
+Cbj
"""