class BinaryTreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def diameter_of_binary_tree(root):
    """
    :param: root - Root of binary tree
    TODO: Complete this method and return diameter (int) of binary tree
    """
    if not root:
        return 0, 0

    def in_order_traverse(node):
        if not node:
            return 0, 0

        height_left, diameter_left = in_order_traverse(node.left)
        height_right, diameter_right = in_order_traverse(node.right)

        height = max(height_left, height_right) + 1
        height_diameter = height_left + height_right
        diameter = max(diameter_left, diameter_right, height_diameter)
        return height, diameter

    return in_order_traverse(root)[1]


arr = [1, 2, 3, 4, 5, None, None, None, None, None, None]
solution = 3
