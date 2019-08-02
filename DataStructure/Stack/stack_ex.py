class Stack():
  
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []
    
	def push(self, item):
		return self.items.append(item)
  
	def pop(self):
		return self.items.pop()
  
	def getElements(self):
		return self.items
	
	def peek(self):
		return self.items[0]
		
	def size(self):
		return len(self.items)

stack = Stack()
print stack.isEmpty()
stack.push(1)
stack.push(2)
stack.push(3)
print stack.getElements()
stack.pop()
print stack.getElements()
print stack.peek()
print stack.size()