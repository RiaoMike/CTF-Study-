# Tools

## 1. IDA

Static analyse

## 2. pwntools

Python lib. Download the pwntools.
```zsh
pip install pwn
```
If you download the pwntools, you will also get 3. and 4.

## 3. checksec

1. Canary: Stack protector
2. NX: no execuable in stack and heap
3. PIE: 
...

## 4. ROPgadget

Use to find the gadgets chains.

```zsh
pacman -S ROPgadget
```

### Example

- ROPgadget --binary /path/to/binary_file --only 'pop|ret' | grep eax
- ROPgadget --binary /path/to/binary_file --string '/bin/sh'

## 5. gdb(pwndbg)

Dynamic debug

> See the [gdb](./gdb)

## 6. one_gadget

## 7. main_arane_offset

---

# Binary Basic

## c_source_code to elf file

1. C code(p1.c p2.c) --(compiler: gcc -S)> Assembly(p1.s p2.s)
> note that we omit the include step

2. Assebly(p1.s p2.s) --(compiler: gcc -c)> Object(p1.o p2.o)
3. Object(p1.o p2.o) --(linker: gcc)> Executable(p)

## executable file

windows:PE
    1. .exe
    2. .dll(dynamic link library)
    3. .lib(static link library)

linux:**ELF**
    1. .out
    2. .so(dynamic link library)
    3. .a(static link library)

## ELF file structure

.elf => {header1/2, sections, header2/2}

header1/2 => {ELF header, Program header table}

header2/2 => {Section Header table}

### ELF header

> ELF header: the whole frame(structure) of the elf file

```bash
$ readelf -h elf_file
```

- Magic: 7f 'E' 'L' 'F' class data version pad
- *Class: 1 for 32, 2 for 64
- *Data: 1 for little endian, 2 for big endian
- Version: current_version
- OS/ABI
- ABI Version
- *Type: REL, EXEC, DYN, CORE...
- Machine: File can exec on which machine
- *Entry point address: virtual addr where system give the control to elf file.
- Start of program headers
- Start of section headers
- Flags
- Size of this header
- Size of program headers
- Number of program headers
- Size of section headers
- Number of section headers
- Section header string table index

### Program header table(*Execution view*)

> Program header table: segment information
>
> A segment contains one or more sections

```bash
$ readelf -l elf_file
```



### Section header table(*Linking view*)

```bash
$ readelf -S elf_file
```

section => {Code, Data, Sections' names}

> Code: code segment

> Data: data segment

> Sections' names:  name of the section


> Section Header table: section information 

![elffile.png](./img/elf_file.png)
More on [this](https://luomuxiaoxiao.com/?p=139)

## Program Load and Run

Linking View: on disk to show different function

Execution View: on memory to show different read-write Permission


### 1. objdump
display information of object file, such as a.out
```
objdump -s elf
```

### 2. cat /proc/pid/maps
objdump display the disk view, while this diaplay the memory view


---

# PWN

Writing before everything

Due to the Local environment are different from the remote side, we need to remember **Stack Alignment** all the time at local debugging. However, this is not demanded for remote environment sometimes.

## Basic ROP

### ret2text

If the program has the stack overflow exploit and there is a system call such as 'system("/bin/sh")' in **.text** section.

We can just overflow the stack to cover the ret Address with where *system call* are.

### ret2shellcode(NX-disable)

Once start the **gdb**, use **vmmap** command to see the permission of memory, say **rwx**.

If the stack or .bss section have the rwx permission, we can write the shellcode to the memory, and then return to that address to execute it.

> Use **shellcraft** of pwntools to generate shellcode or you can write it by yourself.

### ret2syscall

Use gadgets of elf file.

In 32bits elf, we need to modify the registers to specific value to call **sys_execve**

- EAX=0xb=11
- EBX=&('/bin/sh')
- ECX=EDX=0

> In 64bits, regs are *rdi, rsi, rdx, rcx, r8, r9* and then to stack

And then ret to address of **int 0x80** to call the interrupt. Just like execute the command **sys_execve('/bin/sh', 0, 0)**

A simple payload like this:
```
payload = flat(['A'*112, pop_eax_ret, 0xb, pop_edx_ecx_ebx_ret, 0, 0, binsh, int_0x80])
```

### ret2libc

First, we need to get the address of **system** function from *.plt* table. 

> There are three situations here, more details see [ctfwiki](https://ctf-wiki.org/pwn/linux/user-mode/stackoverflow/x86/basic-rop/#ret2libc)

---

1. [example1](PwnFile/ret2libc1)

And then, if we can find the "/bin/sh" string using *ROPgadget* tool. Just call the system function with parameter "/bin/sh" to get the shell.

> Note that we have a *0xdeadbeef* between address of system and binsh_addr.
>
> See this, when we **call** a function, we first place the parameter where function need and then push the return address of the function.
>
> Finally pragram jmp to the address of function to execute it. Distinguish the difference between *call* and *execute*.

Payload like this(32bits):

```python
payload = flat(['a' * 112, system_plt, 'b' * 4, binsh_addr])
```

2. [example2](PwnFile/ret2libc2)

This time, we can not find "/bin/sh" string in the program, but we can see the **gets** function in *.plt* table. 

If there are some place we have **w** permission(vmmap), some place like *.bss*. Make use of gets function to write "/bin/sh" to the .bss section.

And then, everything is as simple as the example1.

```python
payload = flat(['a'*112, gets_plt, pop_ebx_ret, buf2, system_plt, 0xdeadbeef, buf2])
```

A simple explanation:

- 'a'*112: padding for stack
- gets_ple: address of gets function to write "/bin/sh"
- pop_ebx_ret: return address for the **call** of gets in order to pop the buf address and execute the system function
- buf2: **parameter** for the gets, it's address where "/bin/sh" write to.
- system_plt: system function address
- 0xdeadbeef: return address of system, but it's useless, just padding.
- buf2: the parameter of system function to execve system('/bin/sh')

Another elaborate payload is

```python
payload = flat(['a'*112, gets_plt, system_plt, buf2, buf2])
```

This time, we can directly place the system_plt on the return address of the gets_plt, understand it by yourself.

3. [example3](PwnFile/ret2libc3)

If we want to utilize the system function, which program did't give us, how to get the address from libc.

We need two prerequisite knowledge:

1. system function belong to libc, and the offset between all function in libc.so dynamic link library is fixed.
2. Even if the program open the ASLR protector, it only randomize middle position of the address, while the lowest 12 bits remain unchange.

That means if we get a (func_name, func_address) of libc established, we can deduce out the version of libc as well as all offset between functions.

Due to the libc's **Lazy Binding**, we need to leak the address of funcntion which has already been executed. 

We usually use the address leak of **__libc_start_main** and a useful tool call **LibcSearcher**.

Exploitation Steps:

1. Leaked the __libc_start_main address
2. Get the version of libc
3. Get the address of *system* and *'/bin/sh'*
4. Execute the program again(return to main)
5. Trigger the stack overflow to execute system('/bin/sh')


