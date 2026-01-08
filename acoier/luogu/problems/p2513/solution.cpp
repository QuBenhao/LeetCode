//
// Created by benhao on 2026/1/8.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;
constexpr int MOD = 10000;

int main() {
    int n, k;
    cin >> n >> k;
    // 当前位置i, 相当于解决1~n-i的子问题,之前已填入x个逆序对
    // dp[i][x] = dp[i-1][max(0, x-(n-1-i))] + .. + dp[i-1][x]
    vector dp(2, vector(k + 1, 0));
    dp[1][0] = 1;
    for (int i = 0; i < n; ++i) {
        vector pre(k + 2, 0);
        for (int j = 0; j <= k; ++j) {
            pre[j + 1] = (pre[j] + dp[(i + 1) % 2][j]) % MOD;
        }
        for (int j = 0; j <= k; ++j) {
            dp[i%2][j] = ((pre[j+1] - pre[max(0, j - n + 1 + i)]) % MOD + MOD) % MOD;
        }
    }
    cout << dp[(n-1)%2][k] << endl;
    return 0;
}