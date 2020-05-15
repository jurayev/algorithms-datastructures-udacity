def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """
    if len(input) < 2:
        return True
    first_char = input[0]
    last_char = input[-1]
    return first_char == last_char and is_palindrome(input[1:-1])


res = is_palindrome("madam")
print(res)
assert res

