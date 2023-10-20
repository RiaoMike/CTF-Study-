# Stack overflow

## 1. jarvisoj_level2

From: buuctf

click [here](../PwnFile/level2) to download.

We can easily find the **binsh_addr** and **system_call_address**.

It's an easy problem, but there's something new while using **gdb** to find the offset from buffer to *ebp*.

> When you try to set breakpoint, you may get the error like this:
>
> [Attaching after Thread 0xf7fc2400 (LWP 10853) vfork to child process 10856]
> [New inferior 2 (process 10856)]
> 
