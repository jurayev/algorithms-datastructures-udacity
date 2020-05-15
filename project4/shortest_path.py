from heapq import heapify, heappush, heappop
from collections import defaultdict
import math


def shortest_path(M, start, goal):
    frontier = {start}
    explored = set()
    came_from = dict()
    f_costs = get_initial_f_costs(M, start, goal)  # heapq type
    g_costs = get_initial_g_costs(start)  # defaultdict type

    while frontier:
        curr_node = heappop(f_costs)[1]  # cheapest f cost node in the priority queue

        if curr_node == goal:
            path = get_path(came_from, start, goal)
            print(f"path found: start={start}, goal={goal} path={path}")
            return path
        elif curr_node in frontier:
            frontier.remove(curr_node)
            explored.add(curr_node)

            neighbours = M.roads[curr_node]
            for neighbour in neighbours:
                if neighbour not in explored:

                    # since set is a collection of unique elements based on hash tables, this line is equal to
                    # 'if neighbour not in frontier' membership check as both operate at O(1)
                    frontier.add(neighbour)

                    estimated_g_cost = g_costs[curr_node] + distance(M, curr_node, neighbour)

                    # if estimated g cost to the neighbour node is less than neighbour node g cost, update it as for now it is the shortest path
                    if estimated_g_cost < g_costs[neighbour]:
                        g_costs[neighbour] = estimated_g_cost
                        f_cost = get_f_cost(estimated_g_cost, M, neighbour, goal)
                        heappush(f_costs, (f_cost, neighbour))
                        came_from[neighbour] = curr_node   # record the path

    return None


def get_h_cost(M, current, goal):
    return distance(M, current, goal)


def get_f_cost(g_cost, M, current, goal):
    return g_cost + get_h_cost(M, current, goal)


def get_initial_f_costs(M, start, goal):
    f_costs = []
    heapify(f_costs)
    f_cost_start_node = get_f_cost(0, M, start, goal)
    heappush(f_costs, (f_cost_start_node, start))
    return f_costs


def get_initial_g_costs(start):
    g_costs = defaultdict(lambda: math.inf)
    g_costs[start] = 0
    return g_costs


def distance(M, node_1, node_2):
    """Computes the Euclidean L2 Distance."""
    x1, y1 = M.intersections[node_1]
    x2, y2 = M.intersections[node_2]
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))


def get_path(came_from, start, goal):
    """Reconstructs the path using came_from references"""
    path = [goal]
    curr_node = goal
    while curr_node != start:
        curr_node = came_from[curr_node]
        path.append(curr_node)
    path.reverse()
    return path
