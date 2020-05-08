
# LRU cache implementation
As the base the ordered dict data structure is used. ordered dict is build using HashTable and LinkedList
and provides Get, Set, Delete operations at O(1) Runtime complexity

Complexity analysis:
* Runtime O(1), for both get(key) and set(key, value) operations. _move_front() is O(1) as it uses OrderedDict.move_to_end() under the hood
* Space O(n), where n is the cache capacity
