#!/usr/bin/python

tup1, tup2 = (123, 'xyz'), (456, 'xyz', 'abc')
print "tup1[0]: ", tup1[0]
print "tup1[0:5]: ", tup1[0:5]
print "tup1 + tup2: ", tup1 + tup2
print "tup1 * 2: ", tup1 * 2
print "tup2[-2]: ", tup2[-2]
print "tup2[0:]: ", tup2[0:]
print "len(tup1) : ", len(tup1)
print "max(tup1) : ", max(tup1)
print "min(tup1) : ", min(tup1)
print "cmp(tup1, tup2): ", cmp(tup1, tup2)
print "cmp(tup2, tup1): ", cmp(tup2, tup1)
print "tup1.index('xyz'): ", tup1.index('xyz')
print "tup1.count('xyz') : ", tup1.count('xyz')
tup1 = ()
print "tup1(): ", tup1
del tup1
print "del tup1 : ", tup1


