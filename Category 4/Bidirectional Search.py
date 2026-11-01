# Travel from Home to College using Bidirectional Search
graph = {
    'Home': ['Bus Stop'],

    'Bus Stop': ['Home', 'Coffee Shop', 'Library'],

    'Coffee Shop': ['Bus Stop', 'Junction'],

    'Library': ['Bus Stop', 'Junction'],

    'Junction': ['Coffee Shop',
                 'Library',
                 'Railway Station'],

    'Railway Station': ['Junction', 'College'],

    'College': ['Railway Station']
}
from collections import deque


def bidirectional_search(graph, start, goal):

    if start == goal:
        return [start]

    forward_queue = deque([start])
    backward_queue = deque([goal])

    forward_visited = {start}
    backward_visited = {goal}

    forward_parent = {start: None}
    backward_parent = {goal: None}

    while forward_queue and backward_queue:

        # Forward Search

        current_forward = forward_queue.popleft()

        for neighbor in graph[current_forward]:

            if neighbor not in forward_visited:

                forward_visited.add(neighbor)

                forward_parent[neighbor] = current_forward

                forward_queue.append(neighbor)

                if neighbor in backward_visited:

                    return build_path(
                        neighbor,
                        forward_parent,
                        backward_parent
                    )

        # Backward Search

        current_backward = backward_queue.popleft()

        for neighbor in graph[current_backward]:

            if neighbor not in backward_visited:

                backward_visited.add(neighbor)

                backward_parent[neighbor] = current_backward

                backward_queue.append(neighbor)

                if neighbor in forward_visited:

                    return build_path(
                        neighbor,
                        forward_parent,
                        backward_parent
                    )

    return None


def build_path(meeting_node,
               forward_parent,
               backward_parent):

    path = []

    node = meeting_node

    while node is not None:

        path.append(node)

        node = forward_parent[node]

    path.reverse()

    node = backward_parent[meeting_node]

    while node is not None:

        path.append(node)

        node = backward_parent[node]

    return path


graph = {
    'Home': ['Bus Stop'],

    'Bus Stop': ['Home',
                 'Coffee Shop',
                 'Library'],

    'Coffee Shop': ['Bus Stop',
                    'Junction'],

    'Library': ['Bus Stop',
                'Junction'],

    'Junction': ['Coffee Shop',
                 'Library',
                 'Railway Station'],

    'Railway Station': ['Junction',
                        'College'],

    'College': ['Railway Station']
}

start = "Home"
goal = "College"

path = bidirectional_search(
    graph,
    start,
    goal
)

print("Path Found:")

print(" → ".join(path))
