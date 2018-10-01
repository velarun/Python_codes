import os
import random

fileopt = open('C:\\Python27\\name.txt')
content = fileopt.read()
fileopt.close()

cont = content.split("\n")
length = len(cont)-1
randj = random.randint(0,length)
print "Random Line from the file:", randj+1
grepped = cont[randj]
print "Unique Characters:"
if grepped != "":
	for i in grepped:
		out=grepped.count(i)
		if out <= 1:
			print i,
else:
	print "Empty line"




