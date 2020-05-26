import collections

Item = collections.namedtuple('Item', ['weight', 'value'])

"""
Complexities analysis:
 * Runtime O(n * W), n - number of elements in knapsack, W - weight limit
 * Space O(n), n - number of elements in knapsack.
"""
def max_value(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack.
    """
    values = [0 for _ in range(knapsack_max_weight+1)]
    for item in items:
        for weight in range(knapsack_max_weight, item.weight-1, -1):
            values[weight] = max(values[weight], values[weight - item.weight] + item.value)
    return values[-1]


tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
for test in tests:
    assert test['correct_output'] == max_value(**test['input'])
