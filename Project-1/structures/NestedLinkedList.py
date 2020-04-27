class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)


def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    llist = LinkedList(None)
    if not list1:
        return list2
    if not list2:
        return list1

    node1 = list1.head
    node2 = list2.head

    while node1 or node2:
        if not node1:
            llist.append(node2.value)
            node2 = node2.next
        elif not node2:
            llist.append(node1.value)
            node1 = node1.next
        elif node1.value < node2.value:
            llist.append(node1.value)
            node1 = node1.next
        else:
            llist.append(node2.value)
            node2 = node2.next
    return llist


class NestedLinkedList(LinkedList):
    def flatten(self):
        # TODO: Implement this method to flatten the linked list in ascending sorted order.
        return self._flatten(self.head)

    def _flatten(self, node):
        if not node.next:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))

# First Test scenario
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)

solution = nested_linked_list.flatten()

assert solution == [1, 2, 3, 4, 5]
