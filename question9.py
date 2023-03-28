# Find maximum level sum in Binary Tree
from collections import deque

class node:
    def __init__(self,data):
        self.left = None
        self.key = data
        self.right = None

def max_lev_sum(root):
    if root is None:
        return 0
    result = root.key
    q = deque()
    q.append(root)
    while len(q)>0:
        count = len(q)
        sum = 0
        while count > 0:
            temp = q.popleft()
            sum += temp.key
            if temp.left !=None:
                q.append(temp.left)
            if temp.right != None:
                q.append(temp.right)
            count -=1
        result = max(sum,result)
    return result

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.right = node(8)
root.right.right.left = node(6)
root.right.right.right = node(7)
max_lev_sum(root)
