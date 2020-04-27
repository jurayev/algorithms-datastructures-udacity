# Helpers
class Node:
    """LinkedListNode class to be used for this problem"""
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
        print(head.data, end=" ")
        head = head.next
    print()

def swap_nodes(head, left_index, right_index):
    """
    :param: head- head of input linked list
    :param: left_index - indicates position
    :param: right_index - indicates position
    return: head of updated linked list with nodes swapped
    TODO: complete this function and swap nodes present at left_index and right_index
    Do not create a new linked list
    linked_list = 3 4 5 2 6 1 9
    positions = 3 4
    output = 3 4 5 6 2 1 9
    """
    if left_index == right_index:
        return head

    index = 0
    left = None  # 2 1 9
    left_prev = None
    right = None  # 6 2 1 9
    right_prev = None
    new_nead = None
    node = head
    while node:
        if index == left_index:
            left = node
        elif index == right_index:
            right = node
            break
        if left is None:
            left_prev = node
        right_prev = node
        index += 1
        node = node.next
    right_prev.next = left
    node = left.next
    left.next = right.next

    # if both the indices are next to each other
    if left_index != right_index:
        right.next = node

    # if the node at first index is head of the original linked list
    if left_prev is None:
        new_head = right
    else:
        left_prev.next = right
        new_head = head
    return new_head


arr = [3, 4, 5, 2, 6, 1, 9]
head = create_linked_list(arr)
left_index = 0
right_index = 6
res = swap_nodes(head, left_index, right_index)
print_linked_list(res)
# output = 3 4 5 6 2 1 9