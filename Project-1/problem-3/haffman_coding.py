import sys
from heapq import heapify, heappush, heappop
from collections import Counter


"""
Considering the overall algorithm complexity analysis, we can state the following worst case complexities:
~ Runtime O(n log n)
~ Space O(n)
"""


class Node:

    def __init__(self, value, frequency):
        self.value = value
        self.frequency = frequency
        self.left_child = None
        self.right_child = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def huffman_encoding(data):
    if not data or not isinstance(data, str):
        return "", None
    nodes_heap = []
    heapify(nodes_heap)
    # create and sort out leaf nodes
    balanced_chars = Counter(data)               # Runtime O(n)
    for char, freq in balanced_chars.items():    # Runtime O(n) plus O(log n) for heappush operation, falls into O(nlogn)
        heappush(nodes_heap, Node(char, freq))
    # build a huffman tree
    tree = build_huffman_tree(nodes_heap)
    # traverse the huffman tree and generate binary codes
    codes = get_huffman_codes(tree)
    encoded_data = encode_data(data, codes)
    return encoded_data, tree


"""
Complexities: heapq is a binary heap, with O(log n) push and O(log n) pop, however we iterate over heapq item until one element is left
~ Runtime O(n log n), where n is the size of the min heap
~ Space O(1), because we modify input data in-place
"""
def build_huffman_tree(nodes_heap):
    while len(nodes_heap) > 1:
        node_one = heappop(nodes_heap)
        node_two = heappop(nodes_heap)
        internal_node = Node(None, node_one.frequency + node_two.frequency)
        if node_one < node_two:
            internal_node.left_child = node_one
            internal_node.right_child = node_two
        else:
            internal_node.left_child = node_two
            internal_node.right_child = node_one
        # push internal node back to the heap
        heappush(nodes_heap, internal_node)
    return nodes_heap[0]


"""
Complexities:
~ Runtime O(n), where n is the size of the tree
~ Space O(n), where n is the leaf number of the tree
"""
def get_huffman_codes(tree):

    def traverse(node, code):
        if node.left_child:
            traverse(node.left_child, code + "0")
            traverse(node.right_child, code + "1")
        else:
            codes[node.value] = code

    codes = {}
    if not tree:
        return codes
    root_code = ""
    if not tree.left_child:
        root_code = "0"
    traverse(tree, root_code)
    return codes


"""
Complexities:
~ Runtime O(n), where n is the input data size
~ Space O(n) as the best/average case which is the case of the same input and output size i.e in='000' out='AAA', 
for the worst case depending of the huffman tree depth, we can assume O(2n) O(3n) O(Nn), where n is the input data size
"""
def encode_data(data, binary_codes):
    encoded = ""
    for char in data:
        encoded += binary_codes[char]
    return encoded


"""
The algorithm requires to traverse the input data traversing the tree one step(node) per char in the input, 
so we assume the following complexities:
~ Runtime O(n) as the worst case, where n is the input data size
~ Space O(n) as the worst case which is the case of the same input and output size i.e in='000' out='AAA', 
where n is the input data size
"""
def huffman_decoding(data, tree):
    if not data or not tree:
        return ""
    decoded = ""
    node = tree
    for char in data:
        if node.left_child and char == "0":
            node = node.left_child
            # if current node doesn't have a child, record its value and reset a tree head
            if not node.left_child:
                decoded += node.value
                node = tree
        elif node.right_child:
            node = node.right_child
            if not node.right_child:
                decoded += node.value
                node = tree
        else:
            decoded += node.value
    return decoded


def helper_test_function(data):
    print("TEST LOGS\n")
    initial_data_size = sys.getsizeof(data)
    print(f"The size of the data is: {initial_data_size}")
    print(f"The content of the data is: {data}")

    encoded_data, tree = huffman_encoding(data)
    binary_code_size = sys.getsizeof(int(encoded_data, base=2))
    print(f"The size of the encoded data is: {binary_code_size}")
    print(f"The content of the encoded data is: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)
    decoded_data_size = sys.getsizeof(decoded_data)
    print(f"The size of the decoded data is: {decoded_data_size}")
    print(f"The content of the decoded data is: {decoded_data}")

    assert data == decoded_data                    # assert no data loss
    assert initial_data_size == decoded_data_size  # assert no size loss
    assert initial_data_size > binary_code_size    # assert compression algorithm works

def _test_valid_sentence():
    data = "The bird is the word"
    helper_test_function(data)
    print("\n_test_valid_sentence PASSED\n")

def _test_alphanumeric():
    data = "!@#$%^&*()_+ QAZ~<>?|1234 00"
    helper_test_function(data)
    print("\n_test_alphanumeric PASSED\n")

def _test_same_chars():
    data = "AA"
    helper_test_function(data)
    print("\n_test_same_chars PASSED\n")

def _test_single_char():
    data_one = "A"
    helper_test_function(data_one)
    data_two = " "
    helper_test_function(data_two)
    print("\n_test_single_char PASSED\n")

def _test_empty_input_throws_no_errors():
    data = ""
    initial_data_size = sys.getsizeof(data)
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)
    decoded_data_size = sys.getsizeof(decoded_data)
    assert data == decoded_data                    # assert no data loss
    assert initial_data_size == decoded_data_size  # assert no size loss
    print("\n_test_empty_input_throws_no_errors PASSED\n")

def _test_invalid_input_throws_no_errors():
    data = 1234
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert "" == decoded_data  # assert no data loss
    print("\n_test_invalid_input_throws_no_errors PASSED\n")


print("-"*10, "BEGIN TESTING", "-"*10)
_test_valid_sentence()
_test_alphanumeric()
_test_same_chars()
_test_single_char()
_test_empty_input_throws_no_errors()
_test_invalid_input_throws_no_errors()
print("-"*10, "ALL TESTS PASSED", "-"*10)