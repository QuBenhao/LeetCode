//
// Created by benhao on 2025/12/31.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int n;
    cin >> n;
    vector<ll> pre_sum((n << 1) + 1);
    for (int i = 0; i < n; ++i) {
        int v;
        cin >> v;
        pre_sum[i + 1] = pre_sum[i] + v;
    }
    for (int i = n; i < n << 1; ++i) {
        pre_sum[i + 1] = pre_sum[i] + (pre_sum[i-n+1] - pre_sum[i-n]);
    }
    vector dp_max(n << 1, vector<ll>(n << 1)), dp_min(n << 1, vector(n << 1, LONG_LONG_MAX >> 2));
    for (int i = 0; i < n << 1; ++i) {
        dp_min[i][i] = 0;
    }
    for (int len = 2; len <= n; ++len) {
        for (int l = 0; l <= 2 * n - len; ++l) {
            const int r = l + len - 1;
            for (int i = l; i < r; ++i) {
                dp_max[l][r] = max(dp_max[l][r], dp_max[l][i] + dp_max[i+1][r]);
                dp_min[l][r] = min(dp_min[l][r], dp_min[l][i] + dp_min[i+1][r]);
            }
            dp_max[l][r] += pre_sum[r+1] - pre_sum[l];
            dp_min[l][r] += pre_sum[r+1] - pre_sum[l];
        }
    }
    ll ans_min = LONG_LONG_MAX, ans_max = 0;
    for (int i = 0; i < n; ++i) {
        ans_min = min(ans_min, dp_min[i][i + n - 1]);
        ans_max = max(ans_max, dp_max[i][i + n - 1]);
    }
    cout << ans_min << endl;
    cout << ans_max << endl;
    return 0;
}