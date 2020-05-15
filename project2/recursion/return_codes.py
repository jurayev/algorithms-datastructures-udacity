def get_alphabet(number):
    """
    Helper function to figure out alphabet of a particular number
    Remember:
        * ASCII for lower case 'a' = 97
        * chr(num) returns ASCII character for a number e.g. chr(65) ==> 'A'
    """
    return chr(number + 96)


def all_codes(number):  # 23
    """
    :param: number - input integer
    Return - list() of all codes possible for this number
    TODO: complete this method and return a list with all possible codes for the input number
    """
    if number == 0:
        return [""]
    # calculation for two right-most digits e.g. if number = 1123, this calculation is meant for 23
    reminder = number % 100  # 23
    out_100 = []
    if reminder <= 26 and number > 9:
        # get all codes for the remaining number
        char = get_alphabet(reminder)
        out_100 = all_codes(number // 100)

        for i, code in enumerate(out_100):
            out_100[i] = code + char

    # calculation for right-most digit e.g. if number = 1123, this calculation is meant for 3
    reminder = number % 10
    # get all codes for the remaining number
    char = get_alphabet(reminder)
    out_10 = all_codes(number//10)

    for i, code in enumerate(out_10):
        out_10[i] = code + char

    arr = []
    arr += out_100
    arr += out_10
    return arr


# number = 145
# solution = ['abc', 'aw', 'lc']

print(1//10)
print(all_codes(1145))