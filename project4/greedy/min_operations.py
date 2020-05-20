def min_operations(target):
    """
    Return number of steps taken to reach a target number
    input: target number (as an integer)
    output: number of steps (as an integer)
    """
    steps = 0
    while target != 0:
        steps += 1
        if target % 2 == 1:
            target -= 1
        else:
            target /= 2
    return steps

def _test_function(test_case):
    target = test_case[0]
    solution = test_case[1]
    output = min_operations(target)
    print(f"Steps: {output}")
    if output == solution:
        print("Pass")
    else:
        print("Fail")

target = 18
solution = 6
test_case = [target, solution]
_test_function(test_case)

target = 69
solution = 9
test_case = [target, solution]
_test_function(test_case)
