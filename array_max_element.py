arr = [5,524,52,15,35,4578,24,2,365,2,8,9,98,64,25,46,1,5,6]
max_element = max(arr)
print(max_element) 

element_max = 0
for i in arr:
    if i > element_max:
        element_max = i
print(element_max)