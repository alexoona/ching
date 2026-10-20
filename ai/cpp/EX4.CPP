
#include <iostream>
#include <vector>
#include <queue>
#include <set>
using namespace std;

int main() {
    int n;
    cout << "Enter number of disks: ";
    cin >> n;

    vector<int> start(n, 0), goal(n, 2);

    queue<vector<int>> q;
    set<vector<int>> visited;

    q.push(start);
    visited.insert(start);

    while (!q.empty()) {
        vector<int> state = q.front();
        q.pop();

        if (state == goal) {
            cout << "Goal Reached!" << endl;
            return 0;
        }

        vector<int> pegs[3];

        for (int d = 0; d < n; d++)
            pegs[state[d]].push_back(d);

        for (int i = 0; i < 3; i++) {
            if (pegs[i].empty())
                continue;

            int disk = pegs[i][0];

            for (int j = 0; j < 3; j++) {
                if (i == j)
                    continue;

                if (pegs[j].empty() ||
                    pegs[j][0] > disk) {

                    vector<int> next = state;
                    next[disk] = j;

                    if (visited.find(next) == visited.end()) {
                        visited.insert(next);
                        q.push(next);
                    }
                }
            }
        }
    }

    return 0;
}
