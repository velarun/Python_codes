def fact(n):	
	f = 1
	while n>=2:
		f = f * n
		n = n - 1
	return f
x=4
print "Factorial: ", fact(x)
