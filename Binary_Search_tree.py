class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BinarySearchTree:
    #tree
    def __init__(self):
        self.root = None
    def insert_node(self,data):
        newNode = Node(data)
        if self.root is  None:
            self.root = newNode
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = newNode
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = newNode
                        break
                    else:
                        current = current.right
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data,end = "->")
        self.inorder(node.right)
    
    def postOrder(self,node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data, end = "->")

    def preOrder(self,node):
        if node is None:
            return
        print(node.data, end = "->")
        self.preOrder(node.left)
        self.preOrder(node.right)

bst = BinarySearchTree()

bst.insert_node(10)
bst.insert_node(5)
bst.insert_node(78)
bst.insert_node(5)
bst.insert_node(65)
bst.insert_node(72)
bst.insert_node(35)

bst.inorder(bst.root)
print()
bst.preOrder(bst.root)
print()
bst.postOrder(bst.root)


