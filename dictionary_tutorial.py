#!/usr/bin/python

dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Name': 'Mahnaz', 'Age': 27}
dict3 = {'Name': 'Abid', 'Age': 27}

print "dict1: ", dict1
print "dict2: ", dict2
print "dict3: ", dict3

print "dict1.keys() : ", dict1.keys()
print "dict1.values() : ", dict1.values()
print "dict1.items() : %s" % dict1.items()

print "dict1['Name']: ", dict1['Name']
dict1['Name'] = "vel"
print "dict1['Name']: ", dict1['Name']

print "cmp (dict1, dict2) : %d" % cmp (dict1, dict2)
print "cmp (dict2, dict3) : %d" % cmp (dict2, dict3)
print "cmp (dict1, dict1) : %d" % cmp (dict1, dict1)

print "len (dict1) : %d" % len (dict1)
print "str (dict1) : %s" % str (dict1)
print "type (dict1) : %s" % type (dict1)

dict4 = dict1.copy()
print "dict4 = dict1.copy() : %s" % str(dict4)

print "dict1.get('Age') : %s" % dict1.get('Age')
print "dict1.get('Education', \"Never\") : %s" % dict1.get('Education', "Never")

print "dict1.has_key('Age') : %s" % dict1.has_key('Age')
print "dict1.has_key('Sex') : %s" % dict1.has_key('Sex')

print "dict1.setdefault('Age', None) : %s" % dict1.setdefault('Age', None)
print "dict1.setdefault('Sex', None) : %s" % dict1.setdefault('Sex', None)
dict2 = {'Sex': 'female' }
dict1.update(dict2)
print "dict2.update(dict3) : %s" % dict1

seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print "dict.fromkeys(seq) : %s" % str(dict)
dict = dict.fromkeys(seq, 10)
print "dict.fromkeys(seq, 10) : %s" % str(dict)

del dict['name'] 
print "del dict['name'] : %s" % dict
dict.clear()
print "dict.clear(): ", dict
del dict1
dict2 = {}
print "dict2 = {} & del dict1: ", dict1, dict2


