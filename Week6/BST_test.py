from BST import *

x = [56,26,200,18,28,190,213,12,24,27]

if __name__ == "__main__":
    Tree = BST()

    for key in x:
        Tree.Tree_Insert(node(key))

    Tree.print_BSTree()
# BST.Inorder_Tree_Walk()
# print()
# Tree.delete(26)
# Tree.inorderedWalk()
# print()
#testing max and min
# print(BST.Tree_Maximum())
# print(BST.Tree_Minimum())
# print()


