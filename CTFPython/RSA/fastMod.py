
# 快速幂取模算法
def fastMod(a, b, c=1):
    if b == 0:
        return 1
    elif b == 1:
        return a % c

    tmp = fastMod(a, b // 2, c)
    if b % 2 == 0:
        return tmp * tmp % c
    else:
        return tmp * tmp * a % c


if __name__ == '__main__':
    print('pow(2, 9, 50)', fastMod(2, 9, 50))
    print('pow(2, 16, 30)', fastMod(2, 16, 30))
