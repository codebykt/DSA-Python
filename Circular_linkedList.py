class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def insert_begin(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
        else:
            temp = self.head 
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head
            self.head = newNode
            

    


    def display(self):
        if self.is_empty():
            raise Exception("Empty List")
        else:
            temp = self.head
            while True:
                print(temp.data)
                if temp.next == self.head:
                    break   
                temp = temp.next

l = CircularLinkedList()
l.insert_begin(10)
l.insert_begin(20)
l.insert_begin(30)

l.display()
