N = int(input("Enter N: "))

def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row + 1
    j = col - 1
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve(board):
    row = [0] * N
    col = 0

    while col < N:
        if row[col] == N:
            row[col] = 0
            col -= 1

            if col < 0:
                return False

            board[row[col]][col] = 0
            row[col] += 1

        elif isSafe(board, row[col], col):
            board[row[col]][col] = 1
            col += 1

        else:
            row[col] += 1

    return True

def main():
    board = [[0] * N for i in range(N)]

    if solve(board):
        for r in board:
            print(r)
    else:
        print("No solution")
    for i in range(N):
         for j in range(N):
             if board[i][j] == 1:
                  print("Queen at:", (i, j))

if __name__ == "__main__":
    main()
