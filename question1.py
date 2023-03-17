# Implement Binary search

class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self,data):
        if self.key == None:
            self.key = data
            return      
        
        if self.key == data:              # checking for duplicate values
            return
        
        if self.key > data:
            if self.lchild is not None:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        if self.key < data:
            if self.rchild is not None:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self,data):
        if self.key == data:
            print("Node is Found!")
            return
        if data< self.key:
            if self.lchild is not None:
                self.lchild.search(data)
            else:
                print("Node is not present in the tree")
        if data> self.key:
            if self.rchild is not None:
                self.rchild.search(data)
            else: 
                print("Node is not present in the tree")
    
    def preorder(self):
        print(self.key)

root = BST(10)
list = [20,4,30,4,1,5,6]
for i in list:
    root.insert(i)
root.search()