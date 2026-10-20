
#include <iostream>
#include <algorithm>
using namespace std;

char board[9] = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};

void show() {
    for (int i = 0; i < 9; i += 3) {
        cout << board[i] << " | "
             << board[i+1] << " | "
             << board[i+2] << endl;

        if (i < 6)
            cout << "--|---|--" << endl;
    }
}

bool winner(char p) {
    int wins[8][3] = {
        {0,1,2}, {3,4,5}, {6,7,8},
        {0,3,6}, {1,4,7}, {2,5,8},
        {0,4,8}, {2,4,6}
    };

    for (int i = 0; i < 8; i++) {
        if (board[wins[i][0]] == p &&
            board[wins[i][1]] == p &&
            board[wins[i][2]] == p)
            return true;
    }

    return false;
}

int minimax(bool isMax) {
    if (winner('O')) return 1;
    if (winner('X')) return -1;

    bool empty = false;
    for (int i = 0; i < 9; i++)
        if (board[i] == ' ')
            empty = true;

    if (!empty) return 0;

    int best = isMax ? -2 : 2;

    for (int i = 0; i < 9; i++) {
        if (board[i] == ' ') {
            board[i] = isMax ? 'O' : 'X';

            int score = minimax(!isMax);
            board[i] = ' ';

            if (isMax)
                best = max(best, score);
            else
                best = min(best, score);
        }
    }

    return best;
}

void aiMove() {
    int best = -2, move = -1;

    for (int i = 0; i < 9; i++) {
        if (board[i] == ' ') {
            board[i] = 'O';

            int score = minimax(false);
            board[i] = ' ';

            if (score > best) {
                best = score;
                move = i;
            }
        }
    }

    if (move != -1)
        board[move] = 'O';
}

int main() {
    while (true) {
        show();

        int pos;
        cout << "Enter position (1-9): ";
        cin >> pos;
        pos--;

        if (pos < 0 || pos > 8 || board[pos] != ' ') {
            cout << "Invalid move!" << endl;
            continue;
        }

        board[pos] = 'X';

        if (winner('X')) {
            show();
            cout << "You Win!" << endl;
            break;
        }

        bool empty = false;
        for (int i = 0; i < 9; i++)
            if (board[i] == ' ')
                empty = true;

        if (!empty) {
            show();
            cout << "Draw!" << endl;
            break;
        }

        aiMove();

        if (winner('O')) {
            show();
            cout << "AI Wins!" << endl;
            break;
        }

        empty = false;
        for (int i = 0; i < 9; i++)
            if (board[i] == ' ')
                empty = true;

        if (!empty) {
            show();
            cout << "Draw!" << endl;
            break;
        }
    }

    return 0;
}
