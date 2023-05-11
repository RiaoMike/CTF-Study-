from random import randint
from time import time
from fastMod import q_mul, q_mod
from extended_gcd import extended_gcd
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

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# pollard_rho_Floyd
def pollard_rho(n):
    # if miller_rabin(n):
    #     return n, 1
    # 龟兔赛跑，起点相同
    x = y = 2
    test = set() # 防止c值重复
    while True:
        c = randint(1, n)
        while c in test:
            c = randint(1, n)
        test.add(c)
        f = lambda x: (x * x + c) % n
        x = f(x)
        y = f(f(y))
        while x != y:
            fact = gcd(abs(x - y), n)
            if fact > 1:
                return fact, n // fact
            x = f(x)
            y = f(f(y))


p, q = pollard_rho(n)
phi = (p - 1) * (q - 1)
_, a, _ = extended_gcd(b, phi)
while a < 0:
    a += phi

print(f'密钥为({p} {q} {a})')
end = time()
print(f'Used {end - start}s')

