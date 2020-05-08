
# Huffman Coding implementation

Considering the overall algorithm complexity analysis, we can state the following worst case complexities:
* Runtime O(n log n)
* Space O(n)

## build_huffman_tree
Complexities: heapq is a binary heap, with O(log n) push and O(log n) pop, however we iterate over heapq item until one element is left
* Runtime O(n log n), where n is the size of the min heap
* Space O(1), because we modify input data in-place

## get_huffman_codes
Complexities:
* Runtime O(n), where n is the size of the tree
* Space O(n), where n is the leaf number of the tree

## encode_data
Complexities:
* Runtime O(n), where n is the input data size
* Space O(n) as the best/average case which is the case of the same input and output size i.e in='000' out='AAA', 
for the worst case depending of the huffman tree depth, we can assume O(2n) O(3n) O(Nn), where n is the input data size

## huffman_decoding
The algorithm requires to traverse the input data traversing the tree one step(node) per char in the input, 
so we assume the following complexities:
* Runtime O(n) as the worst case, where n is the input data size
* Space O(n) as the worst case which is the case of the same input and output size i.e in='000' out='AAA', 
where n is the input data size
