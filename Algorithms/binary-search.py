def binarySearch(array,item):
    size = len(array)
    if size == 0:
        return False
    else:
        midpoint = size//2
        if array[midpoint] == item:
            return True
        else:
            if item < array[midpoint]:
                return binarySearch(array[:midpoint],item)
            else:
                return binarySearch(array[midpoint+1:],item)
