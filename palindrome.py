def string_op(st):
	ch="abcdefghijklmnopqrstuvwxyz"
	for i in ch:
		if i in st:
			continue
		else:
			return "NO"
	return "YES"
	
N=int(input())
for i in range(N):
	st=str(input())
	get=string_op(st)
	print(get)
	
import itertools
numbers = [1, 2, 3, 7, 7, 9, 10]
result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) == 10]
print result