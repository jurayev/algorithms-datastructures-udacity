def path_from_root_to_node(root, data):
    """
    :param: root - root of binary tree
    :param: data - value (representing a node)
    TODO: complete this method and return a list containing values of each node in the path
    from root to the data node
    """

    def return_path(node):  # 2
        if not node:
            return None
        if node.data == data:
            return [node.data]

        left_path = return_path(node.left)  # 521
        if left_path:
            left_path.append(node.data)
            return left_path

        right_path = return_path(node.right)  # None
        if right_path:
            right_path.append(node.data)
            return right_path

    path = return_path(root)
    return list(reversed(path))

