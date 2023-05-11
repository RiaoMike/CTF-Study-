from random import randint
from extended_gcd import extended_gcd
from time import time
from fastMod import q_mul, q_mod
times = 2


n, b = map(int, input('请输入公钥: ').split())
start = time()


# miller_rabin
# 判断a是否为素数
def miller_rabin(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    tmp = n - 1
    p = 0
    while tmp % 2 == 0:
        p += 1
        tmp //= 2
    # 防止测试用例重复
    test = set()
    for i in range(times):
        num = randint(2, n - 2)
        while num in test:
            num = randint(2, n - 2)
        test.add(num)
        x = q_mod(num, n-1, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(p - 1):
            x = q_mul(x, x, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# pollard_rho
def pollard_rho(n):
    # if miller_rabin(n):
        # return n, 1
    fact = 1
    cycle = 2
    x = y = 2
    c = randint(1, n)
    while fact == 1:
        for i in range(cycle):
            if fact > 1:
                break
            x = (x * x + c) % n
            if x == y:
                c = randint(1, n)
                continue
            fact, _, _ = extended_gcd(abs(x - y), n)
        cycle *= 2
        y = x
    return fact, n // fact


p, q = pollard_rho(n)
phi = (p - 1) * (q - 1)
_, a, _ = extended_gcd(b, phi)
while a < 0:
    a += phi

print(f'密钥为({p} {q} {a})')
end = time()
print(f'Used {end - start}s')

