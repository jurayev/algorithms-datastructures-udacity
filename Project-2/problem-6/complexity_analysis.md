
# Linked List Union and Intersection implementation

## union
Complexity analysis for union opearation based on iteration through each node of the llist_1
for the each node in the llist_2.

Complexities:
* `Runtime O(nm)`, assuming 'n' is the size of the llist_1 and 'm' is the size of the llist_2
* `Space O(nm)`, assuming 'n' is the size of the llist_1 and 'm' is the size of the llist_2, 
then for the worst case when llist_1 and llist_2 are completely different, we require a new linked list 'nm' sized

## intersection
Complexity analysis is quite straight forward since we iterate through each node of the llist_1
for the each node in the llist_2.

Complexities: 
* `Runtime O(nm)`, assuming 'n' is the size of the llist_1 and 'm' is the size of the llist_2
* `Space O(n)`, assuming 'n' is the size of the llist_1 and 'n' is the size of the llist_2, 
then for the worst case when llist_1 and llist_2 are the same, we require a new linked list 'n' sized
