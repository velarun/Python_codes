# A complete working Python program to demonstrate all 
# insertion methods of linked list 
  
# Node class 
class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
  
        # 1 & 2: Allocate the Node & 
        #        Put in the data 
        new_node = Node(new_data) 
  
        # 3. Make next of new Node as head 
        new_node.next = self.head 
  
        # 4. Move the head to point to new Node 
        self.head = new_node 
  
  
    # This function is in LinkedList class. Inserts a 
    # new node after the given prev_node. This method is 
    # defined inside LinkedList class shown above */ 
    def insertAfter(self, prev_node, new_data): 
  
        # 1. check if the given prev_node exists 
        if prev_node is None: 
            print "The given previous node must inLinkedList."
            return
  
        #  2. create new node & 
        #      Put in the data 
        new_node = Node(new_data) 
  
        # 4. Make next of new Node as next of prev_node 
        new_node.next = prev_node.next
  
        # 5. make next of prev_node as new_node 
        prev_node.next = new_node 
  
  
    # This function is defined in Linked List class 
    # Appends a new node at the end.  This method is 
    # defined inside LinkedList class shown above */ 
    def append(self, new_data): 
  
        # 1. Create a new node 
        # 2. Put in the data 
        # 3. Set next as None 
        new_node = Node(new_data) 
  
        # 4. If the Linked List is empty, then make the 
        #    new node as head 
        if self.head is None: 
            self.head = new_node 
            return
  
        # 5. Else traverse till the last node 
        last = self.head 
        while (last.next): 
            last = last.next
  
        # 6. Change the next of last node 
        last.next =  new_node 
  
  
    # Utility function to print the linked list 
    def printList(self): 
        temp = self.head 
        while (temp): 
            print temp.data, 
            temp = temp.next
  
	# Function to reverse the linked list 
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 

	# Given a reference to the head of a list and a key, 
    # delete the first occurence of key in linked list 
    def deleteNode(self, key): 
          
        # Store head node 
        temp = self.head 
  
        # If head node itself holds the key to be deleted 
        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                return
  
        # Search for the key to be deleted, keep track of the 
        # previous node as we need to change 'prev.next' 
        while(temp is not None): 
            if temp.data == key: 
                break 
            prev = temp 
            temp = temp.next 
  
        # if key was not present in linked list 
        if(temp == None): 
            return 
  
        # Unlink the node from linked list 
        prev.next = temp.next 
  
        temp = None 		

	# Given a reference to the head of a list  
    # and a position, delete the node at a given position 
    def deleteNodePos(self, position): 
  
        # If linked list is empty 
        if self.head == None: 
            return 
  
        # Store head node 
        temp = self.head 
  
        # If head needs to be removed 
        if position == 0: 
            self.head = temp.next
            temp = None
            return 
  
        # Find previous node of the node to be deleted 
        for i in range(position -1 ): 
            temp = temp.next
            if temp is None: 
                break
  
        # If position is more than number of nodes 
        if temp is None: 
            return 
        if temp.next is None: 
            return 
  
        # Node temp.next is the node to be deleted 
        # store pointer to the next of node to be deleted 
        next = temp.next.next
  
        # Unlink the node from linked list 
        temp.next = None
  
        temp.next = next 
 
	# This function counts number of nodes in Linked List 
    # iteratively, given 'node' as starting node. 
    def getCount(self): 
        temp = self.head # Initialise temp 
        count = 0 # Initialise count 
  
        # Loop while end of linked list is not reached 
        while (temp): 
            count += 1
            temp = temp.next
        return count 
		
	# This function counts number of nodes in Linked List 
    # recursively, given 'node' as starting node. 
    def getCountRec(self, node): 
        if (not node): # Base case 
            return 0
        else: 
            return 1 + self.getCountRec(node.next) 
  
    # A wrapper over getCountRec() 
    def getCountRecursive(self): 
       return self.getCountRec(self.head) 

	   
# Start with the empty list 
llist = LinkedList() 

# Insert 6.  So linked list becomes 6->None 
llist.append(6) 

print 'Created linked list with head is:', 
llist.printList() 

# Insert 7 at the beginning. So linked list becomes 7->6->None 
llist.push(7)
 
# Insert 1 at the beginning. So linked list becomes 1->7->6->None 
llist.push(1); 

print '\nInserting a element at beginning of linked list is:', 
llist.printList()

# Insert 4 at the end. So linked list becomes 1->7->6->4->None 
llist.append(4) 

print '\nInserting a element at the end of linked list is:', 
llist.printList()

# Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
llist.insertAfter(llist.head.next, 8) 

print '\nInserting a element at after head of linked list is:', 
llist.printList() 

llist.reverse() 
print "\nReversed Linked List:", 
llist.printList()

llist.deleteNode(6)  
print "\nLinked List after Deletion of 1:",
llist.printList() 

llist.deleteNodePos(2) 
print "\nLinked List after Deletion at position 2:",
llist.printList()

print "\nCount of nodes is :", llist.getCount()

print "Count of nodes using recursive is :", llist.getCountRecursive()