"""
    二分查找
"""

def binary_search(list, num):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int( (low + high) / 2 )
        if num == list[mid]:
            print('found')
            return num
        elif num > list[mid]:
            low = mid + 1
        else:
            high = mid - 1

    print('not found')
    return None