def reverse_string(input):
    """
    Return reversed input string

    Examples:
       reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """
    if len(input) == 0:
        return ""
    first = input[0]
    next_input = input[1:]
    rev = reverse_string(next_input)
    return rev + first


res = reverse_string("abc")
print(res)
assert res == "cba"
