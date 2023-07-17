class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None


    def insert_begin(self,value):
        print("adding  ",value)
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.display()

    def display(self):
        temp = self.head
        print("printing linked list")
        if self.head is None:
            print("empty list")

        while temp is not None:
            print(temp.data)
            temp = temp.next

l = LinkedList()
l.insert_begin(40)
l.insert_begin(30)
l.insert_begin(20)
