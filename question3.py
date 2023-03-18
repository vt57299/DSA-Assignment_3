# Perform Pre-order, Post-order, In-order traversal

'''
Inorder traversal: In this traversal, the left subtree is visited first, then the current node is visited, and finally the right subtree is visited. In a binary search tree, the inorder traversal visits the nodes in ascending order.

Preorder traversal: In this traversal, the current node is visited first, then the left subtree is visited, and finally the right subtree is visited.

Postorder traversal: In this traversal, the left subtree is visited first, then the right subtree is visited, and finally the current node is visited.
'''

class Node:
    def __init__(self,data):
        self.lchild = None
        self.data = data
        self.rchild = None

def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.lchild)
        preorder(root.rchild)
def inorder(root):
    if root:
        inorder(root.lchild)
        print(root.data,end=" ")
        inorder(root.rchild)
def postorder(root):
    if root:
        postorder(root.lchild)
        postorder(root.rchild)
        print(root.data,end=" ")

root = Node(1)
root.lchild = Node(2)
root.rchild = Node(3)
root.rchild.lchild = Node(4)
root.rchild.rchild = Node(5)
root.rchild.rchild.lchild = Node(6)

print("Preorder traversal: ",end=" ")
preorder(root)
print()
print("Inorder traversal: ",end=" ")
inorder(root)
print()
print("Postorder Traversal: ",end=" ")
postorder(root)
