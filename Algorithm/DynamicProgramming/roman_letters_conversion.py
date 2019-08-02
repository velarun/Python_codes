num=3999

thou=[" ","M","MM","MMM"]
hund=[" ","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
tens=[" ","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
unit=[" ","I","II","III","IV","V","VI","VII","VIII","IX"]

if (num > 0) and (num < 4000):
	th=num/1000
	h=(num/100)%10
	t=(num/10)%10
	u=num%10
	
val=thou[th]+hund[h]+tens[t]+unit[u]
print(val.strip())
print(val.__class__)

