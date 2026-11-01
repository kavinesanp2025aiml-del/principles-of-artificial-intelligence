import heapq

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])

            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_pos, 3)

            distance += abs(x1-x2) + abs(y1-y2)

    return distance

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)

    moves = [-3, 3, -1, 1]

    for move in moves:
        new = zero + move

        if 0 <= new < 9:
            if move == -1 and zero % 3 == 0:
                continue
            if move == 1 and zero % 3 == 2:
                continue

            temp = list(state)
            temp[zero], temp[new] = temp[new], temp[zero]
            neighbors.append(tuple(temp))

    return neighbors

def astar(start):
    pq = [(heuristic(start), 0, start, [start])]
    visited = {}

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            print("Solution Found!")
            for s in path:
                print(s[:3])
                print(s[3:6])
                print(s[6:])
                print()
            print("Total Moves:", g)
            return

        if state in visited and visited[state] <= g:
            continue

        visited[state] = g

        for next_state in get_neighbors(state):
            new_g = g + 1
            new_f = new_g + heuristic(next_state)

            heapq.heappush(
                pq,
                (new_f, new_g, next_state,
                 path + [next_state])
            )

    print("No solution found")

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

astar(start)
