array = [1,'hello',3.14,3,43]
print(array[0])
print(array[-1])

print("array: ",array)

print("Adding at end 19")
array.append(19)
print("array: ",array)


print("Adding at end 20")
array.append(20)
print("array: ",array)

print("inserting at middle using insert(index,value)")
array.insert(0,'newly inserted value')
print("array: ",array)


#pop and del are same takes index

print("deleting using pop")
array.pop(0)
print("array: ",array)

print("deleting using del")
del array[1]
print("array: ",array)

print("deleting using remove")
array.remove(3.14)
print("array: ",array)

print('printing reverse')
print(array.reverse())
print('array: ',array)

print("printing one by one")
for i in array:
    print(i)
print("without using loops")
print(*array,sep='->')


