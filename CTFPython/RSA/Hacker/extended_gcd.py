
def extended_gcd(a, b):
    # assume that a <= b
    # later we'll ensure it
    if a == 0:
        return b, 0, 1
    else:
        # if a > b
        # a, b = b%a, a will exchange them
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


if __name__ == '__main__':
    b = int(input('input b:'))
    phi = int(input('input \\phi(n):'))
    gcd, x, y = extended_gcd(b, phi)
    if gcd != 1:
        raise SystemExit('gcd not equal to 1!!!')
    # The solution is equivalent under modulo n
    # Choose the smallest one greater than zero
    while x < 0:
        x += phi
    print('Encryption key a:', x)
