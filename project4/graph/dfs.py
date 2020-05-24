class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)

    def dfs_recursion(self, start_node):

        def dfs_recursion(node, visited):

            if not node:
                return False

            visited[node.value] = True
            print(node.value)

            for each in node.children:
                if each.value not in visited:
                    dfs_recursion(each, visited)

        visited = {}
        dfs_recursion(start_node, visited)

    def dfs_iteratively(self, root_node, search_value):
        unvisited = [root_node]
        visited = []
        while unvisited:
            node = unvisited.pop()
            visited.append(node)
            if node.value == search_value:
                return node
            for n in node.children:
                if n not in visited:
                    unvisited.append(n)
        return None


nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] )
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)

assert nodeA == graph1.dfs_iteratively(nodeS, 'A')
assert nodeS == graph1.dfs_iteratively(nodeP, 'S')
assert nodeR == graph1.dfs_iteratively(nodeH, 'R')
