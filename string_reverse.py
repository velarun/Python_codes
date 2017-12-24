a = "hello world!"
b = len(a) - 1
out = ""
while b >= 0:
	out = out + a[b]
	b = b - 1

print "Original String: ", a
print "Reversed String: ", out
