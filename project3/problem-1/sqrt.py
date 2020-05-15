from math import floor
"""
For this problem I used a binary search which produces O(log n) Runtime complexity. For searching sqrt multiplier the algorithm
divides the input number by half to decrease the search order, and generates the possible range of multipliers.

Complexities:
* Runtime O(log n), where n is the size of range the search is performed against
* Space O(n/2), where n is the size of range the search is performed against
"""

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    high = number
    low = 0
    while low <= high:
        mid = (low + high) // 2
        midsquare = mid * mid
        next_midsquare = (mid+1) * (mid+1)
        if midsquare == number or midsquare < number < next_midsquare:
            return mid
        elif midsquare > number:
            high = mid - 1
        else:
            low = mid + 1


print("-"*10, "BEGIN TESTING", "-"*10, "\n")
print ("TEST PASSED" if 3 == sqrt(9) else "TEST FAILED")
print ("TEST PASSED" if 0 == sqrt(0) else "TEST FAILED")
print ("TEST PASSED" if 4 == sqrt(16) else "TEST FAILED")
print ("TEST PASSED" if 1 == sqrt(1) else "TEST FAILED")
print ("TEST PASSED" if 5 == sqrt(27) else "TEST FAILED")
print ("TEST PASSED" if 6 == sqrt(48) else "TEST FAILED")
print ("TEST PASSED" if 7 == sqrt(49) else "TEST FAILED")
print ("TEST PASSED" if floor(sqrt(5000)) == sqrt(5000) else "TEST FAILED")
print ("TEST PASSED" if floor(sqrt(999999)) == sqrt(999999) else "TEST FAILED")
print("\n", "-"*10, "ALL TESTS PASSED", "-"*10)
