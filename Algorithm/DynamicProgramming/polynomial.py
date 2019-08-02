import math

lst=[]
print("Enter the coefficients of the form ax^3+bx^2+cx+d:")
num=int(input("Range of polynomial:"))
for i in range(0,num):
	a=int(input("Enter Coefficients:"))
	lst.append(a)
	
x=int(input("Enter the value of x:"))
sum=0

j=num-1
for i in range(0,num):
	if j>0:
		sum=sum+(lst[i]*math.pow(x,j))
	else:
		sum=sum+lst[i]
	j=j-1
	
print(sum)