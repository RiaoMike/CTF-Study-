Linux environment
# 1. 金三胖(buuoj.cn)
Download the zip file and unzip it, you'll find a gif in it.

use **convert** command to transform it to png(target: split the gif frame by frame)
```bash
# convert aaa.gif flag.png
```
And then you'll find seventy or more flag-numbers.png, in which there are three photos with information about flag.(flag{he11ohongke})

# 2. 二维码(buuoj.cn)
There is a QR-png in the zip file

Use **binwalk** command you can see a zip file hidden in the png file. And the use binwalk to extract the file like below
> binwalk -e QR_code.png --run-as=root
> you may be can run it without "--run-as=root"

In the .extracted file you can see a empty 4numbers.txt and an encrypted zip file.You can easily guess that the password is a four-digit number.

Then use **fcrackzip** to crack the password, maybe others as you like
```bash
# fcrackzip -b -c '1' -l 4 -u 1D7.zip
```
With respect to the usage of fcrackzip, please man it yourself.(flag{vjpw_wnoei})

# 3. 

