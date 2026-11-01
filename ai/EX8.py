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

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == p:
            return True
    return False

def minimax(ai_turn):
    if winner("O"):
        return 1
    if winner("X"):
        return -1
    if " " not in board:
        return 0

    if ai_turn:
        best = -2
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                if score > best:
                    best = score
        return best
    else:
        best = 2
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                if score < best:
                    best = score
        return best

def ai_move():
    best_score = -2
    best_move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"
    print("AI plays position", best_move + 1)

def main():
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

if __name__ == "__main__":
    main()
