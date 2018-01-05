hexdec = "AB"
dec = int(hexdec, 16)
print(hexdec,"in Decimal =",dec,"\n")
print(hexdec,"in Octal =",oct(dec),"\n")
print(hexdec,"in Binary =",bin(dec)[2:],"\n")

octal = "144"
dec = int(octal, 8)
print(octal,"in Decimal =",dec,"\n")
print(octal,"in Hexadecimal =",hex(dec),"\n")
print(octal,"in Binary =",bin(dec)[2:],"\n")

dec = 100
print("The decimal value of",dec,"is:")
print(bin(dec)[2:],"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")

bin = '010110'
print("The binary value of",bin,"is:")
print(int(bin, 2),"in decimal.")
print(hex(int(bin, 2)),"in hexadecimal.")
print(oct(int(bin, 2)),"in octal.")

number = 42
print("Hexadecimal: %X" % number)
print("Octal: %o" % number)
