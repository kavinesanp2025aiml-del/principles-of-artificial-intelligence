goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            pos = goal.index(state[i])

            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(pos, 3)

            distance += abs(x1-x2) + abs(y1-y2)

    return distance

def neighbors(state):
    result = []
    zero = state.index(0)

    for move in [-3, 3, -1, 1]:
        new = zero + move

        if 0 <= new < 9:
            if move == -1 and zero % 3 == 0:
                continue
            if move == 1 and zero % 3 == 2:
                continue

            temp = list(state)
            temp[zero], temp[new] = temp[new], temp[zero]

            result.append(tuple(temp))

    return result

def search(state, g, bound, path):
    f = g + heuristic(state)

    if f > bound:
        return f

    if state == goal:
        return True

    minimum = float('inf')

    for next_state in neighbors(state):
        if next_state not in path:
            path.append(next_state)

            result = search(
                next_state, g+1, bound, path
            )

            if result is True:
                return True

            minimum = min(minimum, result)
            path.pop()

    return minimum

def ida_star(start):
    bound = heuristic(start)
    path = [start]

    while True:
        result = search(start, 0, bound, path)

        if result is True:
            print("Solution Found:")

            for state in path:
                print(state[:3])
                print(state[3:6])
                print(state[6:])
                print()

            print("Total Moves:", len(path)-1)
            return

        if result == float('inf'):
            print("No solution found")
            return

        bound = result

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

ida_star(start)
