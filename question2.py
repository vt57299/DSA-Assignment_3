# Find height of a given binary tree

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
def maxheight(root):
    if root is None:
        return 0
                                       
                                       # Calling recursive functions for left and right nodes
    left_height = maxheight(root.left)
    right_height = maxheight(root.right)

    return 1+ max(left_height,right_height)    # Simply taking the max b/w left and right nodes with +1



root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.right = Node(4)
root.right.right = Node(5)
root.right.right.left = Node(6)
print('height of the tree is',maxheight(root))
