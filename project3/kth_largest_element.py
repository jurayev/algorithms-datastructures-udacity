"""
Complexities:

Runtime O(n)
Space O(n)
"""

def fast_select(arr, k):
    # Implement the algorithm explained above to find the k^th lasrgest element in the given array
    n = len(arr)

    if 0 < k <= n:

        pivot = 0
        arr_less_p = []
        arr_equal_p = []
        arr_more_p = []
        medians = []
        i = 0
        # Step 1 - Break Arr into groups of size 5
        # Step 2 - For each group, sort and find median (middle). Add the median to setOfMedians
        while i < n // 5:                               # n//5 gives the integer quotient of the division
            medians.append(find_median(arr[i*5:i*5+5])) # find median of each group of size 5
            i += 1
        # If n is not a multiple of 5, then a last group with size = n % 5 will be formed
        if i*5 < n:
            medians.append(find_median(arr[i*5:i*5+n%5]))
        # Step 3 - Find the median of setOfMedians
        if len(medians) == 1:
            pivot = medians[0]
        elif len(medians) > 1:
            pivot = fast_select(medians, len(medians)//2)
        # Step 4 - Partition the original Arr into three sub-arrays
        for num in arr:
            if num < pivot:
                arr_less_p.append(num)
            elif num > pivot:
                arr_more_p.append(num)
            else:
                arr_equal_p.append(num)
        # Step 5 - Recurse based on the sizes of the three sub-arrays
        if k <= len(arr_more_p):
            return fast_select(arr_more_p, k)
        elif k > len(arr_more_p) + len(arr_equal_p):
            return fast_select(arr_less_p, k - len(arr_more_p) - len(arr_equal_p))
        else:
            return pivot


def find_median(arr):
    arr.sort()
    middle = len(arr) // 2
    return arr[middle]


# arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
# k = 5
# print(fast_select(arr, k))        # Outputs 12
#
# arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
# k = 5
# print(fast_select(arr, k))        # Outputs 11
#
# arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
# k = 10
# print(fast_select(arr, k))        # Outputs 99

arr = [3,2,1,5,6,4]
k = 2
print(fast_select(arr, k))        # Outputs 5