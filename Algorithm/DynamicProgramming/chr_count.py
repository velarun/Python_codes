chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(){}[]|"
check_string = "[i am checking this string to see how many times each character appears 1 or 2 times %]"

for char in chars:
  count = check_string.count(char)
  if count >= 1:
    print "Character: ", char + ", Count: ", count

	
check_string = "[i am checking this string to see how many times each character appears 1 or 2 times %]"
li=[]
for char in check_string:
	count = check_string.count(char)
	if char not in li and char != " ":
		li.append(char)
		print "Character: ", char + ", Count: ", count
