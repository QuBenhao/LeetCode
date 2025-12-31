//
// Created by benhao on 2025/12/31.
//

#include <bits/stdc++.h>
using namespace std;
using ll = __int128;

void write(__int128 x){
    if(x>=10) write(x/10);
    putchar(x%10+'0');
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> arr(m);
    ll ans = 0;
    for (int i = 0; i < n; ++i) {
        vector dp(m, vector<ll>(m, 0));
        for (int j = 0; j < m; ++j) {
            cin >> arr[j];
            ll base = 1;
            base <<= m;
            dp[j][j] = base * arr[j];
        }
        for (int len = 2; len <= m; ++len) {
            for (int l = 0; l <= m - len; ++l) {
                const int r = l + len - 1;
                ll base = 1;
                base <<= m - len + 1;
                dp[l][r] = max(dp[l][r], max(dp[l+1][r] + base * arr[l], dp[l][r - 1] + base * arr[r]));
            }
        }
        ans += dp[0][m-1];
    }
    write(ans);
    return 0;
}