
# Rearrange array digits implementation analysis

For this problem the merge sort algorithm is used (could also use the quick sort, but for the practice sake I used the merge sort here).
Once we have a sorted input in descending order we can peek every two elements and assign to left_max and right_max accordingly.

Complexities:
* `Runtime O(n log n)`
* `Space O(n)`
