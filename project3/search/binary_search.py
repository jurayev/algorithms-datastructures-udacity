"""
Complexities:
Runtime O(log n)
Space O(1)
"""
def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = array[mid]

        if target == mid_element:
            return mid
        elif target < mid_element:
            high = mid - 1
        else:
            low = mid_element + 1

    return -1