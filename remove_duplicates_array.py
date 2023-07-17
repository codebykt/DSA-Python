arr = [8,56,85,62,6,5,2,945,286,2,42,2,415,2,0,3,87,0,3,21,2]
print("before removing duplicates")
print(arr)
new_arr = []
for i in arr:
    if i not in new_arr:
        new_arr.append(i)
print("without duplicates")
print(new_arr)