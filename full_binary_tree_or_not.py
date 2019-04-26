# Python3 program to find deepest 
# left leaf Binary search Tree 

# Helper function that allocates a 
# new node with the given data and 
# None left and right pairs.									 
class getNode: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

# function to check whether a binary 
# tree is a full binary tree or not 
def isFullBinaryTree( root) : 

	# if tree is empty 
	if (not root) : 
		return True

	# queue used for level oder 
	# traversal 
	q = [] 

	# append 'root' to 'q' 
	q.append(root) 

	# traverse all the nodes of the 
	# binary tree level by level 
	# until queue is empty 
	while (not len(q)): 
		
		# get the pointer to 'node' 
		# at front of queue 
		node = q[0] 
		q.pop(0) 

		# if it is a leaf node then continue 
		if (node.left == None and
			node.right == None): 
			continue

		# if either of the child is not None 
		# and the other one is None, then 
		# binary tree is not a full binary tee 
		if (node.left == None or
			node.right == None): 
			return False

		# append left and right childs 
		# of 'node' on to the queue 'q' 
		q.append(node.left) 
		q.append(node.right) 
	
	# binary tree is a full binary tee 
	return True

# Driver Code 
if __name__ == '__main__': 
	root = getNode(1) 
	root.left = getNode(2) 
	root.right = getNode(3) 
	root.left.left = getNode(4) 
	root.left.right = getNode(5) 

	if (isFullBinaryTree(root)) : 
		print("Yes" ) 
	else: 
		print("No") 
