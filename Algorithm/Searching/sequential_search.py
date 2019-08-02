## Program to check value in a list in sequential manner
## Return True if found else False
def sequentialSearch(alist, item):
	pos = 0
	found = False

	while pos < len(alist) and not found:
		if alist[pos] == item:
			found = True
		else:
			pos = pos+1
	return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))

## Program to check value in a list in sequential manner
## Return Position if found else -1
def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
print(search(testlist, 13))
