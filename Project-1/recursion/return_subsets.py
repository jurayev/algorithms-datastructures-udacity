def subsets(arr):
    return return_subsets(arr, 0)


def return_subsets(arr, index):  # [5,7] # [7] # []
    """
    :param: arr - input integer array
    Return - list of lists (two dimensional array) where each list represents a subset
    TODO: complete this method to return subsets of an array
    """
    if len(arr) <= index:
        return [[]]

    subsets_out = return_subsets(arr, index + 1)  # [], [15]
    output = []
    for el in subsets_out:
        output.append(el)

    for el in subsets_out:
        current = []
        current.append(arr[index])
        current.extend(el)
        output.append(current)

    return output

arr = [9, 12, 15]
solution = [[], [15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]]
print(subsets(arr))
