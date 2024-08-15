
from Crypto.Util.number import *

def get_flag():
	with open("flag.txt", "rb") as f:
		return bytes_to_long(f.read())

p = getPrime(256)
q = getPrime(256)
class Oracle:
    def __init__(self):
        # just standard RSA stuff
        self.e = 0x10001
        self.d = pow(self.e,-1, (p - 1) * (q - 1))
        self.n = p * q
        self.c = pow(get_flag(), self.e, self.n)
        self.print_info()

    def print_info(self):
         print(f"n = {hex(self.n)}")
         print(f"Here's the encrypted flag: {hex(self.c)}")
         
    # what can this even do?
    def query(self, query_c):
        return pow(query_c, self.d, self.n).bit_length()
    

if __name__ == "__main__":
    oracle = Oracle()
    while True:
        try:
            enc_input = int(input("Enter message to sign in hex (e.g. 3a1f ): "), 16)
            assert(0 < enc_input < oracle.n), "walao"
            print("Output: ", oracle.query(enc_input))
        except:
            print("Bad input")
            exit(0)
