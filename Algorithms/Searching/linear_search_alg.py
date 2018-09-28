def linear_search(items, search_value):
    for i in range(len(items)):
        if items[i]==search_value:
            return i
    return -1

# items = list(map(int, input().split(' ')))