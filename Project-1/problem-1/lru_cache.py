from collections import OrderedDict

"""
LRU cache implementation
As the base the ordered dict data structure is used. ordered dict is build using HashTable and LinkedList
and provides Get, Set, Delete operations at O(1) Runtime complexity

Complexity analysis:
Runtime O(1), for both get(key) and set(key, value) operations. _move_front() is O(1) as it uses OrderedDict.move_to_end() under the hood
Space O(n), where n is the cache capacity
"""
class LRU_Cache(object):

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        value = self.cache.get(key)
        if value:
            self._move_front(key)
            return value
        return -1

    def set(self, key, value):
        if key in self.cache: # if the key in the cache, move to the front, later update the value
            self._move_front(key)
        else:
            if self._is_full_capacity():  # if overflow
                self.cache.popitem(last=False)  # remove the least recently used from the HEAD with last=False flag
        self.cache[key] = value  # Adds a new pair to the TAIL

    def _is_full_capacity(self):
        return len(self.cache) == self.capacity

    def _move_front(self, key):
        self.cache.move_to_end(key, last=True)  # with last=False flag the specified key is moved to the TAIL


def _test_get_present_item():
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    assert our_cache.get(1) == 1       # returns 1
    assert our_cache.get(4) == 4       # returns 4
    print("_test_get_present_item PASSED\n")


def _test_get_not_present_item():
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    assert our_cache.get(9) == -1  # returns -1 because 9 is not present in the cache
    assert our_cache.get(0) == -1  # returns -1 because 0 is not present in the cache
    print("_test_get_not_present_item PASSED\n")


def _test_overflow_capacity():
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, 5)
    our_cache.set(6, 6)

    assert our_cache.get(1) == -1  # returns -1 because 1 was removed at the time of cache overflow
    assert our_cache.get(6) == 6  # not important, but double check for correctness
    assert len(our_cache.cache) == 5  # expected sized is 5
    print("_test_overflow_capacity PASSED\n")


def _test_move_front():
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, 5)
    # expected order H -> 1 -> 2 -> 3 -> 4 -> 5 -> T
    our_cache.get(1)  # move 1:1 to the TAIL. 2:2 now at the HEAD(least recently used)
    # expected order H -> 2 -> 3 -> 4 -> 5 -> 1 -> T
    our_cache.get(2)  # move 2:2 to the TAIL. 3:3 now at the HEAD(least recently used)
    # expected order H -> 3 -> 4 -> 5 -> 1 -> 2 -> T
    our_cache.set(6, 6)  # added to the TAIL. 3:3 is removed from the HEAD
    # expected order H -> 4 -> 5 -> 1 -> 2 -> 6 -> T
    assert our_cache.get(3) == -1  # returns -1 as the key was removed from the cache
    assert our_cache.get(2) == 2
    print("_test_move_front PASSED\n")


def _test_update_present_key():
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(3, 1)  # this should not increase the size

    assert our_cache.get(3) == 1  # returns 1 as the key was updated
    assert len(our_cache.cache) == 4  # expected sized is 4
    print("_test_update_present_key PASSED\n")


def _test_larger_capacity():
    our_cache = LRU_Cache(15)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    our_cache.set(7, 7)
    our_cache.set(8, 8)
    our_cache.set(9, 9)
    our_cache.set(10, 10)
    our_cache.set(11, 11)
    our_cache.set(12, 12)
    our_cache.set(13, 13)
    our_cache.set(14, 14)
    our_cache.set(15, 15)

    assert len(our_cache.cache) == 15  # expected sized is 15

    our_cache.set(99, 99)

    assert len(our_cache.cache) == 15  # expected sized is 15
    assert our_cache.get(1) == -1  # expected -1 as it was removed from the cache by the last update operation
    print("_test_larger_capacity PASSED\n")


print("-"*10, "BEGIN TESTING", "-"*10)
_test_get_not_present_item()
_test_get_present_item()
_test_overflow_capacity()
_test_move_front()
_test_update_present_key()
_test_larger_capacity()
print("-"*10, "ALL TESTS PASSED", "-"*10)