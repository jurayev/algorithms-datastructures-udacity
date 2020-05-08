
# Active Directory implementation
For this problem I used recursion to traverse the active directory hierarchy. Base approach is to check membership of
users list, if no user found check membership in other sub groups.

Complexity analysis:
* Runtime O(nm), assuming 'n' is the number of groups and 'm' is the number of groups each group has.
* Space (1), constant space complexity as no additional memory is used

