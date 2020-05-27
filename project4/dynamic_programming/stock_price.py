"""
Complexities:
 * Runtime O(n), n is the number of stock prices
 * Space O(n)
"""
def max_returns(prices):
    min_index = 0
    max_index = 1
    curr_min_index = 0

    if 2 > len(prices):
        return -1
    for i in range(1, len(prices)):
        if prices[curr_min_index] > prices[i]:
            curr_min_index = i

        if prices[i] - prices[curr_min_index] > prices[max_index] - prices[min_index]:
            max_index = i
            min_index = curr_min_index

    return prices[max_index] - prices[min_index]

# Test Cases
def _test_function(test_case):
    prices = test_case[0]
    solution = test_case[1]
    output = max_returns(prices)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
solution = 76
test_case = [prices, solution]
_test_function(test_case)

prices = [54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]
solution = 66
test_case = [prices, solution]
_test_function(test_case)

prices = [78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]
solution = 0
test_case = [prices, solution]
_test_function(test_case)

prices = [78, 54, 45, 37, 34, 23, 24, 12, 9, 9, 7, 2, 2]
solution = 1
test_case = [prices, solution]
_test_function(test_case)
