# Print the nodes at odd levels of a tree

class Node:
    def __init__(self,data):
        self.lchild = None
        self.data = data
        self.rchild = None
    
def printoddnodes(root,isodd= 1):           # 1 or True
    if root is None:
        return
    if isodd %2 ==1:
        print(root.data)
    printoddnodes(root.lchild,isodd +1)
    printoddnodes(root.rchild,isodd +1)

root = Node(1)
root.lchild = Node(2)
root.rchild = Node(3)
root.lchild.lchild = Node(4)
root.lchild.rchild = Node(5)
printoddnodes(root)
