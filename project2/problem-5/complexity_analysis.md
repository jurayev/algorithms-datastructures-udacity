
# Blockchain implementation
Adds a new block at O(1) by adding the new block to the tail pointer.

Complexities:
* `Runtime O(1)`
* `Space O(1)`, technically for each new block we have to allocate more memory, 
but since we just add a ref to the new pointer this complexity can be omitted

