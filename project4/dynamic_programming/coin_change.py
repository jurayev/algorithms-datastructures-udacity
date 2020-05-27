import math

"""
Complexities:
 * Runtime O(n^2), where n is the number of coins
 * Space O(1)
"""
def coin_change(coins, amount):
    min_coins = 0
    for coin in reversed(coins):
        if coin < amount:
            min_coins += amount // coin  # 3
            change = amount % coin  # 5
            if change in coins:
                return min_coins + 1
    return -1


"""
Complexities:
 * Runtime O(n*m), where n is the number of coins, m is the target amount
 * Space O(m), m is the target amount
"""
def coin_change_memo(coins, amount):
    memo = {}

    def get_change(remaining):
        if remaining < 0: return math.inf
        if remaining == 0: return 0

        if remaining not in memo:
            memo[remaining] = min(get_change(remaining - coin) + 1 for coin in coins)
        return memo[remaining]

    result = get_change(amount)
    return -1 if result == math.inf else result


def _test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change_memo(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [1,2,5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
_test_function(test_case)

arr = [1,4,5,6]
amount = 23
solution = 4
test_case = [arr, amount, solution]
_test_function(test_case)

arr = [5,7,8]
amount = 2
solution = -1
test_case = [arr, amount, solution]
_test_function(test_case)
