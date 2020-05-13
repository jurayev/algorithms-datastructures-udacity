from collections import defaultdict


"""
For this problem I used a default dict data structure as it reduces necessary dict membership checks and improves insert operation performance.
iterative traverse for find() and insert() functions, recursive traverse for suffixes() function


Complexity analysis:
* Runtime O(n), assuming 'n' is the number of nodes in the trie
* Space (n), assuming 'n' is the number of nodes in the trie
"""


class RouteTrieNode:
    """ A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler. """
    def __init__(self, handler=None):
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler

    def set_handler(self, name):
        self.handler = name


class RouteTrie:
    """ A RouteTrie will store our routes and their associated handlers """
    def __init__(self, handler):
        self.root = RouteTrieNode(handler)

    def insert(self, route, handler_name):
        node = self.root
        for dir in route:
            node = node.children[dir]
        node.set_handler(handler_name)

    def find(self, route):
        node = self.root
        for dir in route:
            if dir not in node.children:
                return None
            node = node.children[dir]
        return node.handler


class Router:
    """ The Router class will wrap the Trie and handle """
    def __init__(self, root_handler, not_found_handler):
        self.router = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler_name):
        dirs = self.split_path(path)
        self.router.insert(dirs, handler_name)

    def lookup(self, path):
        dirs = self.split_path(path)
        found_handler = self.router.find(dirs)
        if not found_handler:
            return self.not_found_handler
        return found_handler

    def split_path(self, path):
        dirs = [dir for dir in path.split("/") if dir]
        return dirs


def _test_base_scenario():
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    assert router.lookup("/") == "root handler"
    assert router.lookup("/home") == "not found handler"
    assert router.lookup("/home/about") == "about handler"
    assert router.lookup("/home/about/") == "about handler"
    assert router.lookup("/home/about/me") == "not found handler"
    print("TEST PASSED _test_base_scenario\n")


def _test_each_dir_has_handler():
    router = Router("root handler", "not found handler")
    router.add_handler("/home/", "home handler")
    router.add_handler("/home/about", "about handler")
    router.add_handler("home/about/me", "about me handler")

    assert router.lookup("") == "root handler"
    assert router.lookup("/home/") == "home handler"
    assert router.lookup("home/about") == "about handler"
    assert router.lookup("/home/about/me") == "about me handler"
    print("TEST PASSED _test_each_dir_has_handler\n")


def _test_multi_route_router():
    router = Router("root handler", "not found handler")
    router.add_handler("/home/", "home page handler")
    router.add_handler("/home/pricing/for_you", "pricing for you page handler")
    router.add_handler("/home/pricing/for_business", "pricing for business page handler")
    router.add_handler("/home/offers/offer_1", "offer 1 page handler")
    router.add_handler("/home/offers/offer_2", "offer 2 page handler")
    router.add_handler("/home/offers/offer_3", "offer 3 page handler")
    router.add_handler("/home/about", "about page handler")
    router.add_handler("home/about/me", "about me page handler")
    router.add_handler("home/about/services", "about services page handler")
    router.add_handler("home/about/services/personal", "about personal services page handler")
    router.add_handler("home/about/services/corporate", "about corporate services page handler")

    assert router.lookup("") == "root handler"
    assert router.lookup("/home/") == "home page handler"
    assert router.lookup("home/about") == "about page handler"
    assert router.lookup("/home/about/me") == "about me page handler"
    assert router.lookup("/home/about/services/") == "about services page handler"
    assert router.lookup("home/about/services/corporate/") == "about corporate services page handler"
    assert router.lookup("/home/offers/offer_2") == "offer 2 page handler"
    assert router.lookup("/home/pricing/for_business") == "pricing for business page handler"
    print("TEST PASSED _test_multi_route_router\n")


print("-"*10, "BEGIN TESTING", "-"*10, "\n")
_test_base_scenario()
_test_each_dir_has_handler()
_test_multi_route_router()
print("\n", "-"*10, "ALL TESTS PASSED", "-"*10)