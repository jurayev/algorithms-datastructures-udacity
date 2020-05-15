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


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    print_linked_list(head)
    if not head:
        return head

    odd = None
    even = None
    odd_tail = None
    even_tail = None

    while head:
        next_node = head.next
        if head.data % 2 == 0:
            if not even:
                even = head
                even_tail = even
            else:
                even_tail.next = head
                even_tail = even_tail.next
        else:
            if not odd:
                odd = head
                odd_tail = odd
            else:
                odd_tail.next = head
                odd_tail = odd_tail.next
        head.next = None
        head = next_node

    if not odd:
        return even
    odd_tail.next = even
    return odd

arr = [2, 4, 6, 5]
res = even_after_odd(create_linked_list(arr))
print_linked_list(res)



