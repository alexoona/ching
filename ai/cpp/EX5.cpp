
#include <iostream>
#include <vector>
#include <queue>
#include <set>
using namespace std;

int main() {
    vector<vector<char>> start = {{'B', 'C', 'A'}};
    vector<vector<char>> goal = {{'A', 'B', 'C'}};

    queue<vector<vector<char>>> q;
    set<vector<vector<char>>> visited;

    q.push(start);
    visited.insert(start);

    while (!q.empty()) {
        vector<vector<char>> state = q.front();
        q.pop();

        cout << "Current State:" << endl;
        for (int i = 0; i < state.size(); i++) {
            cout << "Stack " << i + 1 << ": ";
            for (char block : state[i])
                cout << block << " ";
            cout << endl;
        }
        cout << endl;

        if (state == goal) {
            cout << "Goal Reached!" << endl;
            return 0;
        }

        for (int i = 0; i < state.size(); i++) {
            if (state[i].empty())
                continue;

            char block = state[i].back();

            for (int j = 0; j < state.size(); j++) {
                if (i == j)
                    continue;

                vector<vector<char>> next = state;

                next[i].pop_back();
                if (next[i].empty())
                    next.erase(next.begin() + i);

                if (j < next.size())
                    next[j].push_back(block);
                else
                    next.push_back({block});

                if (visited.find(next) == visited.end()) {
                    visited.insert(next);
                    q.push(next);
                }
            }
        }
    }

    cout << "No Solution Found" << endl;
    return 0;
}
