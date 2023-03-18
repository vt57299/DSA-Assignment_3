# Implement Binary tree

class Node:
    def __init__(self,data):
        self.lchild = None
        self.key = data
        self.rchild = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return

        if self.key > data:
            if self.lchild is not None:
                self.lchild.insert(data)              # Recursively caliing the insert function on left node if there's data in the left node
            else:
                self.lchild = Node(data)              # If no data in lchild calling the class and storing self.key in the left node

        if self.key < data:
            if self.rchild is not None:
                self.rchild.insert(data)              # Recursively caliing the insert function on right node if there's data in the right node 
            else:
                self.rchild = Node(data)              # If no data in rchild calling the class and storing self.key in the right node

root = Node(10)
root.insert(20)
root.insert(30)
root.insert(5)
print(root.key)
print(root.rchild)
print(root.lchild)
