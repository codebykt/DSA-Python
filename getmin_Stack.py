class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.minval = data
class Stack:
    def __init__(self):
        self.top = None
    def push(self,value):
        newNode = Node(value)
        if self.top is None:
            self.top = newNode
        else:
            newNode.minval = min(self.top.minval,value)
            newNode.next = self.top
            self.top = newNode
        
    def getmin(self):
        if self.top is None:
            raise Exception("Stack Empty")
        else:
            return self.top.minval
        
    def top(self):
        if self.top is None:
            raise Exception("Stack Empty")
        return self.top.data

    def pop(self):
        if self.top is None:
            print("stack empty")
            return
        temp = self.top
        self.top = temp.next
        return temp.data

    def getlen(self):
        count = 0
        temp = self.top
        while temp is not None:
            count+=1
            temp = temp.next
        return count
    
    def is_empty(self):
        return self.top is None


    def display(self):
        print("printing stack")
        if self.top is None:
            print("Stack empty")
        else:
            temp = self.top
            while temp is not None:
                print(temp.data)
                temp = temp.next


s = Stack()
s.push(10)
s.push(50)
s.push(1)
s.push(12)

s.display()
print("min value : ",s.getmin())