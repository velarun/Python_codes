# Binary search tree traversal using recursion with complexity O(n^2) 
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    # Insert Node of BST
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the Tree
def PrintTree(root, ns, ch):
    if root == None:
        return 

    string2=ch + ":" + " " + str(root.data)
    print(string2.rjust(ns))
    
    PrintTree(root.left, ns+10, "L")
    PrintTree(root.right, ns+10, "R")
        
# Inorder traversal
# Left -> Root -> Right
def inorderTraversal(root):
    res = []
    if root:
        res = inorderTraversal(root.left)
        res.append(root.data)
        res = res + inorderTraversal(root.right)
    return res
        
# Preorder traversal
# Root -> Left ->Right        
def PreorderTraversal(root):
    res = []
    if root:
        res.append(root.data)
        res = res + PreorderTraversal(root.left)
        res = res + PreorderTraversal(root.right)
    return res
        
# Postorder traversal
# Left ->Right -> Root
def PostorderTraversal(root):
    res = []
    if root:
        res = PostorderTraversal(root.left)
        res = res + PostorderTraversal(root.right)
        res.append(root.data)
    return res 
        
# Function to  print level order traversal of tree 
def printLevelOrder(root): 
    h = height(root)
    out = []
    for i in range(1, h+1): 
        printGivenLevel(root, i, out)
    return out
    
# Print nodes at a given level 
def printGivenLevel(root , level, out): 
    if root is None: 
        return
    if level == 1: 
        out.append(root.data)
    elif level > 1 : 
        printGivenLevel(root.left , level-1, out) 
        printGivenLevel(root.right , level-1, out) 
  
""" Compute the height of a tree--the number of nodes 
    along the longest path from the root node down to 
    the farthest leaf node 
"""
def height(node): 
    if node is None: 
        return 0 
    else : 
        # Compute the height of each subtree  
        lheight = height(node.left) 
        rheight = height(node.right) 
  
        #Use the larger one 
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1
        
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print("Tree:")
PrintTree(root, 0, "M")

print("DFS Traversal:")
print("Inorder Traversal: ", inorderTraversal(root))
print("Preorder Traversal: ", PreorderTraversal(root))
print("Postorder Traversal: ", PostorderTraversal(root))

print("BFS Traversal:")
print("Level order traversal:", printLevelOrder(root))
