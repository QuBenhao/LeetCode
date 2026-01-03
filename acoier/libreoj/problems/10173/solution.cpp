//
// Created by benhao on 2026/1/3.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

void dfs(const int m, const int i, const int st, vector<int>& states) {
    if (i >= m) {
        states.emplace_back(st);
        return;
    }
    dfs(m, i + 1, st, states); // 不选
    dfs(m, i + 3, st | (1 << i), states); // 选
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> matrix(n);
    for (int i = 0; i < n; ++i) {
        string row;
        cin >> row;
        int st = 0;
        for (int j = 0; j < m; ++j) {
            if (row[j] == 'H') {
                st |= 1 << j;
            }
        }
        matrix[i] = st;
    }
    vector<int> states;
    dfs(m, 0, 0, states);
    vector dp(n, vector<int>(1 << (m << 1)));
    unordered_map<int, unordered_set<int>> graph;
    for (const auto& st: states) {
        if ((matrix[0] & st) == 0) {
            dp[0][st] = popcount(static_cast<unsigned int>(st));
        }
        for (const auto& st1: states) {
            if ((st1 & st) == 0) {
                graph[st].insert(st1);
            }
        }
    }
    for (int i = 1; i < n; ++i) {
        for (const auto& st: states) {
            if (matrix[i] & st) {
                continue;
            }
            const int cnt = popcount(static_cast<unsigned int>(st));
            for (const auto& j: graph[st]) { // 上一行
                for (const auto& sub: graph[j]) {
                    if ((sub & st) != 0) {
                        continue;
                    }
                    dp[i][j << m | st] = max(dp[i][j << m | st], dp[i - 1][sub << m | j] + cnt);
                }
            }
        }
    }
    cout << ranges::max(dp[n - 1]) << endl;
    return 0;
}