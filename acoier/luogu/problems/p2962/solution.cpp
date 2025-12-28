//
// Created by benhao on 2025/12/27.
//

#include <bits/stdc++.h>

using namespace std;


int main() {
    int n, m;
    vector<long long> graph;
    cin >> n >> m;
    graph.resize(n);
    for (int i = 0; i < n; ++i) {
        graph[i] = 1LL << i;
    }
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u, --v;
        graph[u] |= 1LL << v;
        graph[v] |= 1LL << u;
    }
    unordered_map<long long, int> dp;
    for (int i = 0; i < 1LL << (n/2); ++i) {
        long long t = 0LL;
        int cnt = 0;
        for (int j = 0; j < n / 2; ++j) {
            if (i >> j & 1) {
                t ^= graph[j];
                ++cnt;
            }
        }
        if (!dp.contains(t)) {
            dp[t] = cnt;
        } else {
            dp[t] = min(dp[t], cnt);
        }
    }
    int ans = INT_MAX;
    for (int i = 0; i < 1LL << (n - n/2); ++i) {
        long long t = 0LL;
        int cnt = 0;
        for (int j = 0; j < n - n / 2; ++j) {
            if (i >> j & 1) {
                t ^= graph[n / 2 + j];
                ++cnt;
            }
        }
        if (dp.contains(((1LL << n) - 1) ^ t)) {
            ans = min(ans, cnt + dp[((1LL << n) - 1)^t]);
        }
    }
    cout << ans << endl;
    return 0;
}