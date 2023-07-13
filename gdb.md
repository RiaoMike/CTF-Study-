# gdb调试

## Before beginning

Make good use of **help** , this will help a lot

>$:help all
>
>$:help command

To see the information of breakpoints,registers. It's useful.

>$:i b

>$:i r

## How to start

while you are in linux command line:

>$:gdb file_name

else if you have launch the gdb:

>$:file file_name

Then, you need to start debug using **start** command. It will stop at the first convenient location.

>$:start

You can alse use **run** command to start debugged program.
>
## Breakpoint

### Add
Just to use command **b**, which alias to **break**

Use **help b** to see more.

To add the breakpoint at a specific address:
>$:b *\*0x555555555516*

### Disable & Enable
Use the command **disable** and **enable** to control the usage of breakpoints.

>$:disable num

>$:enable num
>
The *num* here can be seen in info like *$:i b*

## Debug

### c
continue, fg, c

Continue program being debugged, after signal or *breakpoint*.

### si
stepi, si

Step one instruction exactly.

This means si will *step into a function*

### ni
nexti, ni

Step one instruction, but proceed through subroutine calls.

This means ni will *step over the function*

### finish
Execute until selected stack frame returns.

This command is often used to exit the function which you just using *si* to enter.

