def getPrimes(n):

	for num in range(1,n + 1):
		if num > 1:
			for i in range(2,num):
			   if (num % i) == 0:
				   break
			else:
			   yield num

for x in getPrimes(20):
	print(x)
