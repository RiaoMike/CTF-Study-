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

-------------------------------
Some useful file header
  1 JPEG (jpg)，file header：FFD8FF
  2 PNG (png)，file header：89504E47
  3 GIF (gif)，file header：47494638
  4 TIFF (tif)，file header：49492A00
  5 Windows Bitmap (bmp)，file header：424D
  6 CAD (dwg)，file header：41433130
  7 Adobe Photoshop (psd)，file header：38425053
  8 Rich Text Format (rtf)，file header：7B5C727466
  9 XML (xml)，file header：3C3F786D6C
 10 HTML (html)，file header：68746D6C3E
 11 Email [thorough only] (eml)，file header：44656C69766572792D646174653A
 12 Outlook Express (dbx)，file header：CFAD12FEC5FD746F
 13 Outlook (pst)，file header：2142444E
 14 MS Word/Excel (xls.or.doc)，file header：D0CF11E0
 15 MS Access (mdb)，file header：5374616E64617264204A
 16 WordPerfect (wpd)，file header：FF575043
 17 Postscript (eps.or.ps)，file header：252150532D41646F6265
 18 Adobe Acrobat (pdf)，file header：255044462D312E
 19 Quicken (qdf)，file header：AC9EBD8F
 20 Windows Password (pwl)，file header：E3828596
 21 ZIP Archive (zip)，file header：504B0304
 22 RAR Archive (rar)，file header：52617221
 23 Wave (wav)，file header：57415645
 24 AVI (avi)，file header：41564920
 25 Real Audio (ram)，file header：2E7261FD
 26 Real Media (rm)，file header：2E524D46
 27 MPEG (mpg)，file header：000001BA
 28 MPEG (mpg)，file header：000001B3
 29 Quicktime (mov)，file header：6D6F6F76
 30 Windows Media (asf)，file header：3026B2758E66CF11
 31 MIDI (mid)，file header：4D546864
------------------------------------

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
> give you a txt file full of hex code, import it to 010editor and then save as a rar(or others, it's depends on the file header)

## 2.6 hexedit
in linux you can use hexedit, it's powerful and free


# 3. File merge

## 3.1 linux
> cat file1 file2...filen > tarfile
> cat file* > tarfile

**after the file is merged, the file header may alse need to be added**
That is, although you have merged the file to target, for example a jpg, the picture still can't see. And $$file example.jpg$$ shows you it's a data, then you need to add the file header manully.

integrity check:    md5sum filename

## 3.2 windows
> copy /B file1+file2+file3 tarfile

integrity check:    certutil -hashfile filename md5    







