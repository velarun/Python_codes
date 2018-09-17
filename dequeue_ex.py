class Deque:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addFront(self, item):
		self.items.append(item)

	def display(self):
		print self.items

	def addRear(self, item):
		self.items.insert(0,item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)
		

d=Deque()
print(d.isEmpty())
d.addRear(4)
d.addRear('dog')
d.display()
d.addFront('cat')
d.display()
d.addFront(True)
d.display()
print(d.size())
print(d.isEmpty())
d.addRear(8.4)
d.display()
print(d.removeRear())
d.display()
print(d.removeFront())
d.display()