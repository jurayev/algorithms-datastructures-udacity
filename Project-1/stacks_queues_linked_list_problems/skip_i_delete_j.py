# LinkedList Node class for your reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head


def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
    i = 2
    j = 3
    Output = 1 2 6 7 11 12
    """
    node = head
    while node:
        for _ in range(1, i):
            if node.next:
                node = node.next
        tail = node
        for _ in range(j):
            if tail.next:
                tail = tail.next
        node.next = tail.next
        node = node.next
    return head

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 2
head = create_linked_list(arr)
solution = [1, 2, 5, 6, 9, 10]

print_linked_list(skip_i_delete_j(head, i, j))
