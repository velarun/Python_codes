##Reverse string using 2 variables

a = "hello world!"
b = len(a) - 1
out = ""
while b >= 0:
	out = out + a[b]
	b = b - 1

print "Original String: ", a
print "Reversed String: ", out

print "Reverse String using slicing functionality: ", a[::-1]
print "String won't change in original variable: ", a