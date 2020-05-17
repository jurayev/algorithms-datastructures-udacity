"""
implemented using timsort and binary search variation

Complexities:

* Runtime O(n)
* Space O(1)
"""

def pair_sum(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    TODO: complete this method to find two numbers such that their sum is equal to the target
    Return the two numbers in the form of a sorted list
    """
    arr.sort()  # O(log n)
    high = len(arr)-1
    low = 0
    while low <= high:   # O(n)
        if arr[low] + arr[high] == target:
            return [arr[low], arr[high]]
        elif arr[low] + arr[high] < target:
            low += 1
        else:
            high -= 1
    return [None, None]


def _test_function(test_case):
    input_list = test_case[0]
    target =test_case[1]
    solution = test_case[2]
    output = pair_sum(input_list, target)
    if output == solution:
        print("Pass")
    else:
        print("False")


input_list = [2, 7, 11, 15]
target = 9
solution = [2, 7]
test_case = [input_list, target, solution]
_test_function(test_case)

input_list = [0, 8, 5, 7, 9]
target = 9
solution = [0, 9]
test_case = [input_list, target, solution]
_test_function(test_case)

input_list = [0, 8, 5, 7, 9]
target = 12
solution = [5, 7]
test_case = [input_list, target, solution]
_test_function(test_case)

input_list = [110, 9, 89]
target = 9
solution = [None, None]
test_case = [input_list, target, solution]
_test_function(test_case)
