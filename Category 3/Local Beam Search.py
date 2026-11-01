# Delivery Hub Optimization using Local Beam Search
scores = [15, 25, 35, 50, 65,
          80, 75, 70, 85, 95,
          90, 100, 98, 105, 110,
          108, 115, 120, 112, 105]


def local_beam_search(k=3, iterations=5):

    current_states = [2, 6, 10]

    print("Initial states:",
          [state + 1 for state in current_states])

    for step in range(iterations):

        neighbors = []

        for state in current_states:

            left = state - 1
            right = state + 1

            if left >= 0:

                neighbors.append(left)

            if right < len(scores):

                neighbors.append(right)

        neighbors = list(set(neighbors))

        neighbors = sorted(neighbors,
                           key=lambda x: scores[x],
                           reverse=True)

        current_states = neighbors[:k]

        print("\nIteration", step + 1)

        print("Selected states:",
              [state + 1 for state in current_states])

        print("Scores:",
              [scores[state]
               for state in current_states])

    best_state = max(current_states,
                     key=lambda x: scores[x])

    return best_state


best = local_beam_search()

print("\nBest location:", best + 1)

print("Maximum efficiency:", scores[best])
