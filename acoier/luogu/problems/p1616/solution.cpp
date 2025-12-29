//
// Created by benhao on 2025/12/30.
//

#include <bits/stdc++.h>

using namespace std;

int main() {
    int t, m;
    cin >> t >> m;
    vector dp(t + 1, 0ll);
    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        for (int j = 0; j <= t - a; ++j) {
            dp[j+a] = max(dp[j+a], dp[j] + b);
        }
    }
    cout << dp[t] << endl;
    return 0;
}