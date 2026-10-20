#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;

vector<int> goal = {1, 2, 3, 4, 5, 6, 7, 8, 0};

int heuristic(vector<int> state) {
    int distance = 0;

    for (int i = 0; i < 9; i++) {
        if (state[i] != 0) {
            int value = state[i] - 1;
            distance += abs(i / 3 - value / 3);
            distance += abs(i % 3 - value % 3);
        }
    }

    return distance;
}

vector<vector<int>> neighbours(vector<int> state) {
    vector<vector<int>> result;
    int blank = find(state.begin(), state.end(), 0)
                - state.begin();

    int row = blank / 3;
    int col = blank % 3;

    int dr[] = {-1, 1, 0, 0};
    int dc[] = {0, 0, -1, 1};

    for (int i = 0; i < 4; i++) {
        int r = row + dr[i];
        int c = col + dc[i];

        if (r >= 0 && r < 3 && c >= 0 && c < 3) {
            int pos = r * 3 + c;
            vector<int> next = state;

            swap(next[blank], next[pos]);
            result.push_back(next);
        }
    }

    return result;
}

struct Node {
    int f, g;
    vector<int> state;

    bool operator>(const Node& other) const {
        return f > other.f;
    }
};

void aStar(vector<int> start) {
    priority_queue<Node, vector<Node>, greater<Node>> pq;

    map<vector<int>, int> cost;
    map<vector<int>, vector<int>> parent;

    pq.push({heuristic(start), 0, start});
    cost[start] = 0;

    while (!pq.empty()) {
        Node current = pq.top();
        pq.pop();

        vector<int> state = current.state;
        int g = current.g;

        if (g != cost[state])
            continue;

        if (state == goal) {
            vector<vector<int>> path;

            while (true) {
                path.push_back(state);

                if (state == start)
                    break;

                state = parent[state];
            }

            reverse(path.begin(), path.end());

            for (int i = 0; i < (int)path.size(); i++) {
                cout << "Move " << i << endl;

                for (int j = 0; j < 9; j++) {
                    cout << path[i][j] << " ";
                    if (j % 3 == 2)
                        cout << endl;
                }

                cout << endl;
            }

            cout << "Total Moves = "
                 << path.size() - 1 << endl;
            return;
        }

        for (vector<int> child : neighbours(state)) {
            int newG = g + 1;

            if (!cost.count(child) || newG < cost[child]) {
                cost[child] = newG;
                parent[child] = state;

                int f = newG + heuristic(child);
                pq.push({f, newG, child});
            }
        }
    }

    cout << "No Solution Found" << endl;
}

int main() {
    vector<int> start = {
        1, 2, 3,
        4, 0, 6,
        7, 5, 8
    };

    aStar(start);

    return 0;
}
