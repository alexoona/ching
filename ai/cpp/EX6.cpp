
#include <iostream>
using namespace std;

const int N = 4;

bool isSafe(int board[N][N], int row, int col) {

    for (int i = 0; i < N; i++) {
        if (board[row][i] == 1)
            return false;
    }

    for (int i = 0; i < N; i++) {
        if (board[i][col] == 1)
            return false;
    }

    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 1)
            return false;
    }

    for (int i = row, j = col; i >= 0 && j < N; i--, j++) {
        if (board[i][j] == 1)
            return false;
    }

    return true;
}

bool solve(int board[N][N], int col) {
    if (col == N)
        return true;

    for (int row = 0; row < N; row++) {
        if (isSafe(board, row, col)) {
            board[row][col] = 1;

            if (solve(board, col + 1))
                return true;

            board[row][col] = 0;
        }
    }

    return false;
}

int main() {
    int board[N][N] = {0};

    if (solve(board, 0)) {
        cout << "Solution:" << endl;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++)
                cout << board[i][j] << " ";
            cout << endl;
        }
    } else {
        cout << "Solution does not exist" << endl;
    }

    return 0;
}


/* 

#include <iostream>
using namespace std;

const int N = 8;

bool isSafe(int board[N][N], int row, int col) {
    for (int i = 0; i < N; i++)
        if (board[row][i] == 1)
            return false;

    for (int i = 0; i < N; i++)
        if (board[i][col] == 1)
            return false;

    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j] == 1)
            return false;

    for (int i = row, j = col; i >= 0 && j < N; i--, j++)
        if (board[i][j] == 1)
            return false;

    return true;
}

int main() {
    int board[N][N] = {0};
    int col[N] = {0};
    int row = 0;
    bool found = false;

    while (row >= 0) {
        while (col[row] < N &&
               !isSafe(board, row, col[row])) {
            col[row]++;
        }

        if (col[row] < N) {
            board[row][col[row]] = 1;

            if (row == N - 1) {
                found = true;
                break;
            }

            row++;
            col[row] = 0;
        } else {
            col[row] = 0;
            row--;

            if (row >= 0) {
                board[row][col[row]] = 0;
                col[row]++;
            }
        }
    }

    if (found) {
        cout << "Solution:" << endl;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++)
                cout << board[i][j] << " ";
            cout << endl;
        }
    } else {
        cout << "No solution exists." << endl;
    }

    return 0;
}
*/