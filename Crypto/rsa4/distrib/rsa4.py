from libnum import s2n 
from Crypto.Util.number import getPrime

p = getPrime(512)
q = getPrime(512)
e=65537
n = p*q

# good luck!
leak1 = pow(2022*p+2021*q,1919,n)
leak2 = pow(2021*p+2022*q,9191,n)

flag = b"REP{FAKE_FLAG}"
flag = b"REP{groebner_basis_can_solve_weird_polynomial_equations}"
m = s2n(flag)
c = pow(m,e,n)

print(f"leak1={leak1}")
print(f"leak2={leak2}")
print(f"n={n}")
print(f"e={e}")
print(f"c={c}")
