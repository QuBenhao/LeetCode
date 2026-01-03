//
// Created by benhao on 2026/1/3.
//

#include <bits/stdc++.h>
using namespace std;

const int MAXN = 400005;

vector<int> adj[MAXN];
int sz[MAXN];
int dp[MAXN]; // Max valid subtree size inside subtree(u)
int up[MAXN]; // Max valid subtree size outside subtree(u)
int n;

// First DFS: Calculate subtree sizes and dp[u]
void dfs_sz(int u, int p) {
    sz[u] = 1;
    dp[u] = 0;
    for (int v : adj[u]) {
        if (v == p) continue;
        dfs_sz(v, u);
        sz[u] += sz[v];
        dp[u] = max(dp[u], dp[v]);
    }

    // If the subtree itself is small enough, it is the best candidate
    if (sz[u] <= n / 2) {
        dp[u] = sz[u];
    }
}

// Second DFS: Calculate up[u]
void dfs_up(int u, int p) {
    // Find top 2 largest dp values among children to handle sibling logic efficiently
    int mx1 = -1, mx2 = -1;
    for (int v : adj[u]) {
        if (v == p) continue;
        if (dp[v] > mx1) {
            mx2 = mx1;
            mx1 = dp[v];
        } else if (dp[v] > mx2) {
            mx2 = dp[v];
        }
    }

    for (int v : adj[u]) {
        if (v == p) continue;

        // Candidate 1: Best valid subtree from above u (passed down from u's parent)
        int best_from_above = up[u];

        // Candidate 2: The component "above u" itself.
        // If we cut the edge above u, the remaining component has size n - sz[u].
        // If this component is small enough, it's a valid candidate for v's "outside".
        if (n - sz[u] <= n / 2) {
            best_from_above = max(best_from_above, n - sz[u]);
        }

        // Candidate 3: Best valid subtree from siblings of v
        int best_from_siblings = (dp[v] == mx1) ? mx2 : mx1;
        if (best_from_siblings == -1) best_from_siblings = 0;

        up[v] = max(best_from_above, best_from_siblings);

        dfs_up(v, u);
    }
}

int main() {
    // Optimize I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> n)) return 0;

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // Step 1: Bottom-up info
    dfs_sz(1, 0);

    // Step 2: Top-down info
    dfs_up(1, 0);

    // Step 3: Check each vertex
    for (int i = 1; i <= n; i++) {
        bool possible = true;

        // Check children components
        for (int v : adj[i]) {
            if (sz[v] < sz[i]) { // v is a child
                if (sz[v] > n / 2) {
                    // Try to fix heavy child component
                    if (sz[v] - dp[v] > n / 2) {
                        possible = false;
                    }
                }
            } else { // v is parent
                int parent_comp_size = n - sz[i];
                if (parent_comp_size > n / 2) {
                    // Try to fix heavy parent component
                    if (parent_comp_size - up[i] > n / 2) {
                        possible = false;
                    }
                }
            }
        }

        cout << (possible ? 1 : 0) << (i == n ? "" : " ");
    }
    cout << endl;

    return 0;
}