"""
For this problem single traversal with 3 pointers approach is used. Single traversal is meant to have order of Runtime O(n).
The sorting is performed in-place, so Space order is O(1).

Complexities:

* `Runtime O(n)`, where n is the input list size. This is achieved by the following: the sort_012(input_list) implements a while loop
that traverses the input list exactly n-times by keeping track of the two index pointers, front_index and next_two.
One of the pointers is incremented by one (decrement operation for the case of next_two pointer) at the time for each while loop
iteration. Once front_index and next_two are met each other we know that single traversal of n-times is done.
* `Space O(1)`, in-place sorting requires no additional space
"""

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    next_zero = 0
    next_two = len(input_list) - 1
    front_index = 0
    while front_index <= next_two:
        if input_list[front_index] == 0:
            input_list[front_index], input_list[next_zero] = input_list[next_zero], 0
            next_zero += 1
            front_index += 1
        elif input_list[front_index] == 2:
            input_list[front_index], input_list[next_two] = input_list[next_two], 2
            next_two -= 1
        else:
            front_index += 1


def _test_function(test_case):
    sort_012(test_case)
    if test_case == sorted(test_case):
        print("TEST PASSED")
    else:
        print("TEST FAILED")


print("-"*10, "BEGIN TESTING", "-"*10, "\n")
_test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
_test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
_test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
_test_function([2, 0, 1])
_test_function([2, 2, 2, 2, 2, 0, 1, 2, 2, 2, 2])
print("\n", "-"*10, "TESTING COMPLETED", "-"*10)
