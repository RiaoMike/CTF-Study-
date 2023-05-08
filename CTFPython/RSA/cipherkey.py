import math
from extended_gcd import extended_gcd
from fastMod import fastMod
from time import time


n, b = map(int, input('请输入公钥: ').split())

start = time()

# 暴力破解
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        p = i
        q = n // i
        break
# 快速幂取余
# Fermat
for i in range(2, int(math.sqrt(n)) + 1):
    if fastMod(3, i-1, i) == 1:
        p = i
        q =


phi = (p - 1) * (q - 1)
_, a, _ = extended_gcd(b, phi)
while a < 0:
    a += phi

print(f'密钥为({p} {q} {a})')

end = time()
print(f'Used {end - start}s')
