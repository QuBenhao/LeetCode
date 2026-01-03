//
// Created by benhao on 2026/1/3.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

constexpr int MOD = 1e8;

void dfs(const int n, const int i, const int st, vector<int>& states) {
    if (i >= n) {
        states.push_back(st);
        return;
    }
    dfs(n, i + 1, st, states); // 不选
    dfs(n, i + 2, st | 1 << i, states); // 选
}

int main() {
    int m, n;
    cin >> m >> n;
    vector<int> matrix(m);
    for (int i = 0; i < m; ++i) {
        int st = 0;
        for (int j = 0, v; j < n; ++j) {
            cin >> v;
            st |= (v ^ 1) << j;
        }
        matrix[i] = st;
    }
    vector<int> states;
    unordered_map<int, vector<int>> graph;
    dfs(n, 0, 0, states);
    vector dp(m, vector<int>(1 << n));
    graph[0].emplace_back(0);
    int ans = 0;
    for (const auto& st: states) {
        for (const auto& st1: states) {
            if (st >= st1 || (st & st1) != 0) {
                continue;
            }
            graph[st].push_back(st1);
            graph[st1].push_back(st);
        }
        if ((matrix[0] & st) == 0) {
            dp[0][st] = 1;
            if (m == 1) {
                ans = (ans + 1) % MOD;
            }
        }
    }
    for (int i = 1; i < m; ++i) {
        for (const auto& [st, sts]: graph) {
            if ((matrix[i] & st) != 0) {
                continue;
            }
            for (const auto& prev: sts) {
                dp[i][st] = (dp[i][st] + dp[i - 1][prev]) % MOD;
            }
            if (i == m - 1) {
                ans = (ans + dp[i][st]) % MOD;
            }
        }
    }
    cout << ans << endl;
    return 0;
}