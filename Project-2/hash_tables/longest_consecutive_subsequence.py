def longest_consecutive_subsequence(input_list):
    # TODO: Write longest consecutive subsequence solution
    input_list.sort()
    # iterate over the list and store element in a suitable data structure
    subseq_indexes = {}
    index = 0
    for el in input_list:
        if index not in subseq_indexes:
            subseq_indexes[index] = [el]
        elif subseq_indexes[index][-1] + 1 == el:
            subseq_indexes[index].append(el)
        else:
            index += 1
            subseq_indexes[index] = [el]

    # traverse / go over the data structure in a reasonable order to determine the solution
    longest_subseq = max(subseq_indexes.values(), key=len)
    return longest_subseq


res = longest_consecutive_subsequence([5, 4, 7, 10, 1, 3, 55, 2, 6])
print(res)
# should be [1, 2, 3, 4, 5, 6, 7]
