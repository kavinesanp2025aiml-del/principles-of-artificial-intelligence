def check_winner(board):

    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c]:
            if board[a] == 'X':
                return 10
            elif board[a] == 'O':
                return -10

    if ' ' not in board:
        return 0

    return None


def minimax(board, maximizing):

    score = check_winner(board)

    if score is not None:
        return score

    if maximizing:
        best = float('-inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                value = minimax(board, False)
                board[i] = ' '
                best = max(best, value)

        return best

    else:
        best = float('inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                value = minimax(board, True)
                board[i] = ' '
                best = min(best, value)

        return best


def best_move(board):

    best = float('-inf')
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            value = minimax(board, False)
            board[i] = ' '

            if value > best:
                best = value
                move = i

    return move


board = [
    'X', 'O', 'X',
    'O', 'X', ' ',
    ' ', ' ', 'O'
]

print("Tic-Tac-Toe Board:")

for i in range(0, 9, 3):
    print(board[i], "|", board[i+1], "|", board[i+2])

move = best_move(board)

if move != -1:
    board[move] = 'X'

print("\nBest Move:", move + 1)

print("\nUpdated Board:")

for i in range(0, 9, 3):
    print(board[i], "|", board[i+1], "|", board[i+2])
