import heapq

def heuristic(state):
    m, c, b = state
    return m + c

def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    mr, cr = 3 - m, 3 - c

    if m > 0 and m < c:
        return False
    if mr > 0 and mr < cr:
        return False

    return True

def greedy_bfs():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    pq = [(heuristic(start), start, [start])]
    visited = set()

    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]

    while pq:
        _, state, path = heapq.heappop(pq)

        if state == goal:
            print("Solution Found:")
            for s in path:
                print(s)
            return

        if state in visited:
            continue

        visited.add(state)

        m, c, boat = state

        for dm, dc in moves:
            if boat == 0:
                new_state = (m-dm, c-dc, 1)
            else:
                new_state = (m+dm, c+dc, 0)

            if valid(new_state[0], new_state[1]):
                if new_state not in visited:
                    heapq.heappush(
                        pq,
                        (heuristic(new_state),
                         new_state,
                         path + [new_state])
                    )

    print("No solution found")

greedy_bfs()
