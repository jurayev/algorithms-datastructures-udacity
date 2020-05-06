def permutations1(string):
    return return_permutations(string, 0)


def return_permutations(string, index):
    # Base Case
    if index >= len(string):
        return [""]

    small_output = return_permutations(string, index + 1)

    output = list()
    current_char = string[index]

    # iterate over each permutation string received thus far
    # and place the current character at between different indices of the string
    for permutation in small_output:
        for index in range(len(small_output[0]) + 1):
            new_permutation = permutation[0: index] + current_char + permutation[index:]
            output.append(new_permutation)
    return output


def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    perms = []
    if len(string) == 0:
        perms.append(string)
    else:
        first_char = string[0]#a #b
        sub_perms = permutations(string[1:])  #b #""
        for p in sub_perms:
            for i in range(len(p)+1):
                c = list(p)
                c.insert(i, first_char)
                perms.append("".join(c))
    return perms

print(permutations("abcd"))
#['abc', 'bac', 'bca', 'acb', 'cab', 'cba']

res = "abc"
print(list(res))
