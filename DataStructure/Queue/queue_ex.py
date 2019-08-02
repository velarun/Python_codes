class Queue:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)
		
	def display(self):
		for Item in self.items:
			print(Item)

q=Queue()
	
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
q.display()
q.dequeue()
q.display()