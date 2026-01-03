//
// Created by benhao on 2026/1/3.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int W, n;
    cin >> W >> n;
    const int total = (1 << n) - 1;
    vector dp(total + 1, INT_MAX >> 1);
    vector<int> times(total + 1), weights(total + 1);
    for (int i = 0, t, w; i < n; ++i) {
        cin >> t >> w;
        for (int j = 0; j <= total; ++j) {
            if (j >> i & 1) {
                times[j] = max(times[j], t);
                weights[j] += w;
            }
        }
    }
    for (int i = 0; i <= total; ++i) {
        if (weights[i] <= W) {
            dp[i] = times[i];
        }
        for (int j = i; j; j = i & (j - 1)) { // 子集枚举
            if (weights[i ^ j] <= W) {
                dp[i] = min(dp[i], dp[j] + times[i ^ j]);
            }
        }
    }
    cout << dp[total] << endl;
    return 0;
}