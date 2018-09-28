def binary_search(items, search_value):
    left = 0
    right = len(items)
    

    while left<=right:
        mid = (left+right)//2
        
        if items[mid] == search_value:
            return mid
        
        if search_value < items[mid]:
            right = mid-1
        else:
            left = mid+1
    
    return -1

# items = list(map(int, input().split(' '))).sort()
search_value = int(input("Enter searching item:"))
result = binary_search([2,4,7,8,10,12,14], search_value)

if result == -1:
    print("Not Found")
else:
    print("Position:",result)
