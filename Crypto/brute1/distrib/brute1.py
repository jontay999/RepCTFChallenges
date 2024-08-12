from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from random import randbytes


def very_powerful_encrypter(plaintext):
    key = randbytes(3)
    # AES needs to work on blocks of 16 bytes
    padded_key = pad(key, 16)
    padded_plaintext = pad(plaintext, 16)
    cipher = AES.new(padded_key, mode=AES.MODE_ECB)
    return cipher.encrypt(padded_plaintext)

if __name__ == "__main__":
    flag = open('flag.txt', 'rb').read().strip()
    with open("encrypted.txt", "wb") as f:
        encrypted_text = very_powerful_encrypter(flag)
        f.write(encrypted_text)

