def binary_search_recursive(array, target):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    def binary_search_recursive_soln(array, target, start_index, end_index):
        if start_index > end_index:
            return -1

        mid = (start_index + end_index) // 2
        mid_element = array[mid]

        if mid_element == target:
            return mid
        elif target < mid_element:
            return binary_search_recursive_soln(array, target, start_index, mid - 1)
        else:
            return binary_search_recursive_soln(array, target, mid + 1, end_index)

    return binary_search_recursive_soln(array, target, 0, len(array) - 1)


def _test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")

array = [0, 1, 2, 3, 4, 5, 6, 7, 9]
target = 9
index = 8
test_case = [array, target, index]
_test_function(test_case)