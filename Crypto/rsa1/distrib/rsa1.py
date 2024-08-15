from libnum import s2n
from sympy import nextprime
from Crypto.Util.number import getPrime

flag = b"REP{FAKE_FLAG}"
p = getPrime(1024)
q = nextprime(p)
print(p,q)
n = p * q 
e = 65537
m = s2n(flag)
ct = pow(m,e,n)

print(f"n={n}")
print(f"e={e}")
print(f"ct={ct}")
