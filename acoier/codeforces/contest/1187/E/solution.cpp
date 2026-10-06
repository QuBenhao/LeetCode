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

int dfs(const int u, const int pa) {
    int p = 1;
    for (const auto& v : graph[u]) {
        if (v == pa) {
            continue;
        }
        p += dfs(v, u);
    }
    sz[u] = p;
    dp[0] += p;
    return p;
}

void dfs2(const int u, const int pa) {
    for (const auto& v : graph[u]) {
        if (v == pa) {
            continue;
        }
        // Reroot: add a score of n-sz[v] and subtract a score of sz[v]
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
    dfs(0, -1);
    dfs2(0, -1);
    cout << ranges::max(dp) << endl;
    return 0;
}
