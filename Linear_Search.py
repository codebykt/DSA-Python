array = [1,39.3,5,48,67,45,245,214,34,0,45,4]
value_to_search = int(input("Enter Value to Search: "))
found = False

for i in range(len(array)):
    if array[i] == value_to_search:
        print("found at position: ", i+1)
        found=True
if not found :
    print("element not found in the array")
