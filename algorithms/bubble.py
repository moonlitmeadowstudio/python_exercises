def bubble_sort(items):
    flag = True
    while flag:
        flag = False
        for i in range(len(items) - 1):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                flag = True
    return items

