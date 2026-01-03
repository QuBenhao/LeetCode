//
// Created by benhao on 2026/1/3.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int n, k;
    cin >> n >> k;
    vector dp(n, vector(1 << n, vector<ll>(k + 1)));
    vector<int> available;
    unordered_map<int, int> counts;
    unordered_map<int, vector<int>> graph;
    for (int i = 0; i < 1 << n; ++i) {
        int cnt = 0;
        bool valid = true;
        for (int j = 0; j < n; ++j) {
            if (i >> j & 1) {
                ++cnt;
                if (j > 0 && (i >> (j - 1) & 1) != 0) {
                    valid = false;
                    break;
                }
            }
        }
        if (valid && cnt <= k) {
            dp[0][i][cnt] = 1;
            available.emplace_back(i);
            counts[i] = cnt;
        }
    }
    graph[0].emplace_back(0);
    for (const auto& i: available) {
        for (const auto& j: available) {
            if (i <= j) {
                continue;
            }
            bool fits = true;
            for (int x = 0; x < n; ++x) {
                if ((i >> x & 1) != 1) {
                    continue;
                }
                if (j >> x & 1) {
                    fits = false;
                    break;
                }
                if (x > 0 && (j >> (x - 1) & 1) == 1) {
                    fits = false;
                    break;
                }
                if (x < n - 1 && (j >> (x + 1) & 1) == 1) {
                    fits = false;
                    break;
                }
            }
            if (fits) {
                graph[i].push_back(j);
                graph[j].push_back(i);
            }
        }
    }
    for (int i = 1; i < n; ++i) {
        for (const auto& st: available) {
            for (const auto& nxt: graph[st]) {
                for (int c = counts[st]; counts[nxt] + c <= k; ++c) {
                    dp[i][nxt][counts[nxt] + c] += dp[i - 1][st][c];
                }
            }
        }
    }
    ll ans = 0;
    for (const auto& st: available) {
        ans += dp[n - 1][st][k];
    }
    cout << ans << endl;
    return 0;
}