"""
Complexities:

* Runtime O(n)
* Space O(n)
"""

def pair_sum_to_zero(input_list, target):
    cache = {}
    for index, el in enumerate(input_list):
        difference = target - el
        if difference not in cache:
            cache[el] = index
        else:
            return [index, cache[difference]]

def _test_function(test_case):
    output = pair_sum_to_zero(test_case[0], test_case[1])
    print(output)
    if sorted(output) == test_case[2]:
        print("Pass")
    else:
        print("Fail")

test_case_2 = [[10, 5, 9, 8, 12, 1, 16, 6], 16, [0, 7]]
_test_function(test_case_2)