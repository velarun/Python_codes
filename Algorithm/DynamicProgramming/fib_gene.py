a = int(raw_input('Give amount: '))

def fib(n):
	a, b = 0, 1
	for _ in xrange(n):
		yield a
		#a, b = b, a + b
		c = a
		a = b
		b = c + b
		
print list(fib(a))

a = int(raw_input('Give amount: '))

def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

b = fib()

for i in range(a):
    print b.next(),