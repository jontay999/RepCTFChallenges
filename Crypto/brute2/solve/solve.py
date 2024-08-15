from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from string import printable
from itertools import product
from libnum import n2s,s2n
from tqdm import tqdm

known_plaintext = b"Brute-force is too easy..."

def get_info():
    enc_text, enc_flag = open('./encrypted.txt', 'r').read().strip().split("\n")
    return n2s(int(enc_text)), n2s(int(enc_flag))

def find_keys(encrypted_text):
    encryption_to_key = {}
    hex_chars = "0123456789abcdef"
    all_keys = list(product(hex_chars, repeat=5))
    plaintext = pad(b"Brute-force is too easy...",16)
    for possible_key in tqdm(all_keys):
        key2 = pad(bytes("".join(possible_key), encoding="utf-8"),16)
        cipher = AES.new(key2, mode=AES.MODE_ECB)
        enc = cipher.encrypt(plaintext)
        encryption_to_key[enc] = key2

    for possible_key in tqdm(all_keys):
        key1 = pad(bytes("".join(possible_key), encoding="utf-8"),16)
        cipher = AES.new(key1, mode=AES.MODE_ECB)
        decrypted = cipher.decrypt(encrypted_text)
        if decrypted in encryption_to_key:
            key2 = encryption_to_key[decrypted]
            return key1, key2

    assert False,  "Unable to find keys"

if __name__ == "__main__":
    enc_text, enc_flag = get_info()
    key1, key2 = find_keys(enc_text)
    cipher1 = AES.new(key1, mode=AES.MODE_ECB)
    cipher2 = AES.new(key2, mode=AES.MODE_ECB)
    decrypt_once = cipher1.decrypt(enc_flag)
    flag = cipher2.decrypt(decrypt_once)
    print("Found flag:",  unpad(flag,16))

