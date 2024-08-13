

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from random import randbytes, seed
from string import printable
seed(b"hello")
class Oracle:
    def __init__(self, key, block_size):
        self.key = key
        self.block_size = block_size
		
    def encrypt(self, msg):
        iv = randbytes(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return (iv + cipher.encrypt(pad(msg, self.block_size))).hex()
    
    def decrypt(self,data):
        try:
            iv = data[:self.block_size]
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
			# sorry, it would be too easy if I just returned you the decryption wouldn't it
            _decrypted = unpad(cipher.decrypt(data[self.block_size:]), self.block_size)
            return "That was nice!"
        except Exception:
            return "That wasn't so nice..."

key = b'0123456789abcdef'
oracle = Oracle(key, 16)

cipher = "9ddd2f8c31d34c1cefc47f217f7ccc5aec8b5afbdca3f775a1fcf1b7d6bd920d9efd50beff231da73377dc0bbbbca7ab"
blocks = [cipher[i:i+32] for i in range(0,len(cipher),32)]
padding_good = "That was nice!"
padding_bad = "That wasn't so nice..."


alphabet = "0123456789abcdefghijklmnopqrstuvwxyzREP{}_"
def is_padding_wrong(payload):
    payload = bytes.fromhex(payload)
    return oracle.decrypt(payload) == padding_bad



def find_char(first_block, second_block, padding):
    # first_block is known, trying to find out contents of second_block
    # first_block is xored with output of second_block
    first_block = [int(first_block[i:i+2], 16) for i in range(0,len(first_block), 2)]
    
    modified_block = first_block[:]
    # our second_block has `padding` amount of padding bytes
    # we want to cause it to have `padding+1` amount of padding bytes
    # first_block[-padding-1:]  ^ second_block[-padding-1:]
    for i in range(padding):
        modified_block[-i-1] ^= ((padding+1) ^ (padding))

    flag_block = ""
    while padding < 16:
        for i in alphabet:
            testing_block = modified_block[:]
            testing_block[-padding-1] ^= ((ord(i)) ^ (padding+1))
            payload_block = [bytes([j]) for j in testing_block]
            payload_block = (b"".join(payload_block)).hex()

            if not is_padding_wrong(payload_block+second_block):
                flag_block = i + flag_block
                padding += 1

                modified_block = testing_block
                for i in range(padding):
                    modified_block[-i-1] ^= ((padding+1) ^ (padding))
                if padding > 16: return flag_block
                break

    print(flag_block)
    return flag_block

initial_padding = 4
final_flag = ""
for i in range(len(blocks)-2):
    final_flag += find_char(blocks[i], blocks[i+1], 0)

final_flag += find_char(blocks[-2], blocks[-1], 4)
print(final_flag)
