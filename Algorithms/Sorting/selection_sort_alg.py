def selection_sort(items):
    for i in range(0, len(items)-1):
        min_index = i

        for j in range(i+1, len(items)):
            if items[j] < items[min_index]:
                min_index = j

        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]

    return items
