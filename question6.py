# Find sum of all left leaves in a given Binary Tree

class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    
def left_leaves_sum(root):
    if root is None:
        return 0
    
    stack = [(root,False)]
    left_sum = 0

    while stack:
        node, isleft = stack.pop()

        if not node.left and not node.right and isleft:
            left_sum += node.data
        if node.left:
            stack.append((node.left,True))
        if node.right:
            stack.append((node.right,False))
    return left_sum

root = Node(50)
root.left = Node(45)
root.left.left = Node(40)
root.left.right = Node(46)
root.right = Node(60)
root.right.right = Node(70)
root.right.right.left = Node(68)
root.right.left = Node(65)
print(left_leaves_sum(root))
