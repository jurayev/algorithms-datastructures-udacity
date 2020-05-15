
# Binary Search Tree
class Tree():
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    def insert_with_loop(self, new_value):
        new_node = Node(new_value)
        node = self.root
        if not node:
            self.root = new_node
            return

        while node:
            comparison = self.compare(node, new_node)
            if comparison == 0:
                # override with new node's value
                node.set_value(new_value)
                break
            elif comparison == -1:
                # traverse left
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break
            else:
                # traverse right
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break

    def insert_with_recursion(self,value):

        def search_and_insert(node):
            comparison = self.compare(node, new_node)
            if comparison == 0:
                #override with new node's value
                node.set_value(value)
            elif comparison == -1:
                # traverse left
                if node.has_left_child():
                    search_and_insert(node.get_left_child())
                else:
                    node.set_left_child(new_node)
            else:
                # traverse right
                if node.has_right_child():
                    search_and_insert(node.get_right_child())
                else:
                    node.set_right_child(new_node)
        node = self.root
        if not node:
            self.set_root(value)
        else:
            new_node = Node(value)
            search_and_insert(node)

    def search(self, value):
        search_node = Node(value)
        node = self.get_root()
        if not node:
            return False

        while True:
            comparison = self.compare(node, search_node)
            if comparison == 0:
                return True
            elif comparison == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    return False
            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return False
