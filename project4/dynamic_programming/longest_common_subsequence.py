"""
Complexities:
 * Runtime O(n1*n2) or O(n^2), where n1 size of string 1, n2 size of string 2
 * Space O(n1*n2), where n1 size of string 1, n2 size of string 2
"""
def lcs(string_a, string_b):
    match_matrix = [[0 for _ in range(len(string_a)+1)] for _ in range(len(string_b)+1)]
    for i in range(len(string_b)):
        for j in range(len(string_a)):
            if string_b[i] == string_a[j]:
                match_matrix[i+1][j+1] = match_matrix[i][j] + 1
            else:
                match_matrix[i+1][j+1] = max(match_matrix[i][j+1], match_matrix[i+1][j])
    return match_matrix[-1][-1]

# Tests
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs(test_A2, test_B2)

test_A3 = "masterpiece"
test_B3 = "go"

lcs_val3 = lcs(test_A3, test_B3)
print('LCS val 1 = ', lcs_val1)
assert lcs_val1==5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2==7, "Incorrect LCS value."
print('LCS val 3 = ', lcs_val3)
assert lcs_val3==0, "Incorrect LCS value."
print('Tests passed!')
