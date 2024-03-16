# TO Know

We need to be familiar to some frequently used function, like **scanf**, **puts**, **gets**, etc.

Here I don't talk about string format exploit, only some basic thing will be mentioned.

It's just remaining to look up while puzzled.

## scanf

## printf

### %s
Only stopped with '\x00'

只有当遇到换行符或缓冲区满或[程序退出时](./Wp/pwn.md/)才会打印出字符串

## puts

> int puts(const char* str);

将地址(str)指向字符串输出到标准输出,直到遇到终止符('\0').此终止符不会被输出,最后会
自动添加换行符('\n')

## gets

**!!!**

> char *gets(char *s);

从标准输入输入到s,直到遇到**换行符('\n')或EOF**,会丢弃换行符并自动添加'\0'  

note: gets函数遇到空白符不会停止,但很多其他函数遇到'\0'会停止

## fgets

> char *fgets(char *str, int n, FILE *stream);

从指定流stream读取一行，并存储到str所指向字符串。直到读取了(n - 1)个字符，或者读取到换行符或者到达文件末尾

## strcpy

字符串复制,遇到'\x00'停止

## strcat

字符串拼接,遇到'\x00'停止

## strlen

> size_t strlen(const char* s);

计算字符串长度,遇到空结束符('\0')结束,不计入空结束符
