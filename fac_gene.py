#!/usr/bin/env python

import sys
def generate_integers(N):
    for i in range(0,N):
        yield i

def factorial(x):

    y = 0
    z = 0
    gen = generate_integers(x)
    try:
        while y <= x:
            y = gen.next()
            if (z == 0) and (y == 0):
                z = 1
            else:
                z = z * y
    except StopIteration:
        pass

    print("%s! = %s" % (str(x - 1), z))

a = (sys.argv[1])

factorial(int(a) + 1)

def factorial(n):
	start = 1
	fact = 1
	while start <= n :
	   yield fact
	   start = start + 1
	   fact = fact * start
 
func = factorial(5)
for i in func:
   print i