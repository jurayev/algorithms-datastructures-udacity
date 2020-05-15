
# Search in a rotated sorted array implementation analysis

For this problem I used a binary search which produces O(log n) Runtime complexity. If mid index does not hit the target number
then the algorithm tries to guess in which part to search by comparing mid index element and high/low index with the target number.
No additional memory is required.

Complexities:
* `Runtime O(log n)`, where n is the size of input list the search is performed against
* `Space O(1)`
