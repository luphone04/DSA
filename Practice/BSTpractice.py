import sys
sys.setrecursionlimit(10001)

root = None

class node:
    def __init__(self, key , data):
        self.key = key
        self.data = data
        self.p = None
        self.left  = None
        self.right = None

def InOrder_Tree_Walk(x):
    if x != None:
        InOrder_Tree_Walk(x.left)
        print(x.key)
        InOrder_Tree_Walk(x.right)