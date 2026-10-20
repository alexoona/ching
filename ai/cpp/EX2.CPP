
#include <iostream>
#include <vector>
using namespace std;

int main() {
    char grid[3][3] = {
        {'S', '.', '.'},
        {'X', '.', '.'},
        {'.', '.', 'G'}
    };

    int row = 0, col = 0;
    vector<pair<int, int>> visited;

    while (true) {
        visited.push_back({row, col});

        cout << "Current Position: ("
             << row << ", " << col << ")" << endl;

        if (grid[row][col] == 'G') {
            cout << "Goal Reached!" << endl;
            break;
        }

        if (col < 2 && grid[row][col + 1] != 'X') {
            col++;
        }
        else if (row < 2 && grid[row + 1][col] != 'X') {
            row++;
        }
        else {
            cout << "No Path Found!" << endl;
            break;
        }
    }

    cout << "Visited Cells: ";
    for (auto cell : visited) {
        cout << "(" << cell.first << ", "
             << cell.second << ") ";
    }

    cout << endl;
    return 0;
}
