//
// Created by benhao on 2025/12/27.
//

#include <bits/stdc++.h>

using namespace std;
constexpr int DIRS[4][2] = {{0, -1}, {0, 1}, {1, 0}, {-1, 0}};
const string TARGET = "123804765";

vector<string> transfer(const string& state) {
    vector<string> result;
    int zero = find(state.begin(), state.end(), '0') - state.begin();
    int x = zero / 3, y = zero % 3;
    for (const auto& [dx, dy]: DIRS) {
        const int nx = x + dx, ny = y + dy;
        if (nx < 0 || nx >= 3 || ny < 0 || ny >= 3) {
            continue;
        }
        string tmp = state;
        swap(tmp[nx * 3 + ny], tmp[zero]);
        result.push_back(tmp);
    }
    return result;
}

int main() {
    string start;
    cin >> start;
    if (start == TARGET) {
        cout << 0 << endl;
        return 0;
    }
    unordered_map<string, pair<int, int>> visited;
    queue<tuple<int, int, string>> q;
    q.emplace(1, 0, start);
    q.emplace(2, 0, TARGET);
    visited[start] = {1, 0};
    visited[TARGET] = {2, 0};
    while (!q.empty()) {
        const auto [mark, dist, state] = q.front();
        q.pop();
        const auto& trans = transfer(state);
        for (const auto& nxt: trans) {
            auto iter = visited.find(nxt);
            if (iter == visited.end()) {
                visited[nxt] = {mark, dist + 1};
                q.emplace(mark, dist + 1, nxt);
            } else {
                if (iter->second.first == mark) {
                    continue;
                }
                cout << iter->second.second + dist + 1 << endl;
                return 0;
            }
        }
    }
    return 0;
}