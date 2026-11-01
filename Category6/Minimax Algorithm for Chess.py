def minimax(depth, node, maximizing):
    if depth == 0:
        return node

    if maximizing:
        best = float('-inf')

        for child in node:
            value = minimax(depth - 1, child, False)
            best = max(best, value)

        return best

    else:
        best = float('inf')

        for child in node:
            value = minimax(depth - 1, child, True)
            best = min(best, value)

        return best


# Chess move evaluation tree
chess_tree = [
    [3, 5],
    [2, 9],
    [12, 5]
]

best_score = minimax(2, chess_tree, True)

print("Minimax Chess Algorithm")
print("Best Score:", best_score)
