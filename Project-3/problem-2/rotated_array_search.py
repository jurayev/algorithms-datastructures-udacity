"""
For this problem I used a binary search which produces O(log n) Runtime complexity. If mid index does not hit the target number
then the algorithm tries to guess in which part to search by comparing mid index element and high/low index with the target number.
No additional memory is required.

Complexities:
* Runtime O(log n), where n is the size of input list the search is performed against
* Space O(1)

Not sure if this solution is elegant, would be glad to hear some feedback
"""

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array
    """
    high = len(input_list) - 1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if input_list[mid] == number:
            return mid
        elif input_list[mid] < number <= input_list[high]:
            low = mid + 1
        else:
            if input_list[low] <= number:
                high = mid - 1
            else:
                low = mid + 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def _test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("TEST PASSED")
    else:
        print("TEST FAILED")


print("-"*10, "BEGIN TESTING", "-"*10, "\n")
_test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
_test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
_test_function([[6, 7, 8, 1, 2, 3, 4], 8])
_test_function([[6, 7, 8, 1, 2, 3, 4], 1])
_test_function([[6, 7, 8, 1, 2, 3, 4], 10])
_test_function([[0], 0])
_test_function([[], 5])
_test_function([[5, 1], 5])
_test_function([[5, 1], 1])
print("\n", "-"*10, "ALL TESTS PASSED", "-"*10)
