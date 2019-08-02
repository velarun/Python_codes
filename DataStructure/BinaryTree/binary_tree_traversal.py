# Binary Tree Traversal: O(n) complexity
class Node: 
	def __init__(self ,key): 
		self.data = key 
		self.left = None
		self.right = None

# Iterative Method to print the height of binary tree 
def printLevelOrder(root): 
	# Base Case 
	if root is None: 
		return
	
	# Create an empty queue for level order traversal using queue
	queue = [] 

	# Enqueue Root and initialize height 
	queue.append(root) 

	while(len(queue) > 0): 
		# Print front of queue and remove it from queue 
		print(queue[0].data), 
		node = queue.pop(0) 

		#Enqueue left child 
		if node.left is not None: 
			queue.append(node.left) 

		# Enqueue right child 
		if node.right is not None: 
			queue.append(node.right) 

# Iterative function for inorder tree traversal using stack
def inOrder(root): 
      
    # Set current to root of binary tree 
    current = root  
    s = [] # initialze stack 
    done = 0 
      
    while(not done): 
        # Reach the left most Node of the current Node 
        if current is not None: 
              
            # Place pointer to a tree node on the stack  
            # before traversing the node's left subtree 
            s.append(current) 
            current = current.left  
  
        # BackTrack from the empty subtree and visit the Node 
        # at the top of the stack; however, if the stack is  
        # empty you are done 
        else: 
            if(len(s) >0 ): 
                current = s.pop() 
                print(current.data), 
          
                # We have visited the node and its left  
                # subtree. Now, it's right subtree's turn 
                current = current.right  
  
            else: 
                done = 1

# Iterative function for preorder tree traversal using stack
def preOrder(root): 
      
    # Set current to root of binary tree 
    current = root  
    s = [] # initialze stack 
    done = 0 
      
    while(not done): 
        # Reach the left most Node of the current Node 
        if current is not None: 
            print(current.data),
            # Place pointer to a tree node on the stack  
            # before traversing the node's left subtree 
            s.append(current) 
            current = current.left  
  
        # BackTrack from the empty subtree and visit the Node 
        # at the top of the stack; however, if the stack is  
        # empty you are done 
        else: 
            if(len(s) >0): 
                current = s.pop() 
                # We have visited the node and its left  
                # subtree. Now, it's right subtree's turn 
                current = current.right  
            else: 
                done = 1

def peek(stack): 
    if len(stack) > 0: 
        return stack[-1] 
    return None
    
# A iterative function to do postorder traversal using stack
def postOrder(root): 
          
    # Check for empty tree 
    if root is None: 
        return 
  
    stack = [] 
      
    while(True): 
        while (root): 
             # Push root's right child and then root to stack 
             if root.right is not None: 
                stack.append(root.right) 
             stack.append(root) 
  
             # Set root as root's left child 
             root = root.left 
          
        # Pop an item from stack and set it as root 
        root = stack.pop() 
  
        # If the popped item has a right child and the 
        # right child is not processed yet, then make sure 
        # right child is processed before root 
        if (root.right is not None and 
            peek(stack) == root.right): 
            stack.pop() # Remove right child from stack  
            stack.append(root) # Push root back to stack 
            root = root.right # change root so that the  
                             # righ childis processed next 
  
        # Else print root's data and set root as None 
        else: 
            print(root.data),  
            root = None
  
        if (len(stack) <= 0): 
                break
                
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

print("Level Order Traversal:")
printLevelOrder(root) 
print("Inorder Traversal:")
inOrder(root)
print("Preorder Traversal:")
preOrder(root)
print("Postorder Traversal:")
postOrder(root)
