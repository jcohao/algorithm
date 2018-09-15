"""
    快速排序
"""

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        great = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(great)

print(quicksort([4, 5, 4, 1, 2, 7, 9, 8]))