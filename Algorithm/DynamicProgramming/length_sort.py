xs = ['dddd','a','bb','ccc']
print(sorted(xs, key=len))

def lensort(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1,n):
            if len(a[i]) > len(a[j]):
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a
print lensort(["hello","bye","good"])

def sorts(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1,n):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a
print sorts([5,3,4])