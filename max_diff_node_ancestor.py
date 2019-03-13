# Python3 program to find maximum difference 
# between node and its ancestor 

_MIN = -2147483648
_MAX = 2147483648

# Helper function that allocates a new 
# node with the given data and None left 
# and right poers.								 
class newNode: 

	# Constructor to create a new node 
	def __init__(self, key): 
		self.key = key 
		self.left = None
		self.right = None

""" 
Recursive function to calculate maximum 
ancestor-node difference in binary tree. 
It updates value at 'res' to store the 
result. The returned value of this function 
is minimum value in subtree rooted with 't' """
def maxDiffUtil(t, res): 

	""" Returning Maximum value if node 
	is not there (one child case) """
	if (t == None): 
		return _MAX, res 

	""" If leaf node then just return 
		node's value """
	if (t.left == None and t.right == None): 
		return t.key, res 

	""" Recursively calling left and right 
	subtree for minimum value """
	a, res = maxDiffUtil(t.left, res) 
	b, res = maxDiffUtil(t.right, res) 
	val = min(a, b) 

	""" Updating res if (node value - minimum 
	value from subtree) is bigger than res """
	res = max(res, t.key - val) 
	
	""" Returning minimum value got so far """
	return min(val, t.key), res 

""" This function mainly calls maxDiffUtil() """
def maxDiff(root): 

	# Initialising result with minimum value 
	res = _MIN 
	x, res = maxDiffUtil(root, res) 
	return res 

""" Helper function to pr inorder 
traversal of binary tree """
def inorder(root): 

	if (root): 
	
		inorder(root.left) 
		prf("%d ", root.key) 
		inorder(root.right) 
	
# Driver Code 
if __name__ == '__main__': 
	
	""" 
	Let us create Binary Tree shown 
	in above example """
	root = newNode(8) 
	root.left = newNode(15) 

	root.left.left = newNode(1) 
	root.left.right = newNode(6) 
	root.left.right.left = newNode(4) 
	root.left.right.right = newNode(7) 

	root.right = newNode(10) 
	root.right.right = newNode(14) 
	root.right.right.left = newNode(13) 
	print("Maximum difference between a node and", "its ancestor is :", maxDiff(root)) 
