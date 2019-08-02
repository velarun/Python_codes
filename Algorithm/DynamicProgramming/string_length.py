import re
def count_letter(string):
    count = 0
    for i in range(len(string)):
        if string[i].isalpha():
            count += 1
    return count
s = 'hello world!'
leng = 0
for val in s:
	leng = leng + 1
print("String Length without using builtin func: ", leng)
print("String Length using len(s): ", len(s))
print("Character counts: ", count_letter(s))
count = len(re.findall('[a-zA-Z]',s))
print("Character counts using regexp: ", count)
print("Character & special symbols counts using builtin func: ", len(s) - s.count(" "))

