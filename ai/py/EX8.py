
board = [" "] * 9

def show():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--|---|--")

def winner(p):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(all(board[i] == p for i in w) for w in wins)

def minimax(is_max):
    if winner("O"):
        return 1
    if winner("X"):
        return -1
    if " " not in board:
        return 0

    best = -2 if is_max else 2

    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if is_max else "X"
            score = minimax(not is_max)
            board[i] = " "

            if is_max:
                best = max(best, score)
            else:
                best = min(best, score)

    return best

def ai_move():
    best = -2
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best:
                best = score
                move = i

    board[move] = "O"

while True:
    show()
    pos = int(input("Enter position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid move!")
        continue

    board[pos] = "X"

    if winner("X"):
        show()
        print("You Win!")
        break

    if " " not in board:
        show()
        print("Draw!")
        break

    ai_move()

    if winner("O"):
        show()
        print("AI Wins!")
        break

    if " " not in board:
        show()
        print("Draw!")
        break
