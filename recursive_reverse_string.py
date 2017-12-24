def reverseString(string):    
	if len(string)==0:
		return string
	else:
		return string[-1:] + reverseString(string[:-1])

if __name__ == "__main__":
	string = "Hello world!"
	print reverseString(string)
	