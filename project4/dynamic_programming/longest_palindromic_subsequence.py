"""
Complexities:
 * Runtime O(n^2), where n is the size of input string
 * Space O(n^2)
"""
def lps(input_string):
    # TODO: Complete this implementation of the LPS function
    # The function should return one value: the LPS length for the given input string
    length = len(input_string)
    match_matrix = create_matrix(len(input_string))
    for i in range(2, length+1):
        for start_ind in range(length-i+1):
            end_ind = start_ind + i - 1
            if input_string[start_ind] == input_string[end_ind]:
                match_matrix[start_ind][end_ind] = match_matrix[start_ind+1][end_ind-1] + 2
            else:
                match_matrix[start_ind][end_ind] = max(match_matrix[start_ind][end_ind-1], match_matrix[start_ind+1][end_ind])
    return match_matrix[0][-1]


def create_matrix(length):
    match_matrix = []
    for i in range(length):
        row = []
        for j in range(length):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        match_matrix.append(row)
    return match_matrix

def _test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


string = "TACOCAT"
solution = 7
test_case = [string, solution]
_test_function(test_case)

string = 'BANANA'
solution = 5
test_case = [string, solution]
_test_function(test_case)

string = 'BANANO'
solution = 3
test_case = [string, solution]
_test_function(test_case)
