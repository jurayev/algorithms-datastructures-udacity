"""
Problem Statement

Suppose there is a staircase that you can climb in either 1 step, 2 steps, or 3 steps.
In how many possible ways can you climb the staircase if the staircase has n steps?
Write a recursive function to solve the problem-2.
"""
def staircase(n):
    """
    :param: n - number of steps in the staircase
    Return number of possible ways in which you can climb the staircase
    TODO - write a recursive function to solve this problem
    """
    if n <= 1:
        return 1
    elif n == 2:
        return 2

    return staircase(n-1) + staircase(n-2) + staircase(n-3)


def staircase_with_caching(n):
    cache = {0: 1, 1: 1, 2: 2, 3: 4}

    def staircase_memoize(n):
        if n not in cache.keys():
            cache[n] = staircase_memoize(n - 1) + staircase_memoize(n - 2) + staircase_memoize(n - 3)
        return cache[n]

    return staircase_memoize(n)


def t_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = staircase_with_caching(n)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


n = 3
solution = 4
case = [n, solution]
t_function(case)

n = 4
solution = 7
case = [n, solution]
t_function(case)

n = 7
solution = 44
case = [n, solution]
t_function(case)
print(staircase_with_caching(44))