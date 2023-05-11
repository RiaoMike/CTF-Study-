
# 快速乘积
def q_mul(a, b, n):
    result = 0
    while b:
        if b & 1:
            result = (result + a) % n
        a = (a + a) % n
        b //= 2
    return result

# 快速幂取模算法
def q_mod(a, b, n=1):
    result = 1
    while b:
        if b & 1:
            result = q_mul(result, a, n)
        a = q_mul(a, a, n)
        b //= 2
    return result


if __name__ == '__main__':
    print('pow(2, 9, 50)', q_mod(2, 9, 50))
    print('pow(2, 16, 30)', q_mod(2, 16, 30))
