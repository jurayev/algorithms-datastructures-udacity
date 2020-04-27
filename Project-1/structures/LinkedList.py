class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        if not self.head:
            self.head = Node(value)
        else:
            new_head = Node(value)
            new_head.next = self.head
            self.head = new_head

    def append(self, value):
        """ Append a value to the end of the list. """
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def remove(self, value):
        """ Remove first occurrence of value. """
        if not self.head:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            else:
                current = current.next
        raise ValueError("Value not found in the list.")

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        value = self.head.value
        self.remove(value)
        return value

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        if pos > self.size():
            self.append(value)
            return
        if pos == 0:
            self.prepend(value)
            return

        current = self.head
        index = 1
        while current.next:
            if pos == index:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            index += 1

    def size(self):
        """ Return the size or length of the linked list. """
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


def iscircular(llist):
    """
    Determine whether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """
    if not llist.head:
        return False

    slow = llist.head
    fast = llist.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    llist = LinkedList()
    values = [_ for _ in linked_list]
    for v in reversed(values):
        llist.append(v)
    print(llist)
    return llist

# Test prepend
print("# Test prepend")
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append

print("# Test append")
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
print("# Test search")
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
print("# Test remove")
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
print("# Test pop")
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert
print("# Test insert")
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size
print("# Test size")
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"