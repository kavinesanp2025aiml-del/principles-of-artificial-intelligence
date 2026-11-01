import random

N = 8

def conflicts(board, col, row):

    count = 0

    for c in range(N):
        if c == col:
            continue

        r = board[c]

        if r == row or abs(r-row) == abs(c-col):
            count += 1

    return count


def min_conflicts():

    while True:

        board = [random.randint(0, N-1)
                 for _ in range(N)]

        for step in range(10000):

            conflicted = [
                c for c in range(N)
                if conflicts(board, c, board[c]) > 0
            ]

            if not conflicted:
                return board

            col = random.choice(conflicted)

            values = [
                conflicts(board, col, row)
                for row in range(N)
            ]

            minimum = min(values)

            best_rows = [
                r for r in range(N)
                if values[r] == minimum
            ]

            board[col] = random.choice(best_rows)


solution = min_conflicts()

print("Eight Queens Solution:")

for row in range(N):

    for col in range(N):

        if solution[col] == row:
            print("Q", end=" ")
        else:
            print(".", end=" ")

    print()

print("\nSolution Found!")
print("Total Queens:", N)
