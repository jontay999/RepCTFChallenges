from libnum import s2n
from sympy import nextprime
from Crypto.Util.number import getPrime

flag = b"REP{close_primes_are_bad_0c566079d50e4af68facf90b87c26676}"
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
