#!/usr/bin/python

str = "hello\tworld!";
print "Original String: ", str
print "str[:7]: ", str[:7]
print "str[2:]: ", str[2:]
print "str[4]: ", str[4]
print "str[3:8]: ", str[3:8]
print "Update String str[:6] + 'Python': ", str[:6] + 'python'
print "Multiply String str * 2: ", str * 2
print "Multiply 2nd character str[2] * 2: ", str[2] * 2
print "Raw string:", r"\n"
print "My name is %s, My weight is %d kg and My height is %.2f ft" % ('Arun', 24, 5.8)
print "str.capitalize(): ", str.capitalize()
print "str.center(40, ' ') : ", str.center(40, ' ')
sub = "l"
print "str.count(\"l\", 0, 40) : ", str.count(sub, 0, 40)
print "str.count(\"l\") : ", str.count(sub)
suffix = "world!"
print "str.endswith(suffix): ", str.endswith(suffix)
print "str.endswith(suffix, 2): ", str.endswith(suffix, 2)
print "str.endswith(suffix, 2, 40): ", str.endswith(suffix, 2, 40)
print "str.endswith(suffix, 2, 6): ", str.endswith(suffix, 2, 6)
print "str.startswith('hello'): ", str.startswith('hello')
print "str.startswith('hello', 0, 6): ", str.startswith('hello', 0, 6)
print "str.startswith('hello', 2, 4): ", str.startswith('hello', 2, 4)
var1 = str.encode('utf-32','strict')
print "str.encode('utf-32','strict'): " + var1
print "str.decode('utf-32','strict'): " + var1.decode('utf-32','strict')
print "str.expandtabs(): " + str.expandtabs();
print "str.expandtabs(16): " + str.expandtabs(16);
str1 = "l"
print "str.find(str1): ", str.find(str1)
print "str.find(str1, 1): ", str.find(str1, 1)
print "str.find(str1, 14): ", str.find(str1, 14)
print "str.rfind(str1): ", str.rfind(str1)
print "str.rfind(str1, 0, 10): ", str.rfind(str1, 0, 10)
print "str.rfind(str1, 10, 0): ", str.rfind(str1, 10, 0)
print "str.index(str1): ", str.index(str1)
print "str.index(str1, 1): ", str.index(str1, 1)
print "str.rindex(str1): ", str.rindex(str1)
print "str.isalpha(): ", str.isalpha()
print "str.isalnum(): ", str.isalnum()
print "str.isdigit(): ", str.isdigit()
print "str.islower(): ", str.islower()
print "str.isupper(): ", str.isupper()
str1 = u"2009"
print "str.isnumeric() & string as Unicode: ", (str1.isnumeric(),str1)
print "str1.isdecimal(): ", str1.isdecimal()
print "str.isspace(): ", str.isspace()
print "str.istitle() & start letter caps: ", str.istitle()
print "str.title(): ", str.title()
seq = "-"
print "seq.join( str ): ", seq.join(str)
print "len(str): ", len(str)
print "str.ljust(50, '0'): ", str.ljust(50, '0')
print "str.rjust(50, '0'): ", str.rjust(50, '0')
print "str.zfill(40): ", str.zfill(40)
print "str.lower(): ", str.lower()
print "str.upper(): ", str.upper()
print "max(str): " + max(str)
print "min(str): " + min(str)
print "str.replace('l', 'p'): ", str.replace("l", "p")
print "str.replace('l', 'p', 2): ", str.replace("l", "p", 2)
print "str.split( ): ", str.split()
print "str.split(' ', 14): ", str.split(' ', 14)
print "str.splitlines(3): ", str.splitlines(3)
print "str.swapcase(): ", str.swapcase()
str3 = "888this is string example....wow!!!888"
print "Strip string: ", str3
print "str3.lstrip('8') ", str3.lstrip('8')
print "str3.rstrip('8'): ", str3.rstrip('8')
print "str3.strip('8'): ", str3.strip('8')
str4 = "   this is string example....wow!!!   "
print "Strip string: ", str4
print "str4.lstrip(): ", str4.lstrip()
print "str.index(str1, 14): ", str.index(str1, 14)
