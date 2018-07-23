def missingNumber(arr):
	n = len(arr)+1
	sum = 0
	expectedSum = n*(n+1)/2
	for i in range(len(arr)):
		sum += arr[i]

	return expectedSum - sum

print(missingNumber([3,2,5,1,6,10,4,9,8]))