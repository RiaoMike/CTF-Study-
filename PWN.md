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

> ELF header: the whole frame(structure) of the elf file

> Program header table: segment information

section => {Code, Data, Sections' names}

> Code: code segment

> Data: data segment

> Sections' names:  name of the section

header2/2 => {Section Header table}

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

## Basic ROP

### Exploit the exist System call

If the program has the stack overflow exploit and there is a system call such as 'system("/bin/sh")' in **.text** section.

We can just overflow the stack to cover the ret IP with where *system call* are.

### ShellCode(NX-disable)

Once start the **gdb**, use **vmmap** command to see the permission of memory, say **rwx**.

If the stack or .bss section have the rwx permission, we can write the shellcode to the memory, and then return to that address to execute it.

> Use **shellcraft** of pwntools to generate shellcode or you can write it by yourself.

### basic rop

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
