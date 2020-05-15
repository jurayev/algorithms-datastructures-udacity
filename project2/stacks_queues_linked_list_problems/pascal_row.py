def nth_row_pascal(n):
    """
    Runtime compl O(n^2)
    Space compl O(2n)
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    curr_row = [1]
    for i in range(1, n + 1):
        prev_row = curr_row
        curr_row = [1]
        for j in range(i - 1):
            curr_row.append(prev_row[j] + prev_row[j + 1])
        curr_row.append(1)
    return curr_row


res = nth_row_pascal(4)
print(res)
# [1,4,6,4,1]
