import math
from extended_gcd import extended_gcd
from time import time
from fastMod import q_mul, q_mod


n, b = map(int, input('请输入公钥: ').split())
start = time()


# miller_rabin


# pollard_rho


phi = (p - 1) * (q - 1)
_, a, _ = extended_gcd(b, phi)
while a < 0:
    a += phi

print(f'密钥为({p} {q} {a})')

end = time()
print(f'Used {end - start}s')

