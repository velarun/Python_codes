def recfact(x):
    if x == 0:
        return 1
    return x * recfact(x - 1)

x=4
print "Recursive Factorial: ", recfact(x)
