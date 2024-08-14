from Crypto.Cipher import AES
from libnum import n2s, s2n
from Crypto.Util.number import *

p = 58636598104215507085237883834215987773680466086833471916366896017220753138463
q = 77384536993006032876494890832715201451205889667357418199030720265457126937137

flag = b"REP{well_done_honestly_wasn't_expecting_anyone_to_get_this}"
class Oracle:
    def __init__(self):
        self.e = 0x10001
        self.d = pow(self.e,-1, (p-1)*(q-1))
        self.n = p*q
        self.c = pow(s2n(flag), self.e, self.n)
        self.print_info()

    def print_info(self):
         print(f"d = {self.d}")
         print(f"n = {self.n}")
         print("Here's the encrypted flag: ", hex(self.c))
         
    # what can this even do?
    def query(self, query_c):
        return pow(query_c, self.d, self.n).bit_length()
    

while True:
    oracle = Oracle()
    try:
        enc_input = bytes.fromhex(input("Enter message to sign in hex (e.g. 3a1f ): "))
        assert(0 < enc_input < oracle.n), "walao"
        print("Output: ", oracle.query(enc_input))
    except:
        print("Bad input")
        exit(0)
