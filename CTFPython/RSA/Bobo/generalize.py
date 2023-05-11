import sys
import os
import extended_gcd

# p, q = map(int, sys.argv[1:])
p, q = map(int, (input('请输入素数p q: ').split()))

n = p * q
phi = (p - 1) * (q - 1)
for i in range(2, phi):
    x, y = i, phi
    while x != 0:
        x, y = y % x, x
    if y == 1:  # prime
        b = i
        break
_, a, _ = extended_gcd.extended_gcd(b, phi)
while a < 0:
    a += phi

if os.path.exists('./key.txt'):
    os.remove('./key.txt')

with open('./key.txt', 'a', encoding='utf-8') as f:
    f.write('p = ' + str(p) + '\n')
    f.write('q = ' + str(q) + '\n')
    f.write('n = ' + str(n) + '\n')
    f.write('phi = ' + str(phi) + '\n')
    f.write('b = ' + str(b) + '\n')
    f.write('a = ' + str(a))

print(f'公钥: ({n} {b})')
print(f'私钥: ({p} {q} {a})')
