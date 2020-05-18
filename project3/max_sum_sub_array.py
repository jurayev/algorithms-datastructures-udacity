"""
Complexities:
* Runtime O(n log n)
* Space O(1)

Pseudo code
maxSubArrayRecursive(arr, start, stop)     T(n)
  1. if (start==stop):
      return arr[start]

  2. Calculate mid index       constant

  3. L = maxSubArrayRecursive(arr, start, mid)       T( 𝑛2 )

  4. R = maxSubArrayRecursive(arr, mid+1, stop)       T( 𝑛2 )

  5. C = maxCrossingSum(arr, start, mid, stop)         Θ(𝑛)

  6. return max(C, max(L,R))       constant
"""
def max_sub_array(arr):
    """
    param: An array `arr`
    return: The maximum sum of the contiguous subarray.
    No need to return the subarray itself.
    """
    def traverse(arr, start, stop):
        if start == stop:
            return arr[start]

        mid = (start + stop) // 2

        left_arr = traverse(arr, start, mid)
        right_arr = traverse(arr, mid + 1, stop)

        crossing = max_crossing_sum(arr, start, mid, stop)
        return max(crossing, max(left_arr, right_arr))

    return traverse(arr, 0, len(arr)-1)


def max_crossing_sum(arr, start, mid, stop):

    left_sum = arr[mid]
    left_max_sum = arr[mid]
    for i in range(mid-1, start-1, -1):
        left_sum += arr[i]
        if left_sum > left_max_sum:
            left_max_sum = left_sum

    right_sum = arr[mid+1]
    right_max_sum = arr[mid+1]
    for j in range(mid+2, stop+1):
        right_sum += arr[j]
        if right_sum > right_max_sum:
            right_max_sum = right_sum

    return left_max_sum + right_max_sum

arr1 = [-2, -5, 6, -2, -3, 1, 5, -6]
max_crossing_sum(arr1, 0, len(arr1)//2, len(arr1)-1)  # 7
# Test your code
arr = [-2, 7, -6, 3, 1, -4, 5, 7]
print("Maximum Sum = ", max_sub_array(arr))     # Outputs 13

# Test your code
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Sum = ", max_sub_array(arr))     # Outputs 6

# Test your code
arr = [-4, 14, -6, 7]
print("Maximum Sum = ", max_sub_array(arr))     # Outputs 15

# Test your code
arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
print("Maximum Sum = ", max_sub_array(arr))     # Outputs 10

# Test your code
arr = [-2, -5, 6, -2, -3, 1, 5, -6]
print("Maximum Sum = ", max_sub_array(arr))     # Outputs 7
