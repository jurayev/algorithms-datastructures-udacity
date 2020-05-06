def last_index(arr, target):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    TODO: complete this method to find the last index of target in arr
    """
    return last_index_sol(arr, target, 0)

def last_index_sol(arr, target, index):
    if index >= len(arr):
        return -1
    last = last_index_sol(arr, target, index+1)
    if target == arr[index] and last < 0:
        return index
    return last


# Solution
def last_index2(arr, target):
    # we start looking from the last index
    return last_index_arr2(arr, target, len(arr) - 1)


def last_index_arr2(arr, target, index):
    if index < 0:
        return -1

    # check if target is found
    if arr[index] == target:
        return index

    # else make a recursive call to the rest of the array
    return last_index_arr2(arr, target, index - 1)

arr = [1, 2, 5, 5, 4]
target = 5
solution = 3
res = last_index(arr, target)
assert res == solution