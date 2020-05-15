
# Dutch national flag problem analysis

For this problem single traversal with 3 pointers approach is used. Single traversal is meant to have order of Runtime O(n).
The sorting is performed in-place, so Space order is O(1).

Complexities:

* `Runtime O(n)`, where n is the input list size. This is achieved by the following: the sort_012(input_list) implements a while loop
that traverses the input list exactly n-times by keeping track of the two index pointers, front_index and next_two. 
One of the pointers is incremented by one (decrement operation for the case of next_two pointer) at the time for each while loop
iteration. Once front_index and next_two are met each other we know that single traversal of n-times is done.
* `Space O(1)`, in-place sorting requires no additional space
