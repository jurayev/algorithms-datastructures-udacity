from structures.StackArray import Stack


def evaluate_post_fix(input_list):
    """
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
       3 4 5 × −, which unambiguously means 3 (4 5 ×) −
    """
    stack = Stack()
    for el in input_list:
        if el == "+":
            arg1 = stack.pop()
            arg2 = stack.pop()
            stack.push(arg2 + arg1)
        elif el == "*":
            arg1 = stack.pop()
            arg2 = stack.pop()
            stack.push(arg2 * arg1)
        elif el == "/":
            arg1 = stack.pop()
            arg2 = stack.pop()
            stack.push(int(arg2 / arg1))
        elif el == "-":
            arg1 = stack.pop()
            arg2 = stack.pop()
            stack.push(arg2 - arg1)
        else:
            stack.push(int(el))
    return stack.pop()


test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
#  (10 * (6 / ((9+3) * -11))) + 17 + 5 == 22
res = evaluate_post_fix(test_case_3[0])
print(f"{res} == {test_case_3[1]}")
assert res == test_case_3[1]
