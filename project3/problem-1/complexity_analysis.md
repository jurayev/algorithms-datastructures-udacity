
# Square root of an integer implementation analysis

For this problem I used a binary search which produces O(log n) Runtime complexity. For searching sqrt multiplier the algorithm
divides the input number by half to decrease the search order, and generates the possible range of multipliers.

Complexities:
* `Runtime O(log n)`, where n is the size of range the search is performed against
* `Space O(n/2)`, where n is the size of range the search is performed against
