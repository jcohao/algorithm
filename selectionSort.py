"""
    选择排序
"""

def findSmallest(list):
    smallest = list[0]
    smallest_index = 0
    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i

    return smallest_index


def selectionSort(list):
    newArr = []
    for i in range(len(list)):
        smallest_index = findSmallest(list)
        newArr.append(list.pop(smallest_index))

    return newArr
