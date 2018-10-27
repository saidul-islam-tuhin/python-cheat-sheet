# using for loop

def linearSearch(array,item):
    for i in array:
        if i == item:
            return True
            break
    else:
        return False
 
 
# using while loop

def linearSearch(array,item):
    
    found = False
    index = 0
    while index < len(array) and found is False:
        if array[index] == item:
            found = True
            break
        else:
            index += 1
    return found
