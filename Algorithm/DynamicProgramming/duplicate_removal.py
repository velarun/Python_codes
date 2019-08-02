import collections

def removeduplicate1(alist):
	newli=[]
	for item in alist:
		if item not in newli:
			newli.append(item)
	return newli
	
def removeduplicate2(alist):
	return list(sorted(set(alist), key=alist.index))
	
def removeduplicate3(alist):
	return list(set(alist))

def removeduplicate4(lst):
    lst.sort()
    i = len(lst) - 1
    while i > 0:  
        if lst[i] == lst[i - 1]:
            lst.pop(i)
        i -= 1
    return lst
	
li=[88,120,155,88,120,155,12,24,35,24,24]
print("Remove duplicate using empty list: ", removeduplicate1(li))
print("Remove duplicate using set(): ", removeduplicate3(li))
print("Remove duplicate using set() with order: ", removeduplicate2(li))

s = [x for i, x in enumerate(li) if i == li.index(x)]
print("Remove duplicate using enumerate: ", s)

c = collections.Counter(li)
print("Remove duplicate using collections: ", c.keys())

print("Original list before using pop: ", li)
print("Remove duplicate using sort & pop: ", removeduplicate4(li))
print("Original list after using pop: ", li)