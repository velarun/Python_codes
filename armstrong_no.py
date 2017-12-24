num = 154
digit = len(str(num))
f = num
sum = 0
while(f!=0):
	a = f % 10
	f = f / 10
	sum = sum + ( a ** digit)
	
if( sum == num):
	print('%d is a armstrong number' %num)
else:
	print('%d is not a armstrong number' %num)

