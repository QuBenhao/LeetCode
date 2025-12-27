//
// Created by benhao on 2025/12/27.
//
#include <bits/stdc++.h>

using namespace std;

int n, m;
vector<string> matrix;

constexpr int DIR[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

int main() {
    cin >> n >> m;
    matrix.resize(n);
    for (int i = 0; i < n; ++i) cin >> matrix[i];
    if (n == 1 && m == 1) {
        cout << "Yes" << endl;
        return 0;
    }
    vector visited(n, vector<bool>(m));
    queue<pair<int, int> > q;
    q.emplace(0, 0);
    while (!q.empty()) {
        const auto [x, y] = q.front();
        q.pop();
        for (const auto &[dx, dy]: DIR) {
            int nx = x + dx, ny = y + dy;
            if (nx < 0 || nx >= n || ny < 0 || ny >= m || matrix[nx][ny] == '#' || visited[nx][ny]) {
                continue;
            }
            if (nx == n - 1 && ny == m - 1) {
                cout << "Yes" << endl;
                return 0;
            }
            visited[nx][ny] = true;
            q.emplace(nx, ny);
        }
    }
    cout << "No" << endl;
    return 0;
}
