
# HTTPRouter using a Trie implementation analysis

For this problem I used a default dict data structure as it reduces necessary dict membership checks and improves insert operation performance.
iterative traverse for find() and insert() functions, recursive traverse for suffixes() function

Complexity analysis:
* `Runtime O(n)`, assuming 'n' is the number of nodes in the trie
* `Space (n)`, assuming 'n' is the number of nodes in the trie


## Router.add_handler
Iterates over each dir in route and add a handler at the leaf node.

Complexities:
* `Runtime O(n)`, assuming 'n' is the number of dirs in the path
* `Space (n)`, assuming 'n' is the number of dirs in the path


## Router.lookup
Iterates over each dir in route and return a handler.

Complexities:
* `Runtime O(n)`, assuming 'n' is the number of dirs in the path
* `Space (n)`, assuming 'n' is the number of dirs in the path


## Router.split_path
Iterates over each dir in route and return dir names as a list.

Complexities:
* `Runtime O(n)`, assuming 'n' is the number of dirs in the path
* `Space (n)`, assuming 'n' is the number of dirs in the path