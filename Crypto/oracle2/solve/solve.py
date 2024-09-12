from pwn import *
from Crypto.Util.number import *
from libnum import n2s
from tqdm import trange

ip = "104.248.97.237"
# p = remote("localhost", 1003)
p = remote(ip, 1338)


e = 0x10001
p.recvuntil(b"n = ")
n = int(p.recvline().strip().decode('utf-8'), 16)
p.recvuntil(b"Here's the encrypted flag:")
c = int(p.recvline().strip().decode('utf-8'), 16)
print(f"n={n}")
print(f"c={c}")

k = n.bit_length()//8
B = 2 ** ( 8 * (k - 1))

print(f"k={k}")
def more_than_b(i):
    p.recvuntil(b"Enter message to sign in hex (e.g. 3a1f ):") 
    payload = hex(c*i % n)[2:].encode('utf-8')
    p.sendline(payload)
    p.recvuntil(b"Output:")
    output = int(p.recvline().strip().decode('utf-8'))
    return output > 8 * (k-1)

## STEP 1 
f1 = 2
count = 0
while not  more_than_b(pow(f1, e, n)):
    count += 1
    f1 *= 2
    
## STEP 2
# at this point:  B <= test_c <= 2B
# B / 2 <= test_c / 2 <= B

j = 1
count = 0
f2 = (n + B) // B  
f2 *= (f1 // 2)
max_steps = ceil_div(n, B)
for j in trange(1,max_steps+1):
    count += 1
    f2 += (f1 // 2)
    if not more_than_b(pow(f2, e, n)):
        break

# this makes the "wrapped" f2 * m < B
# because by definition f2 * m >= B
# implies that n <= f2 * m <= n + B

# this step terminates, taking at most [n/B] queries
# since n is exceeded when f2 = (2n / B) * (f1 / 2)

## STEP 3
mmin = ceil_div(n, f2)
mmax = (n + B) // f2
bb = 2 * B
tries = 0
while mmax - mmin > 0:
    tries += 1
    f_tmp = bb // (mmax - mmin) 
    boundary_point = (f_tmp * mmin) // n
    # (f3 * m) must span a single boundary point at (boundary_point + B)
    iN = boundary_point * n
    f3 = ceil_div(iN, mmin)
    if more_than_b(pow(f3,e, n)):
        mmin = ceil_div(iN + B, f3) 
    else:
        mmax = (iN + B) // f3

print(f"tries: {tries}")
print(n2s(mmin))
# REP{well_done_honestly_wasn't_expecting_anyone_to_get_this}