class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parrent = None
    def addChild(self,child):
        self.children.append(child)
        self.parrent = self

    def display(self,node):
        if node is not None:
            print(node.data)
            if len(node.children) > 0:
                print(f"children of {node.data} are:")
                children = node.children
                # print(child.data for child in children)
                for child in children:
                    node.display(child)

root = TreeNode("electronics")

tv = TreeNode("tv")
ac = TreeNode("ac")
phone = TreeNode("phone")

root.addChild(tv)
root.addChild(ac)
root.addChild(phone)

mi = TreeNode("mi")
lg = TreeNode("lg")
vu = TreeNode("vu")

tv.addChild(mi)
tv.addChild(lg)
tv.addChild(vu)

voltas = TreeNode("voltas")
hitachi = TreeNode("hitachi")
panasonic = TreeNode("panasonic")

ac.addChild(voltas)
ac.addChild(hitachi)
ac.addChild(panasonic)

poco = TreeNode("poco")
apple = TreeNode("apple")
samsung = TreeNode("samsung")

phone.addChild(poco)
phone.addChild(apple)
phone.addChild(samsung)



root.display(root)
