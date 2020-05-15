from structures.StackArray import Stack


def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    stack = Stack()
    for el in equation:
        if el == "(":
            stack.push(")")
        elif el == ")":
            if stack.pop() == None:
                return False
    return stack.size() == 0


print ("Pass" if (equation_checker('()((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")