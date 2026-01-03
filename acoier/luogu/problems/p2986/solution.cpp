//
// Created by benhao on 2026/1/3.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n;
vector<vector<pair<int, int>>> graph;
vector<int> counts;
vector<ll> dp;
vector<ll> sz;
ll ans;

int dfs(const int u, const int pa, const ll dist) {
    sz[u] = counts[u];
    for (const auto& [v, l]: graph[u]) {
        if (v == pa) {
            continue;
        }
        dp[0] += (dist + l) * counts[v];
        sz[u] += dfs(v, u, dist + l);
    }
    return sz[u];
}

void dfs2(const int u, const int pa) {
    for (const auto& [v, l]: graph[u]) {
        if (v == pa) {
            continue;
        }
        dp[v] = dp[u] + (sz[0] - sz[v] * 2) * l;
        ans = min(ans, dp[v]);
        dfs2(v, u);
    }
}

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    cin >> n;
    graph.resize(n);
    counts.resize(n);
    dp.resize(n);
    sz.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> counts[i];
    }
    for (int i = 0; i < n - 1; ++i) {
        int a, b, l;
        cin >> a >> b >> l;
        --a, --b;
        graph[a].emplace_back(b, l);
        graph[b].emplace_back(a, l);
    }
    dfs(0, -1, 0);
    ans = dp[0];
    dfs2(0, -1);
    cout << ans << endl;
    return 0;
}