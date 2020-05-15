"""
Define a procedure, deep_reverse, that takes as input a list,
and returns a new list that is the deep reverse of the input list.
This means it reverses all the elements in the list,
and if any of those elements are lists themselves, reverses all the elements in the inner list, all the way down.
"""


def deep_reverse(arr):
    return reverse(arr, 0)


def is_list(instance):
    return isinstance(instance, list)


def reverse(arr, index):
    if index == len(arr):
        return list()

    curr_element = arr[index]

    if is_list(curr_element):
        curr_element = reverse(curr_element, 0)

    new_arr = reverse(arr, index + 1)
    new_arr.append(curr_element)
    return new_arr


arr =  [1, [2,3], 4, [5,6]]
solution = [ [6,5], 4, [3, 2], 1]
res = deep_reverse(arr)
print(res)
assert res == solution
