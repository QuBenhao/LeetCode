//
// Created by benhao on 2026/1/2.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n;
vector<vector<int>> graph;
vector<int> sz;
vector<ll> dp;

int dfs(const int u, const int pa, const int depth) {
    int p = 1;
    if (pa != -1) {
        dp[0] += depth + 1;
    }
    for (const auto& v : graph[u]) {
        if (v != pa) {
            p += dfs(v, u, depth + 1);
        }
    }
    sz[u] = p;
    return p;
}

void dfs2(const int u, const int pa) {
    for (const auto& v : graph[u]) {
        if (v == pa) {
            continue;
        }
        // 交换得分, v得分相对于u来说, (n - sz[v])整体+1, sz[v]整体-1
        dp[v] = dp[u] + n - sz[v] * 2;
        dfs2(v, u);
    }
}

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    cin >> n;
    graph.resize(n);
    sz.resize(n);
    dp.resize(n);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        --u, --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    dfs(0, -1, 0);
    dfs2(0, -1);
    ll ans = dp[0];
    int ans_root = 0;
    for (int i = 1; i < n; ++i) {
        if (dp[i] > ans) {
            ans = dp[i], ans_root = i;
        }
    }
    cout << ans_root + 1 << endl;
    return 0;
}