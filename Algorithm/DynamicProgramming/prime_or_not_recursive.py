n1 = 3
l1 = n1 - 1
def recPrime(n, l):
	if n < 2:
		print 'Not prime.'
	else:
		if n % l == 0:
			print 'Not prime.'
		elif n % l != 0 and l != 2:
			recPrime(n, l - 1)
		elif n % l != 0 and l == 2:
			print 'Prime!'
recPrime(n1, l1)