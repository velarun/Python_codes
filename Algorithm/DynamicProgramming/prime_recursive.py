rang = 100

def recprime(num):

	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				break
		else:
			print(num)
			
for i in range(1, rang+1):
	recprime(i)