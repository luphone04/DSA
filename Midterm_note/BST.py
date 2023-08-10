import sys
sys.setrecursionlimit(10001) #set the maximum depth of the Python interpreter stack to n. This limit prevents any
#maximum depth of the Python interpreter stack
#used for handling function calls, and this limit prevents any potential stack overflow errors when using recursive functions


root = None
#will be used to store the root node of the binary search tree

class node: #represents a node in the BST
    def __init__(self, key, data): 
    #is called when a new node object is created. 
    #key parameter represents the value of the node (the key value), and the data parameter is for
    # additional data associated with the node 

        self.key = key
        self.data = data
        self.p = None # used to store the parent node of the current node
        self.left = None # left child node of the current node
        self.right = None # right child node of the current node

#ensures that the BST is printed in ascending order 
def Inorder_Tree_Walk(x): #print the nodes of the BST in ascending order (in-order traversal) 
    if x != None: # checks if the current node x is not None or empty
        Inorder_Tree_Walk(x.left) #less than root key value x
        #calls Inorder_Tree_Walk on the left child of the current node x to print the smaller nodes first
        print(x.key)
        #prints the key value of the current node x
        Inorder_Tree_Walk(x.right) #greater than root key value x
        #calls Inorder_Tree_Walk on the right child of the current node x to print the larger nodes last

# returns the node with the minimum key value in the subtree rooted at the node x
def Tree_Minimum(x):
    # Replace "pass" with your code
    while x.left != None: #checks if the left child of the current node x is not None, which means 
                          #there is a smaller value node
        x = x.left # updates the current node x to its left child, moving down the left subtree
    return x # returns the node with the minimum key

def Tree_Maximum(x):
    # Replace "pass" with your code
    global root
    while x.right != None:
        x = x.right
    return x



#returns the node with the smallest key value greater than the key value of the node x
# is useful when we need to find the next node in an in-order traversal of the BST
def Tree_Successor(x):
    # Replace "pass" with your code
    global root 
    if x.right != None: # checks if the right child of the current node x is not None, which means 
                        #there is a right subtree.
        return Tree_Minimum(x.right) # returns the node with the smallest key value in the right subtree of x,
    y = x.p #assigns the parent of the current node x to the variable y
    while y != None and x == y.right: #starts a loop that continues until the current node x is 
                                      #a right child of its parent y
        x = y
        y = y.p
    return y

def Tree_Predecessor(x):

    global root
    if x.left != None:
        return Tree_Maximum(x.left)
    y = x.p
    while y != None and x == y.left:
        x = y
        y = y.p
    return y


'''
Adding your own Tree_Predecessor(x) is recommended, but not required
'''

def Transplant(u, v):
    # This function is required for supporting Tree_Delete
    # Replace "pass" with your code
    global root
    if u.p == None:
        root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v != None:
        v.p = u.p
    

def Tree_Delete(z):
    # Replace "pass" with your code
    global root
    if z.left == None:
        Transplant(z, z.right)
    elif z.right == None:
        Transplant(z, z.left)
    else:
        y = Tree_Minimum(z.right)
        if y.p != z:
            Transplant(y, y.right)
            y.right = z.right
            y.right.p = y
        Transplant(z, y)
        y.left = z.left
        y.left.p = y


def Tree_Search(root, k):

    # Replace "pass" with your code
    if root == None or k == root.key:
        return root
    if k < root.key:
        return Tree_Search(root.left, k)
    else:
        return Tree_Search(root.right, k)
    


def Tree_Insert(z):  #inserts a new node z into the BST while maintaining its properties
    global root
    y = None #will be used to track the parent of the new node
    x = root #which will be used to traverse the tree.
    while x != None: #starts a loop that continues until we find the correct position to insert the new node.
        y = x #assigns the current node x to the variable y which tracks the potential parent of the new node.
        if z.key < x.key: #This line checks if the key value of the new node z is less than 
                          #the key value of the current node x
            x = x.left #assigns the left child of the current node x to the variable x for x is down to  the left subtree
        else:
            x = x.right #assigns the right child of the current node x to the variable x for x is down to  the right subtree
    z.p = y #sets the parent of the new node z to be the potential parent y
    if y == None: #checks if the potential parent y is None, which means the tree is empty
        root = z #sets the root of the tree to be the new node z
    elif z.key < y.key:  #checks if the key value of the new node z is less than the key value of 
                        #the potential parent y.
        y.left = z #sets the left child of y to be the new node z
    else: #if the key value of the new node z is greater than the key value of the potential parent y
        y.right = z  #sets the right child of y to be the new node z

    

# Function to print
def printCall ( node , indent , last ) :
    if node != None :
        print(indent, end=' ')
        if last :
            print ("R----",end= ' ')
            indent += "     "
        else :
            print("L----",end=' ')
            indent += "|    "

        print ( str ( node.key ) )
        printCall ( node.left , indent , False )
        printCall ( node.right , indent , True )

# Function to call print
def print_BSTree (root) :
    printCall( root , "" , True )



#insert element 
# Tree_Insert(node(56, None))
#  #None is for data value of the node . Here None represents that there is no data value for the node, 
#  # 56 is the key value of the node 
# Tree_Insert(node(26, None))
# Tree_Insert(node(200, None))
# Tree_Insert(node(18, None))
# print_BSTree(root)
# print()



Tree_Insert(node(56, None))
Tree_Insert(node(70, None))
Tree_Insert(node(30, None))
Tree_Insert(node(60, None))
Tree_Insert(node(65, None))
Tree_Insert(node(22, None))
Tree_Insert(node(11, None))
Tree_Insert(node(16, None))
Tree_Insert(node(40, None))
Tree_Insert(node(95, None))
Tree_Insert(node(63, None))
Tree_Insert(node(3, None))
Tree_Insert(node(67, None))
print_BSTree(root)
print()




#printing Maximum and Minimum
# print("Maxiumum :" ,Tree_Maximum(root).key)
#  #.key is for printing the key value of the node. We need .key because the function Tree_Maximum returns the node, not the key value
# print("Minumum : ", Tree_Minimum(root).key)
# print()



# finding successor and predecessor
print("Predecessor of 63 : ", Tree_Predecessor(Tree_Search(root, 63)).key)
print("Successor of 67 : ", Tree_Successor(Tree_Search(root, 67)).key)


print("After deleting 40 --------------------------")
print("---------------------------------------")
print("---------------------------------------")
print("---------------------------------------")
print("---------------------------------------")
print("---------------------------------------")

Tree_Delete(Tree_Search(root, 40))
print_BSTree(root)
print()







#delete element
# Tree_Delete(Tree_Search(root, 26))
# print_BSTree(root)
# print()
# Tree_Delete(Tree_Search(root, 56))
# print_BSTree(root)
# print()
# Tree_Delete(Tree_Search(root, 200))
# print_BSTree(root)
# print()
# Tree_Delete(Tree_Search(root, 18))
# print_BSTree(root)
# print()
# Tree_Delete(Tree_Search(root, 28))
# print_BSTree(root)
# print()
# #insert new element
# Tree_Insert(node(300, None))
# print_BSTree(root)
# print()
# #delete element
# Tree_Delete(Tree_Search(root, 300))
# print_BSTree(root)
# print()

