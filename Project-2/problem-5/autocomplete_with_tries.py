from collections import defaultdict


"""
For this problem I used a default dict data structure as it reduces necessary dict membership checks and improves insert operation performance, 
iterative traverse for find() and insert() functions, recursive traverse for suffixes() function

Complexities:
* Runtime O(nm)
* Space O(n)

See some complexity explanation down below
"""


""" Represents a single node in the Trie """
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

    """
    Complexity analysis:
    * Runtime O(nm), assuming 'n' is the number of nodes in the trie and 'm' is the number of nodes each node has.
    * Space (n), where 'n' is the number of suffixes the trie node has.
    """
    def suffixes(self, suffix=''):
        """ Get all suffixes of the TrieNode """
        def traverse(node, suffix):
            suffixes = []
            if not node.keys():
                return suffixes

            for key in node.keys():
                sub_suffix = suffix + key
                if node[key].is_word:
                    suffixes.append(sub_suffix)
                suffixes += traverse(node[key].children, sub_suffix)

            return suffixes

        return traverse(self.children, suffix)


class Trie:
    def __init__(self):
        """ Initialize this Trie (add a root node) """
        self.root = TrieNode()

    """
    * Runtime O(n), where n is the size of input word
    * Space O(n), where n is the size of input word used to produce trie datastructure
    """
    def insert(self, word):
        """ Add a word to the Trie """
        curr_node = self.root
        for char in word:
            curr_node = curr_node.children[char]
        curr_node.is_word = True

    """
    * Runtime O(n), where n is the size of input prefix to traverse
    * Space O(1), no additional memory is used
    """
    def find(self, prefix):
        """ Find the Trie node that represents this prefix """
        curr_node = self.root
        for char in prefix:
            if char not in curr_node.children:
                return None
            curr_node = curr_node.children[char]
        return curr_node


def _test_autocomplete(prefix, expected_suffixes):
    print(">"*10, "Start _test_autocomplete", "<"*10, "\n")
    MyTrie = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in wordList:
        MyTrie.insert(word)

    prefix_node = MyTrie.find(prefix)
    actual_suffixes = prefix_node.suffixes()
    print(f"Actual: {actual_suffixes}")
    print(f"Expected: {expected_suffixes}")
    assert expected_suffixes == actual_suffixes
    print("TEST PASSED\n")


print("-"*10, "BEGIN TESTING", "-"*10, "\n")
_test_autocomplete('ant', ["hology", "agonist", "onym"])
_test_autocomplete('f', ["un", "unction", "actory"])
_test_autocomplete('tripod', [])
_test_autocomplete('', [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ])
print("-"*10, "ALL TESTS PASSED", "-"*10)
