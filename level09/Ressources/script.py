#! /usr/bin/env python3

hexadicwrongorder = [52, 102, 109, 107, 54, 109, 124, 112, 130, 61, 112, 127, 110, 130, 130, 131, 66, 68, 68, 131, 123, 117, 140, 127, 137, 10]

hexadic = [102, 52, 107, 109, 109, 54, 112, 124, 61, 130, 127, 112, 130, 110, 131, 130, 68, 66, 131, 68, 117, 123, 127, 140, 137]

flag = ""
decryptdir = []
i=0
while i < (len(hexadic)):
	decryptdir.append(hexadic[i] - i)
	i += 1
print (decryptdir)


for charflag in decryptdir:
	flag = flag + chr(charflag)

print (flag)



	




