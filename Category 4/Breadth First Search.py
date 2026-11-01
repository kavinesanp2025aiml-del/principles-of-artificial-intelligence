# Finding the Shortest Route to a Hospital Using BFS
from collections import deque


def bfs(graph, start, goal):

    visited = set()

    queue = deque([(start, [start])])

    while queue:

        current_node, path = queue.popleft()

        if current_node not in visited:

            visited.add(current_node)

            print("Visiting:", current_node)

            if current_node == goal:

                return path

            for neighbor in graph[current_node]:

                if neighbor not in visited:

                    queue.append(
                        (neighbor, path + [neighbor]))

    return None


graph = {

    "Home": ["Mall", "School"],

    "Mall": ["Park", "Market"],

    "School": ["Office"],

    "Park": ["Hospital"],

    "Market": ["Hospital"],

    "Office": [],

    "Hospital": []

}


start = "Home"

goal = "Hospital"

result = bfs(graph, start, goal)

print("\nShortest Path:")

print(" -> ".join(result))
