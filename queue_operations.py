class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        print(f'pushed {value} to the queue')
        newNode = Node(value)
        if self.front is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        self.display()

    def dequeue(self):
        if self.front is None:
            print("queue empty")
            return
        delNode = self.front
        print(f'popped {delNode.data} from queue')
        self.front = delNode.next

        if self.front is None:
            self.rear = None 
        self.display()

    def getlen(self):
        count = 0
        temp = self.front
        while temp is not None:
            count+=1
            temp = temp.next
        return count
    
    def display(self):
        print("printing queue")
        if self.front is None:
            print("queue empty")
        temp = self.front
        while temp is not None:
            print(temp.data)
            temp = temp.next


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print("length : ",q.getlen())
q.dequeue()
print("length : ",q.getlen())

