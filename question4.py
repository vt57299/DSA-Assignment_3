# Function to print all the leaves in a given binary tree

class Node:
    def __init__(self,data):
        self.lchild = None
        self.data = data
        self.rchild = None
    
def leaves(root):
    if root is None:
        return
    
    if root.lchild is None and root.rchild is None:
        print(root,end=" ")
    leaves(root.lchild)
    leaves(root.rchild)

root = Node(1)
root.lchild = Node(2)
root.rchild = Node(3)
root.rchild.lchild = Node(4)
root.rchild.rchild = Node(5)
root.rchild.rchild.lchild = Node(6)

print("leaves:",end=" ")
leaves(root)
