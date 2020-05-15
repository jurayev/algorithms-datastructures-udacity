import random

"""
For this problem we traverse the input list and with help of two pointers compare current min/max value and replace the values if needed
The algorithm finds the solution within single traversal in order of O(n), linear complexity. Requires no additional memory.

Complexities:
* Runtime O(n), where n is the size of input list
* Space O(1), no additional memory required
"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None, None
    _min = ints[0]
    _max = ints[0]
    for integer in ints[1:]:
        if integer < _min:
            _min = integer
        if integer > _max:
            _max = integer
    return _min, _max


def _test_min_max(start, end):
    print(">" * 10, "Start _test_min_max", "<" * 10, "\n")
    l = [i for i in range(start, end)]
    random.shuffle(l)
    min_max = get_min_max(l)
    print(f"Actual: {min_max}")
    print(f"Expected: {(start, end-1)}")
    assert (start, end-1) == min_max
    print("TEST PASSED\n")


def _test_min_max_empty_input():
    print(">" * 10, "Start _test_min_max_empty_input", "<" * 10, "\n")
    min_max = get_min_max([])
    print(f"Actual: {min_max}")
    print(f"Expected: {(None, None)}")
    assert (None, None) == min_max
    print("TEST PASSED\n")

print("-"*10, "BEGIN TESTING", "-"*10, "\n")
_test_min_max(start=0, end=10)
_test_min_max(start=541, end=100000)
_test_min_max(start=1, end=2)
_test_min_max(start=1, end=3)
_test_min_max(start=-5, end=5)
_test_min_max(start=-5, end=0)
_test_min_max_empty_input()
print("\n", "-"*10, "ALL TESTS PASSED", "-"*10)