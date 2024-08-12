from tqdm import tqdm
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from itertools import product
encrypted_flag = open('./encrypted.txt', 'rb').read().strip()

def check_key(possible_key):
    key = pad(possible_key, 16)
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = cipher.decrypt(encrypted_flag)
    if decrypted_text.startswith(b'REP{'):
        print(unpad(decrypted_text,16))
        exit()

if __name__ == "__main__":
    for possible_key in tqdm(product(range(256), repeat=3)):
        check_key(bytes(possible_key))
    
