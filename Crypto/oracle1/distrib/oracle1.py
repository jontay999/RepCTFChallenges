

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from random import randbytes

BLOCK_SIZE = 16
BANNER = """
                                                     
,------. ,------.,------.  ,-----.,--------.,------. 
|  .--. '|  .---'|  .--. ''  .--./'--.  .--'|  .---' 
|  '--'.'|  `--, |  '--' ||  |       |  |   |  `--,  
|  |\  \ |  `---.|  | --' '  '--'\   |  |   |  |`    
`--' '--'`------'`--'      `-----'   `--'   `--'     
                                                                                                                                  
"""


def menu():
	MENU  = "\n====================  Menu ====================\n"
	MENU += "Select:\n"
	MENU += " 1. Free decryption service \n"
	MENU += " 2. Quit\n"
	MENU += "> "

	choice = input(MENU)
	return choice


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


def main():
	flag = b'REP{5hort_fl4g_t0_s4ve_t1m3}'
	block_size = 16
	key = randbytes(block_size)
	oracle = Oracle(key, block_size)
	print(BANNER)
	print("I wonder what an oracle is...")
	print("Here's the (unpadded) flag length: ", len(flag))
	print("Anyway here's the encrypted flag, crack it if you can: ", oracle.encrypt(flag), "\n")
	while True:
		try:
			choice = menu()
			if choice == "1":
				enc_input = bytes.fromhex(input("Encrypted text in hex (e.g. 3a1f): "))
				print("Here's your decryption: ", oracle.decrypt(enc_input))
				continue
			elif choice == "2":
				print("Thanks for visiting the oracle! 👋👋")
				break
			else:
				print("Only options '1' and '2' present")
		except :
			exit(0)

if __name__ == "__main__":
    main()