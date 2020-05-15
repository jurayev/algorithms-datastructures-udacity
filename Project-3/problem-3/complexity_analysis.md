
# Rearrange array digits implementation analysis

For this problem the MergeSort algorithm is used.
Once we have a sorted input in descending order we can peek every two elements and assign to left_max and right_max accordingly.

Complexities:
* `Runtime O(n log n)` Complexity is achieved by the following: 
        1. sort(input_list) function implements the MergeSort algorithm with runtime complexity of O(n log n) and space complexity of O(n)
        for the worst case scenario.
        2. rearrange_digits(input_list) function implements 'for loop' with runtime of O(n/2) iterating half n-times, where 'n'
        is the sorted by sort(input_list) input_list size. However, rearrange_digits(input_list) uses MergeSort function inside with 
        O(n log n) complexity that overrides O(n/2) and produces the final complexity of O(n log n)
* `Space O(n)`, in the worst case scenario the rearrange_digits(input_list) 
function will use n-size additional space to store sorted input_list result
