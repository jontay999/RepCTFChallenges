from Crypto.Util.number import getPrime
from libnum import s2n

flag = b"REP{FAKE_FLAG}"
p = getPrime(100)
q = getPrime(100)
n = p*q
e = 0x10001
m = s2n(flag)
c = pow(m,e,n)

print(f"n={n}")
print(f"e={e}")
print(f"c={c}")