# Find sum of all nodes of the given perfect binary tree

class Node:
    def __init__(self,data):
        self.lchild = None
        self.data = data
        self.rchild = None

def PerfectTreeSum(root):
    if root is None:
        return 0
    else:
        return root.data + PerfectTreeSum(root.lchild) + PerfectTreeSum(root.rchild)

root = Node(1)
root.lchild = Node(2)
root.rchild = Node(3)
root.lchild.lchild = Node(4)
root.lchild.rchild = Node(5)
root.rchild.lchild = Node(6)
root.rchild.rchild = Node(7)

result = PerfectTreeSum(root)
print("Total: ",result)
