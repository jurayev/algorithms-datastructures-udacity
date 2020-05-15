
# Autocomplete with Tries implementation analysis

For this problem I used a default dict data structure as it reduces necessary dict membership checks and improves insert operation performance, 
iterative traverse for find() and insert() functions, recursive traverse for suffixes() function

Complexities:
* `Runtime O(nm)`
* `Space O(n)`

See some complexity explanation down below

## TrieNode.suffixes

Complexity analysis:
* `Runtime O(nm)`, assuming 'n' is the number of nodes in the trie and 'm' is the number of nodes each node has.
* `Space (n)`, where 'n' is the number of suffixes the trie node has.
 
## Trie.insert

Complexity analysis:
* `Runtime O(n)`, where n is the size of input word
* `Space O(n)`, where n is the size of input word used to produce trie datastructure

## Trie.find

Complexity analysis:
* `Runtime O(n)`, where n is the size of input prefix to traverse
* `Space O(1)`, no additional memory is used