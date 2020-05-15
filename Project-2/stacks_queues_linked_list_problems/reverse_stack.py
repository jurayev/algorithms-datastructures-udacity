"""
### Problem Statement

Reverse a stack. If your stack initially has `1, 2, 3, 4` (4 at the top and 1 at the bottom),
after reversing the order must be `4, 3, 2, 1` (4 at the bottom and 1 at the top).
"""
from structures.StackArray import Stack


def reverse_stack(stack):
    """
    Reverse a given input stack

    Args:
       stack(stack): Input stack to be reversed
    Returns:
       stack: Reversed Stack
    """
    # 1, 2, 3, 4
    reversed_stack = Stack()
    while not stack.is_empty():
        reversed_stack.push(stack.pop())
    stack = reversed_stack