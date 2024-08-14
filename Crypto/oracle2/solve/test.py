from Crypto.Cipher import AES
from libnum import n2s, s2n
from Crypto.Util.number import *

p = 58636598104215507085237883834215987773680466086833471916366896017220753138463
q = 77384536993006032876494890832715201451205889667357418199030720265457126937137

flag = b"REP{well_done_honestly_wasn't_expecting_anyone_to_get_this}"
class Oracle:
    def __init__(self):
        self.e = 0x10001
        self.d = pow(self.e,-1, (p-1)*(q-1))
        self.n = p*q
        self.c = pow(s2n(flag), self.e, self.n)
        self.print_info()

    def print_info(self):
         print(f"d = {self.d}")
         print(f"n = {self.n}")
         print("Here's the encrypted flag: ", hex(self.c))
         
    # what can this even do?
    def query(self, query_c):
        return pow(query_c, self.d, self.n).bit_length()
        # return pow(query_c, self.d, self.n)

oracle = Oracle()

k = 63
B = 2 ** ( 8 * (k - 1))
def more_than_b(i):
    return oracle.query(oracle.c * i) > 8 * (k-1)

## STEP 1 
f1 = 2
count = 0
while not  more_than_b(pow(f1, oracle.e, oracle.n)):
    count += 1
    f1 *= 2
    
print("step 1 counts:", count)
print("step 2 started")
## STEP 2
# at this point:  B <= test_c <= 2B
# B / 2 <= test_c / 2 <= B
assert count == 25

j = 1
count = 0
f2 = (oracle.n + B) // B  
f2 *= (f1 // 2)
max_steps = ceil_div(oracle.n, B)
for j in range(1,max_steps+1):
    count += 1
    f2 += (f1 // 2)
    if not more_than_b(pow(f2, oracle.e, oracle.n)):
        break
    print(max_steps - j)
print("step 2 counts:", count)
print("step 3 started")



# this makes the "wrapped" f2 * m < B
# because by definition f2 * m >= B
# implies that n <= f2 * m <= n + B

# this step terminates, taking at most [n/B] queries
# since n is exceeded when f2 = (2n / B) * (f1 / 2)

## STEP 3
mmin = ceil_div(oracle.n, f2)
mmax = (oracle.n + B) // f2
bb = 2 * B
tries = 0
while mmax - mmin > 0:
    tries += 1
    f_tmp = bb // (mmax - mmin) 
    boundary_point = (f_tmp * mmin) // oracle.n
    # (f3 * m) must span a single boundary point at (boundary_point + B)
    iN = boundary_point * oracle.n
    f3 = ceil_div(iN, mmin)
    if more_than_b(pow(f3,oracle.e, oracle.n)):
        mmin = ceil_div(iN + B, f3) 
    else:
        mmax = (iN + B) // f3


print(f"tries: {tries}")
print(n2s(mmin))


# REP{well_done_honestly_wasn't_expecting_anyone_to_get_this}