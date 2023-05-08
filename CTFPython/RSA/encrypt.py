import sys
from fastMod import fastMod
from time import time


n, b = map(int, input('请输入公钥n b: ').split())
s = input('请输入要加密的明文: ')
# get (b, n) from agrv
# n, b = map(int, sys.argv[1:])
start = time()

if s.isnumeric():
    result = fastMod(int(s), b, n)
    result = str(result)
else:
    result = ''
    for ch in s:
        newc = chr(fastMod(ord(ch), b, n))
        result += newc

# print('Ciphertext is:', result)
print('密文为:', result)
# print result to a file
filename = 'ciphertext.txt'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(result)

print(f'密文已保存至{filename}')

end = time()

print(f'Used {end - start}s')
