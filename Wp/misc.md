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

# 3. 你竟然赶我走(buuoj.cn)
Download and unzip the file and there is jpg file in it.
Use the **hexedit** to check the hex and ascii code of jpg. Search the "flag" in ascii you will find the flag.(flag{stego_is_s0_bor1ing})

# 4. 大白(buuoj.cn)

The picture can not open at first which remind you that a error happened in CRC code. Use tweakpng or stegsolve to show the right CRC. Here I used the stegsolve because it gives the width and height at same time. 

> stegsolve and analyse dabai.png
![dabai.png](../img/dabai_analyse.png)

You can see the CRC right now is "6d7c7135" and calculated CRC is "8e14dfcf".
Then use hexedit to modify the CRC area and Ctr-X to save. After that the picture can be successfully open, but it is only half.

Double the height of png from 0100 to 0200 with hexedit, and calculate the new CRC with tweakpng(this time stegsolve can't work). Modify the CRC to new value(bffcc552) and then you can find the flag.(flag{He1l0_d4_ba1})**Notice the digits and characters**


# 5. 
