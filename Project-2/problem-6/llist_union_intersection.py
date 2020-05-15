class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def __eq__(self, other):
        node_1 = self.head
        node_2 = other.head
        while node_1:
            if node_1.value != node_2.value:
                return False
            node_1 = node_1.next
            node_2 = node_2.next
        return True

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next


"""
Complexity analysis for union opearation based on iteration through each node of the llist_1
for the each node in the llist_2. 
~ Runtime O(nm), assuming 'n' is the size of the llist_1 and 'm' is the size of the llist_2
~ Space O(nm), assuming 'n' is the size of the llist_1 and 'm' is the size of the llist_2, 
then for the worst case when llist_1 and llist_2 are completely different, we require a new linked list 'nm' sized
"""
def union(llist_1, llist_2):
    if not llist_1.head:
        return llist_2
    if not llist_2.head:
        return llist_1

    node_1 = llist_1.head
    node_2 = llist_2.head
    while node_1:
        prev = llist_2.head
        while node_2:
            if node_1.value == node_2.value:
                if prev.value == node_2.value:
                    llist_2.head = node_2.next
                else:
                    prev.next = node_2.next
                break
            else:
                prev = node_2
                node_2 = node_2.next
        node_2 = llist_2.head
        node_1 = node_1.next

    # assign
    new_llist = LinkedList()
    new_llist.head = llist_1.head
    new_llist.tail = llist_1.tail
    new_llist.tail.next = llist_2.head
    return new_llist


"""
Complexity analysis is quite straight forward since we iterate through each node of the llist_1
for the each node in the llist_2. 
~ Runtime O(nm), assuming 'n' is the size of the llist_1 and 'm' is the size of the llist_2
~ Space O(n), assuming 'n' is the size of the llist_1 and 'n' is the size of the llist_2, 
then for the worst case when llist_1 and llist_2 are the same, we require a new linked list 'n' sized
"""
def intersection(llist_1, llist_2):
    if not llist_1.head or not llist_2.head:
        return LinkedList()

    node_1 = llist_1.head
    node_2 = llist_2.head
    new_llist = LinkedList()
    new_node = None
    while node_1:
        while node_2:
            if node_1.value == node_2.value:
                if not new_node:
                    new_llist.head = Node(node_1.value)
                    new_llist.tail = new_llist.head
                    new_node = new_llist.head
                else:
                    new_node.next = Node(node_1.value)
                    new_llist.tail = new_node.next
                    new_node = new_node.next
                break
            node_2 = node_2.next
        node_1 = node_1.next
        node_2 = llist_2.head

    return new_llist


def _test_union(input, expected):
    print(">"*10, "Start _test_union", "<"*10)
    llist_1 = LinkedList()
    llist_2 = LinkedList()
    expected_ll_list = LinkedList()

    for i in input[0]:
        llist_1.append(i)

    for i in input[1]:
        llist_2.append(i)

    for i in expected:
        expected_ll_list.append(i)

    llist_union = union(llist_1, llist_2)
    print(f"Actual: {llist_union}")
    print(f"Expected: {expected_ll_list}")
    assert expected_ll_list == llist_union
    print("TEST PASSED\n")

def _test_intersection(input, expected):
    print(">"*10, "Start _test_intersection", "<"*10)
    llist_1 = LinkedList()
    llist_2 = LinkedList()
    expected_ll_list = LinkedList()

    for i in input[0]:
        llist_1.append(i)

    for i in input[1]:
        llist_2.append(i)

    for i in expected:
        expected_ll_list.append(i)

    llist_union = intersection(llist_1, llist_2)
    print(f"Actual: {llist_union}")
    print(f"Expected: {expected_ll_list}")
    assert expected_ll_list == llist_union
    print("TEST PASSED\n")

# test base cases
# 1
_test_union([[3, 2, 4, 35, 6, 65, 6, 4, 3, 21], [6, 32, 4, 9, 6, 1, 11, 21, 1]], [3, 2, 4, 35, 6, 65, 6, 4, 3, 21, 32, 9, 1, 11, 1])
_test_intersection([[3, 2, 4, 35, 6, 65, 6, 4, 3, 21], [6, 32, 4, 9, 6, 1, 11, 21, 1]], [4, 6, 6, 4, 21])
# 2
_test_union([[3, 2, 4, 35, 6, 65, 6, 4, 3, 23], [1, 7, 8, 9, 11, 21, 1]], [3, 2, 4, 35, 6, 65, 6, 4, 3, 23, 1, 7, 8, 9, 11, 21, 1])
_test_intersection([[3, 2, 4, 35, 6, 65, 6, 4, 3, 23], [1, 7, 8, 9, 11, 21, 1]], [])

# test cases the same linked list
_test_union([[1, 2, 4, 5, 3, 3], [1, 2, 4, 5, 3, 3]], [1, 2, 4, 5, 3, 3])
_test_intersection([[1, 2, 4, 5, 3, 3], [1, 2, 4, 5, 3, 3]], [1, 2, 4, 5, 3, 3])

# test cases head and tail element are handled properly
_test_union([[1, 2, 4, 5, 3, 3], [1, 6, 7, 8, 9, 1]], [1, 2, 4, 5, 3, 3, 6, 7, 8, 9, 1])
_test_intersection([[1, 2, 4, 5, 3, 3], [11, 6, 7, 8, 9, 1]], [1])

# test cases with single element in each linked list
# 1
_test_union([[1], [1]], [1])
_test_intersection([[1], [1]], [1])
# 2
_test_union([[1], [2]], [1, 2])
_test_intersection([[1], [2]], [])

# test cases with empty linked list
# 1
_test_union([[0], []], [0])
_test_intersection([[0], []], [])
# 2
_test_union([[], [0]], [0])
_test_intersection([[], [0]], [])
# 3
_test_union([[], []], [])
_test_intersection([[], []], [])
