# 1. File type identification

## 1.1 file
a command in linux to show file type

## 1.2 winhex 
a commnd in windows to show file type through file header messgae

## 1.3 incompelete or wrong file header 
```bash
# file example.png
example.png: data
```

# 2. File separation

## 2.1 binwalk
analyse file: show hidden files that may exist
> binwalk filename

extract file
> binewalk -e filename

## 2.2 foremost

a tool similar to binwalk
> foremost filename -o output-dir

## 2.3 dd

the hardest one, could manual separation files
> dd if=source-file of=tar-file bs=block-size count=blocks-number skip=numbers-to-skip
> if:   input filename
> of:   output filename
> bs:   set the read and write block size
> count:    set the block numbers
> skip: skip the first $numbers blocks

always usage: binwalk analyse + dd manual separation

## 2.4 winhex
in windows
not recommand, usually use **010 editor** in windows

## 2.5 010 Editor
a powerful software in windows(not free)
> give you a txt file full of hex code, import it to 010editor and then save as a rar(or others, it's depends on the file header)

# 3. File merge






