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
        

    def insert_end(self,value):
        print("adding at end",value)
        newNode = Node(value)
        temp = self.head

        if self.head is None:
            self.head = newNode
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
        self.display()

    def insert_at(self,value,index):
        if index  < 0 or index > self.getlen():
            print("invalid index")
            return
        count = 0 

        if index == 0:
            self.insert_begin(value)
        else:
            temp = self.head
            while count != index - 1:
                count+=1
                temp = temp.next
            newNode = Node(value)
            newNode.next = temp.next
            temp.next = newNode
        print("Added new Node")
        self.display()

        

    def remove_begin(self):
        print("removing  from the begininng")
        temp = self.head
        print("removed val",temp.data)
        self.head = temp.next
        self.display()


    def remove_end(self):
        print("removing from end")
        temp = self.head
        if self.head is None:
            print("list empty")
        else:
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
        self.display()

    def remove_at(self,index):
        print("called remove at")
        if index <0 or index > self.getlen():
            print("invalid index")
            return
        count = 0
        temp = self.head
        while count != index - 1:
            temp = temp.next
            count+=1
        temp.next = temp.next.next
        # delNode = temp.next
        # temp.next = delNode.next
        self.display()

        
    def getlen(self):
        count = 0
        temp = self.head
        while temp is not None:
            count+=1
            temp = temp.next
        return count

    def display(self):
        temp = self.head
        print("printing linked list")
        if self.head is None:
            print("empty list")

        while temp is not None:
            print(temp.data)
            temp = temp.next

l=LinkedList()
l.insert_begin(10)
l.insert_begin(20)
l.insert_begin(30)
l.insert_end(9)
l.insert_end(8)
l.insert_end(7)




l.remove_begin()

l.remove_end()
print("length : ",l.getlen())


l.insert_at(99,4)
print("length : ",l.getlen())

l.remove_at(4)
print("length : ",l.getlen())



