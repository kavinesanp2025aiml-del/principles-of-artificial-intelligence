coverage = [10, 20, 35, 50, 65,
            80, 75, 70, 85, 90,
            88, 95, 100, 92, 85]


def hill_climbing(start):

    current = start

    path = [current]

    while True:

        current_score = coverage[current]

        left = current - 1

        right = current + 1

        best_state = current

        best_score = current_score

        if left >= 0:

            if coverage[left] > best_score:

                best_state = left

                best_score = coverage[left]

        if right < len(coverage):

            if coverage[right] > best_score:

                best_state = right

                best_score = coverage[right]

        if best_state == current:

            break

        current = best_state

        path.append(current)

    return current, coverage[current], path


state, score, path = hill_climbing(5)

print("Best location:", state + 1)

print("Coverage score:", score)

print("Path:", [x + 1 for x in path])
