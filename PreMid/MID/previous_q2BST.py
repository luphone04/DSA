import sys
sys.setrecursionlimit(10001)

R = [17,21,24,26,29,36]#list(map(int,input().split()))
t = 33#int(input())
k = 3 

class Node:
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data
        self.p = None
        self.left = None
        self.right = None 

    def __repr__(self):
        return str(self.key)


class BST:
    def __init__(self, root=None):
        self.root = root

    def inorderedWalk(self):
        result = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            result.append(node.key)
            inorder(node.right)
        inorder(self.root)
        return result

    def search(self, k):
        x = self.root
        while x is not None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right

        return x

    def minimum(self,node):
        min_node = node

        while min_node.left is not None:
            min_node = min_node.left
        return min_node

    def maximum(self, node):
        max_node = node

        while max_node.right is not None:
            max_node = max_node.right
        return max_node

    def successor(self, key):
        nodeX = self.search(key)
        if nodeX is None:
            return
        if nodeX.right is not None:
            return self.minimum(nodeX.right)

        y = nodeX.p

        while y is not None and nodeX == y.right:
            nodeX = y
            y = y.p
        return y

    def predecessor(self, key):
        nodeX = self.search(key)
        if nodeX is None:
            return

        if nodeX.left is not None:
            return self.maximum(nodeX.left)

        y = nodeX.p

        while y is not None and nodeX == y.left:
            nodeX = y
            y = y.p
        return y

    def insert(self, z):
        nodeZ = Node(z)
        y = None
        x = self.root

        while x is not None:
            y = x
            if nodeZ.key < x.key:
                x = x.left

            else:
                x = x.right

        nodeZ.p = y
        if y is None:
            self.root = nodeZ  # T is Empty Tree

        elif nodeZ.key < y.key:
            y.left = nodeZ

        else:
            y.right = nodeZ

    def transplant(self, u, v):  # Change connection from u node to v node
        if u.p is None:
            self.root = v  # u is root (Orphan Node)

        elif u == u.p.left:
            u.p.left = v  # if u on left side

        else:
            u.p.right = v  # if u on right side

        if v is not None:
            v.p = u.p  # In case of not delete ( v is a Node)

    def delete(self, z):
        nodeZ = self.search(z)
        if nodeZ.left is None:
            self.transplant(nodeZ, nodeZ.right)

        elif nodeZ.right is None:
            self.transplant(nodeZ, nodeZ.left)

        else:
            y = self.minimum(nodeZ.right)
            if y.p != nodeZ:
                self.transplant(y, y.right)
                y.right = nodeZ.right
                y.right.p = y

            self.transplant(nodeZ, y)
            y.left = nodeZ.left
            y.left.p = y

tree = BST()
for key in R:
    tree.insert(key)
tree.inorderedWalk()
tree.insert(t)
tree.inorderedWalk()
if tree.predecessor(t) is None:
    print("Invalid")
elif tree.successor(t) is None and t - tree.predecessor(t).key >= k:
    print("Done, bitch!")
    print(tree.inorderedWalk())
elif t- tree.predecessor(t).key >= k and tree.successor(t).key - t >= k:
    print("Done, bitch!")
    print(tree.inorderedWalk())   
else:
    print("Invalid bruh")