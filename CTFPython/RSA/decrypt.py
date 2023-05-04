# import sys
# import extended_gcd

# p, q, b = map(int, sys.argv[1:])
p, q, a = map(int, input('请输入密钥p, q, a: ').split())

n = p * q
phi = (p - 1) * (q - 1)

# _, a, _ = extended_gcd.extended_gcd(b, phi)
# Choose the smallest one great than zero
# !!! It's necessory
while a < 0:
    a += phi

cipher = input('请输入密文文件名(直接回车默认ciphertext.txt): ')
if cipher == '':
    cipher = 'ciphertext.txt'
s = open(cipher, 'r', encoding='utf-8').read()
if s.isnumeric():
    result = int(s) ** a % n
else:
    result = ''
    for ch in s:
        oldc = chr(ord(ch) ** a % n)
        result += oldc

# print('Plaintext is:', result)
print('明文为:', result)
