
N = 4

def isSafe(board, row, col):
    for j in range(col):
        if board[row][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve(board, col):
    if col == N:
        return True

    for row in range(N):
        if isSafe(board, row, col):
            board[row][col] = 1

            if solve(board, col + 1):
                return True

            board[row][col] = 0

    return False

board = [[0] * N for _ in range(N)]

if solve(board, 0):
    print("Solution:")
    for row in board:
        print(*row)
else:
    print("Solution does not exist")
