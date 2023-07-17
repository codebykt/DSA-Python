import sys
sys.path.append('E:\DSA\Day-1')
import Stack_LinkedList 

s = Stack_LinkedList.Stack()
my_string = input("enter a string :  ")

#pushing each char to stack
for i in my_string:
    s.push(i)
rev_string = ""

while not s.is_empty():
    rev_string += s.pop()
# print(rev_string)

if my_string == rev_string:
    print("the string is pallindrome")
else:
    print("the string is not a pallindrome")