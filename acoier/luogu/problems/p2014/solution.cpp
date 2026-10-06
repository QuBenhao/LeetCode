//
// Created by benhao on 2026/1/1.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n, m;
vector<int> score;
unordered_map<int, vector<int>> graph;
vector<vector<int>> dp;

int dfs(int u) { // Return the number of nodes under the current root
    int p = 1; // Include the current node
    dp[u][1] = score[u];
    for (const auto& v : graph[u]) {
        int sz = dfs(v); // Number of nodes in the subtree
        for (int i = min(p, m + 1); i; --i) { // Number of nodes currently selected, at most m + 1
            for (int j = 1; j <= sz && i + j <= m + 1; ++j) { // Select at least one node; otherwise this iteration serves no purpose
                dp[u][i + j] = max(dp[u][i + j], dp[u][i] + dp[v][j]); // Recurrence
            }
        }
        p += sz;
    }
    return p;
}

int main() {
    cin >> n >> m;
    score.resize(n+1);
    dp = vector (n+1, vector(m+2, 0));
    graph.clear();
    // Add node 0 as the root of all trees
    for (int i = 1; i <= n; ++i) {
        int k, s;
        cin >> k >> s;
        score[i] = s;
        graph[k].push_back(i);
    }
    dfs(0);
    cout << dp[0][m + 1] << endl;
    return 0;
}
