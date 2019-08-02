##Function assigned to variable

def first(msg):
	print(msg)
	
first("hello")
second=first
second("world")

##Function passed as argument to another function

def incr(x):
	print(x+1)
	
def decr(x):
	print(x-1)
	
def deco(func,x):
	func(x)
	
deco(incr,2)
deco(decr,2)

##Function return another function
def make_pretty(func):
	def inner():
		print("i got decorated")
		func()
	return inner
	
def ordinary():
	print("i am ordinary")
	
pretty=make_pretty(ordinary)
pretty()

##Function return another function with syntactic way to implement
def make_pretty(func):
	def inner():
		print("i got decorated")
		func()
	return inner
	
@make_pretty
def ordinary():
	print("i am ordinary")
	
ordinary()
	
##Function with chaining decorators
def star(func):
	def inner(*args,**kwargs):
		print("*" * 30)
		func(*args,**kwargs)
		print("*" * 30)
	return inner
	
def percent(func):
	def inner(*args,**kwargs):
		print("%" * 30)
		func(*args,**kwargs)
		print("%" * 30)
	return inner
	
@star
@percent
def printer(msg):
	print(msg)

printer("Hello")

	
##Class with decorators
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)


	
