#divide and conquer
def binary_search_recursive(array, value_to_search, left, right):
    if left > right:
        print("Element not found")
        return

    mid = (left + right) // 2

    if array[mid] == value_to_search:
        print("Element found")
    elif array[mid] > value_to_search:
        binary_search_recursive(array, value_to_search, left, mid - 1)
    else:
        binary_search_recursive(array, value_to_search, mid + 1, right)

def binary_search(array,value_to_search):
    if len(array) == 0:
        print("Element not found")
        return

    left=0
    right=len(array)-1

    while left<=right:
        mid=(left+right)//2

        if array[mid] == value_to_search:
            print("Element found at ", mid+1)
            return
        elif array[mid] < value_to_search:
            left = mid + 1
        else:
            right = mid - 1

    print("Element not found")

array = [0,20,25,29,35,36,38,40,48,49,55,59,68,77,82,85,99,1001,2004]  #sorted array
value_to_search = int(input("enter value to search: "))
# binary_search(array,value_to_search)
binary_search_recursive(array,value_to_search,0,len(array)-1)
