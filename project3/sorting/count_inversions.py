"""
TODO:
Complexities:
Runtime O(n log n)
Space O(n)
"""
def count_inversions(arr):

    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left, count_left = count_inversions(left)
    right, count_right = count_inversions(right)
    merged, count = merge(left, right)
    total = count_left + count_right + count
    return merged, total

def merge(left, right):
    merged = []
    left_ind = 0
    right_ind = 0
    count = 0
    while left_ind < len(left) and right_ind < len(right):
        if left[left_ind] > right[right_ind]:
            merged.append(right[right_ind])
            right_ind += 1
        else:
            merged.append(left[left_ind])
            left_ind += 1

    merged += left[left_ind:]
    merged += right[right_ind:]
    return merged, right_ind


def _test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    print(count_inversions(arr))
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")

arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
_test_function(test_case)

arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
_test_function(test_case)

arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
_test_function(test_case)