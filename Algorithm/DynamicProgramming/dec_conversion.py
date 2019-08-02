def baseConverter(decNumber,base):

	digits = "0123456789ABCDEF"
	newString = ""

	while decNumber > 0:
		rem = decNumber % base
		decNumber = decNumber // base
		newString = digits[rem] + newString

	return newString

print("Decimal to binary:", baseConverter(1001,2))
print("Decimal to hexadecimal:", baseConverter(1001,16))
print("Decimal to octal:", baseConverter(1001,8))

def octal_to_decimal(number):
    i = 1
    decimal = 0
    while (number != 0):
        reminder = number % 10
        number /= 10
        decimal += reminder * i
        i *= 8
    return decimal

print("Octal to decimal:", octal_to_decimal(144))
print("Octal to octal:", baseConverter(octal_to_decimal(144),2))
print("Octal to hexadecimal:", baseConverter(octal_to_decimal(144),16))

def binary_to_decimal(bin):
	
	bin=str(bin)
	n=len(bin)
	res=0
	for i in range(1,n+1):
		res = res + int(bin[i-1])*2**(n-i)
	
	return res

print("Binary to decimal:", binary_to_decimal(1101))
print("Binary to octal:", baseConverter(binary_to_decimal(1101),8))
print("Binary to hexadecimal:", baseConverter(binary_to_decimal(1101),16))

def hex_to_decimal(hex):
	
	n=len(hex)
	res=0
	b=0
	for i in range(0,n):
		if hex[i] == "A":
			b = 10
		elif hex[i] == "B":
			b = 11
		elif hex[i] == "C":
			b = 12
		elif hex[i] == "D":
			b = 13
		elif hex[i] == "E":
			b = 14
		elif hex[i] == "F":
			b = 15
		else:
			if hex[i].isalpha():
				break
			else:
				b = hex[i]
		
		res = res + int(b) * 16**((n-1)-i)
	return res
print("Hexadecimal to decimal:", hex_to_decimal("3E9"))
print("Hexadecimal to octal:", baseConverter(hex_to_decimal("3E9"),8))
print("Hexadecimal to binary:", baseConverter(hex_to_decimal("3E9"),2))
