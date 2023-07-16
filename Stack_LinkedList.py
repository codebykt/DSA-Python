class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self,value):
        print(f'pushed {value} to stack')
        if self.top is None:
            self.top = Node(value)
        else:
            newNode = Node(value)
            newNode.next = self.top
            self.top = newNode
        self.display()

    def pop(self):
        print("called pop")
        if self.top is None:
            print("stack empty")
            return
        temp = self.top
        print(f'popped {temp.data} from the stack')
        self.top = temp.next
        self.display()

    def getlen(self):
        count = 0
        temp = self.top
        while temp is not None:
            count+=1
            temp = temp.next
        return count


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
s.push(20)
s.push(30)

s.pop()

print("Stack length is: ",s.getlen())
