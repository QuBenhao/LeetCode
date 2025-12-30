//
// Created by benhao on 2025/12/30.
//

#include <bits/stdc++.h>

using namespace std;

int main() {
    int m, n;
    cin >> m >> n;
    unordered_map<int, vector<pair<int, int>>> mp;
    int k = 0;
    for (int i = 0; i < n; ++i) {
        int a, b, c;
        cin >> a >> b >> c;
        k = max(k, c);
        mp[c-1].emplace_back(a, b);
    }
    vector<int> dp(m + 1);
    for (int i = 0; i < k; ++i) {
        for (int j = m; j >= 0; --j) {
            for (const auto& [a, b]: mp[i]) {
                if (j >= a) {
                    dp[j] = max(dp[j], dp[j-a] + b);
                }
            }
        }
    }
    cout << dp[m] << endl;
    return 0;
}