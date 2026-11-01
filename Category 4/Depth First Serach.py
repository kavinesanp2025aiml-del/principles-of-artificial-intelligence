# Exploring a Maze using Depth First Serach
graph = {
    "Home": ["A", "B"],
    "A": ["C", "D"],
    "B": ["E", "F"],
    "C": [],
    "D": ["G"],
    "E": [],
    "F": [],
    "G": []
}


def dfs(graph, start, goal):

    stack = [start]
    visited = set()

    while stack:

        node = stack.pop()

        if node not in visited:

            print("Visiting:", node)

            visited.add(node)

            if node == goal:
                print("\nGoal Found:", node)
                return

            for neighbor in reversed(graph[node]):
                stack.append(neighbor)

    print("Goal not found")


dfs(graph, "Home", "G")
