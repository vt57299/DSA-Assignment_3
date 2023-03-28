# Count subtress that sum up to a given value x in a binary tree
class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    
def subtree_count(root,x):
    count = 0
    def dfs(node):
        nonlocal count
        if not node:
            return 0
        
        left_sum = dfs(node.left)
        right_sum = dfs(node.right)

        if left_sum +right_sum + node.data==x:
            count +=1
        
        return left_sum + right_sum + node.data
    dfs(root)

    return count

root = Node(5)
root.left = Node(-10)
root.right = Node(3)
root.left.left = Node(9)
root.left.right = Node(8)
root.right.left = Node(-4)
root.right.right = Node(7)
print(subtree_count(root,7))
