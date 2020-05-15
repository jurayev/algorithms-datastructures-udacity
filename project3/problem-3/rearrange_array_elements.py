"""
For this problem the MergeSort algorithm is used.
Once we have a sorted input in descending order we can peek every two elements and assign to left_max and right_max accordingly.

Complexities:
* `Runtime O(n log n)` Complexity is achieved by the following:
        1. sort(input_list) function implements the MergeSort algorithm with runtime complexity of O(n log n) and space complexity of O(n)
        for the worst case scenario.
        2. rearrange_digits(input_list) function implements 'for loop' with runtime of O(n/2) iterating half n-times, where 'n'
        is the sorted by sort(input_list) input_list size. However, rearrange_digits(input_list) uses MergeSort function inside with
        O(n log n) complexity that overrides O(n/2) and produces the final complexity of O(n log n)
* `Space O(n)`, in the worst case scenario the rearrange_digits(input_list)
function will use n-size additional space to store sorted input_list result
"""

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    if len(input_list) <= 1:
        return input_list

    sorted_list = sort(input_list)
    left_max = ""
    right_max = ""
    for i in range(0, len(sorted_list), 2):
        left_max += str(sorted_list[i])
        if i < len(sorted_list) - 1:
            right_max += str(sorted_list[i+1])

    return [int(left_max), int(right_max)]


def sort(input_list):
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2

    left = input_list[:mid]
    right = input_list[mid:]

    left = sort(left)
    right = sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
    return merged


def _test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("TEST PASSED")
    else:
        print("TEST FAILED")


print("-"*10, "BEGIN TESTING", "-"*10, "\n")
_test_function([[1, 2, 3, 4, 5], [542, 31]])
_test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
_test_function([[1, 2], [1, 2]])
_test_function([[1], [1]])
_test_function([[1, 0, 2], [20, 1]])
_test_function([[1, 2, 5, 7, 4, 8, 3, 9, 6], [97531, 8642]])
_test_function([[1, 0, 0, 0, 0, 0, 1, 0, 0], [10000, 1000]])
print("\n", "-"*10, "TESTING COMPLETED", "-"*10)
