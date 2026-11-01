pruned = 0

def alpha_beta(depth, node, alpha, beta, maximizing):

    global pruned

    if depth == 0:
        return node

    if maximizing:
        best = float('-inf')

        for child in node:
            value = alpha_beta(
                depth - 1, child,
                alpha, beta, False
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                pruned += 1
                break

        return best

    else:
        best = float('inf')

        for child in node:
            value = alpha_beta(
                depth - 1, child,
                alpha, beta, True
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                pruned += 1
                break

        return best


chess_tree = [
    [3, 5],
    [2, 9],
    [12, 5]
]

result = alpha_beta(
    2, chess_tree,
    float('-inf'),
    float('inf'),
    True
)

print("Alpha-Beta Pruning Chess")
print("Best Score:", result)
print("Pruned Branches:", pruned)
