class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree:
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

# Depth First Search algorithm
# define pre-order traversal
def pre_order_traversal(tree):
    node = tree.get_root()
    visited_nodes = []

    def traverse(node):
        # A -> B -> D -> C
        if node:
            # visit
            visited_nodes.append(node.get_value())
            # traverse left
            traverse(node.get_left_child())
            # traverse right
            traverse(node.get_right_child())

    traverse(node)
    return visited_nodes

# define in-order traversal
def in_order_traversal(tree):
    node = tree.get_root()
    visited_nodes = []

    def traverse(node):
        # D -> B -> A -> C
        if node:
            traverse(node.get_left_child())
            visited_nodes.append(node.get_value())
            traverse(node.get_right_child())


    traverse(node)
    return visited_nodes

# define post-order traversal
def post_order_traversal(tree):
    node = tree.get_root()
    visited_nodes = []

    def traverse(node):
        # D -> B -> A -> C
        if node:
            traverse(node.get_left_child())
            traverse(node.get_right_child())
            visited_nodes.append(node.get_value())

    traverse(node)
    return visited_nodes