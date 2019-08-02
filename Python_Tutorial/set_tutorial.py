import sys	

print "Sets being mutable are unhashable:"
my_set = {1, 2, 3}
print "my_set = {1, 2, 3}: ", my_set

print "set of mixed datatypes:"
mixed = {1.0, "Hello", (1, 2, 3)}
print "mixed = {1.0, \"Hello\", (1, 2, 3)}: ", mixed

print "set removes duplicate:"
dup = {1,2,3,4,3,2}
print "dup = {1,2,3,4,3,2}: ", dup

print "set defines as {} or set():"
set_def = set([1,2,3,2])
print "set_def = set([1,2,3,2]): ", set_def

print "set cannot have mutable items:"
mutable = {1, 2, [3, 4]}
print "mutable = {1, 2, [3, 4]}: ", mutable

print "type(my_set): ", type(my_set)

my_set.add(4)
print "my_set.add(4): ", my_set

my_set.update([5,6], {7,6,8})
print "my_set.update([5,6], {7,6,8}): ", my_set

my_set.discard(4)
print "my_set.discard(4): ", my_set

my_set.remove(6)
print "my_set.remove(6): ", my_set

my_set.discard(0)
print "my_set.discard(0): ", my_set

new_set = my_set.copy()
print "new_set = my_set.copy(): ", new_set

my_set.remove(0)
print "my_set.remove(0): ", my_set

my_set.clear()
print "my_set.clear(): ", my_set
 
A = {1, 4, 3, 2, 5}
B = {4, 5, 6, 7, 8}
C = {}
D = {4, 5}
E = {1, 4, 3, 2, 5}
F = {6, 7, 8, 9, 0}
G = {1, 2, 6, 7, 0}

print "Set A: ", A
print "Set B: ", B
print "Set C: ", C
print "Set D: ", D
print "Set E: ", E
print "Set F: ", F
print "Set G: ", G

print "len(A): ", len(A)
print "any(A): ", any(A)
print "any(C): ", any(C)
print "all(A): ", all(A)
print "all(C): ", all(C)
print "max(A): ", max(A)
print "min(A): ", min(A)
print "sum(A): ", sum(A)
print "sorted(A): ", sorted(A)
print "A.issuperset(D): ", A.issuperset(D)
print "A.issuperset(D): ", A.issuperset(D)
print "A.issubset(B): ", A.issubset(B)
print "A.issubset(D): ", A.issubset(D)
print "my_set.pop(): ", my_set.pop()
print "G.pop(): ", G.pop()
print "G after pop() lowest number in a set: ", G

print "A set Union B set:"
print "A | B : ", A | B
print "A.union(B) : ", A.union(B)

print "A set Intersection B set:"
print "A & B : ", A & B
print "A.intersection(B) : ", A.intersection(B)
print "B.intersection(A) : ", B.intersection(A)

print "A set difference B set:"
print "A - B : ", A - B
print "A.difference(B) : ", A.difference(B)
print "B.difference(A) : ", B.difference(A)

print "A set Symmetric difference B set:"
print "A ^ B : ", A ^ B
print "A.symmetric_difference(B) : ", A.symmetric_difference(B)

print "Print letter from set removes duplicate:"
for letter in set("apple"):
	print(letter)
	
my_set = set("apple")
print "'a' in my_set : ", 'a' in my_set
print "'p' not in my_set : ", 'p' not in my_set

print "Sets have null intersection A.isdisjoint(F): ", A.isdisjoint(F)
print "Sets have intersection A.isdisjoint(B): ", A.isdisjoint(B)

A.difference_update(B)
print "A.difference_update(B): ", A

A.intersection_update(G)
print "A.intersection_update(G): ", A

A.symmetric_difference_update(B)
print "A.symmetric_difference_update(B): ", A

print "Frozensets being immutable are hashable:"

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([1, 4, 3, 2])

print "A.isdisjoint(B): ", A.isdisjoint(B)
print "A.difference(B): ", A.difference(B)
print "A.union(B): ", A.union(B)
print "A.intersection(B): ", A.intersection(B)
print "A.symmetric_difference(B): ", A.symmetric_difference(B)
print "A.issuperset(C): ", A.issuperset(C)
print "A.issubset(C): ", A.issubset(C)
print "len(A): ", len(A)

A.remove(6)
print "my_set.remove(6): ", A

