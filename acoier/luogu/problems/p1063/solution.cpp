//
// Created by benhao on 2025/12/31.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n << 1);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    for (int i = n; i < n << 1; ++i) {
        arr[i] = arr[i - n];
    }
    vector dp(n << 1, vector<int>(n << 1));
    for (int len = 2; len <= n; ++len) {
        for (int l = 0; l <= (n << 1) - len; ++l) {
            const int r = l + len - 1;
            for (int i = l; i < r; ++i) {
                dp[l][r] = max(dp[l][r], dp[l][i] + dp[i+1][r] + arr[l] * arr[r+1] * arr[i+1]);
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        ans = max(ans, dp[i][i + n - 1]);
    }
    cout << ans << endl;
    return 0;
}