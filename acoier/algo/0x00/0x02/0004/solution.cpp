//
// Created by benhao on 2026/1/15.
// Example: 费解的开关 acwing95
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))

constexpr int N = 5;
int matrix[N];
constexpr int STEP = 6;
constexpr int DIR[4][2]{{0, -1}, {0, 1}, {1, 0}, {-1, 0}};

int dfs(int x, int y, int s) {
    if (s > STEP) return STEP + 1;
    if (y == N) return dfs(x + 1, 0, s);
    bool flag = true;
    for (int i = 0; i < N; ++i) {
        if (matrix[i] != (1 << N) - 1) {
            flag = false;
            break;
        }
    }
    if (flag) {
        return s;
    }
    if (x == N || s == STEP) {
        return STEP + 1;
    }
    // Required pruning: do not turn a correct cell in the previous row into an incorrect one
    if (x > 0 && matrix[x - 1] >> (N - 1 - y) & 1) return dfs(x, y + 1, s);
    int res = STEP + 1;
    // Toggle x, y
    matrix[x] ^= 1 << (N - 1 - y);
    for (const auto& [dx, dy]: DIR) {
        const int nx = x + dx, ny = y + dy;
        if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
        matrix[nx] ^= 1 << (N - 1 - ny);
    }
    res = min(res, dfs(x, y + 1, s + 1));
    // Do not toggle
    matrix[x] ^= 1 << (N - 1 - y);
    for (const auto& [dx, dy]: DIR) {
        const int nx = x + dx, ny = y + dy;
        if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
        matrix[nx] ^= 1 << (N - 1 - ny);
    }
    res = min(res, dfs(x, y + 1, s));
    return res;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        string line;
        for (int i = 0; i < N; ++i) {
            cin >> line;
            int val = 0;
            for (int j = 0; j < N; ++j) {
                val |= (line[j] - '0') << (N - 1 - j);
            }
            matrix[i] = val;
        }
        if (const int ans = dfs(0, 0, 0); ans <= STEP) {
            cout << ans << endl;
        } else {
            cout << -1 << endl;
        }
    }
    return 0;
}
