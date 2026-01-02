//
// Created by benhao on 2026/1/2.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n, k;
vector<vector<int>> graph;
array<vector<vector<int>>, 4> dp; // 0: 未放置&未监听, 1: 未放置&监听, 2: 放置&未监听, 3: 放置&监听
constexpr int MOD = 1e9 + 7;

int sum_mod(const initializer_list<int> nums) {
    int res = 0;
    for (const auto &num: nums) {
        res = (res + num) % MOD;
    }
    return res;
}

int mul_mod(const initializer_list<int> nums) {
    ll res = 1LL;
    for (const auto &num: nums) {
        res = res * num % MOD;
    }
    return static_cast<int>(res);
}

int dfs(const int u, const int pa) {
    int p = 1;
    dp[0][u][0] = 1;
    dp[2][u][1] = 1;
    for (const auto &v: graph[u]) {
        if (v == pa) {
            continue;
        }
        const int sz = dfs(v, u);
        vector tmp(4, vector<int>(k + 1));
        for (int i = min(p, k); i >= 0; --i) {
            for (int j = 0; j <= sz && i + j <= k; ++j) {
                int tot = sum_mod({dp[0][v][j], dp[1][v][j], dp[2][v][j], dp[3][v][j]});
                tmp[0][i + j] = sum_mod({
                    tmp[0][i + j],
                    mul_mod({dp[0][u][i], dp[1][v][j]}) // 子节点必须被监听, 因为父节点不会监听它了
                });
                tmp[1][i + j] = sum_mod({
                    tmp[1][i + j],
                    mul_mod({dp[0][u][i], dp[3][v][j]}), // 子节点必须被监听, 因为父节点不会监听它了
                    mul_mod({dp[1][u][i], sum_mod({dp[1][v][j], dp[3][v][j]})}), // 子节点必须自洽
                });
                tmp[2][i + j] = sum_mod({
                    tmp[2][i + j],
                    mul_mod({dp[2][u][i], sum_mod({dp[0][v][j], dp[1][v][j]})}),
                });
                tmp[3][i + j] = sum_mod({
                    tmp[3][i + j],
                    mul_mod({dp[3][u][i], tot}),
                    mul_mod({dp[2][u][i], sum_mod({dp[2][v][j], dp[3][v][j]})}),
                });
            }
        }
        p += sz;
        for (int s = 0; s < 4; ++s) {
            for (int i = 0; i <= min(p, k); ++i) {
                dp[s][u][i] = tmp[s][i];
            }
        }
    }
    return p;
}

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    cin >> n >> k;
    graph.resize(n);
    for (int i = 0; i < 4; ++i) {
        dp[i] = vector(n, vector(k + 1, 0));
    }
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        --u, --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    dfs(0, -1);
    cout << sum_mod({dp[1][0][k], dp[3][0][k]}) << endl;
    return 0;
}
