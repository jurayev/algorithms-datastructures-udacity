from heapq import heappush, heappop, heapify


def create_graph(num_islands, bridge_config):
    graph = [[] for _ in range(num_islands+1)]
    for config in bridge_config:
        bridge_a = config[0]
        bridge_b = config[1]
        distance = config[2]
        graph[bridge_a].append((bridge_b, distance))
        graph[bridge_b].append((bridge_a, distance))
    return graph


def minimum_cost(islands):
    min_cost = 0
    start_island = 1
    unvisited = [(0, start_island)]
    heapify(unvisited)
    visited = set()

    while unvisited:
        cost, current_island = heappop(unvisited)
        if current_island in visited:
            continue
        visited.add(current_island)
        min_cost += cost

        for bridge, bridge_cost in islands[current_island]:
            heappush(unvisited, (bridge_cost, bridge))

    return min_cost


"""
Complexities:
 * Runtime O(E + V), where E is edges, V is vertices. We should traverse all edges and its vertices in the worst case scenario
 * Space O(E + V)
"""
def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the problem statement
    return: cost (int) minimum cost of connecting all islands
    """
    islands = create_graph(num_islands, bridge_config)
    return minimum_cost(islands)


def _test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)

    if output == solution:
        print("Pass")
    else:
        print("Fail")

num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
_test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
_test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

test_case = [num_islands, bridge_config, solution]
_test_function(test_case)
