//
// Created by benhao on 2025/12/30.
//

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector dp(m + 1, 0);
    for (int i = 0; i < n; ++i) {
        int w, d;
        cin >> w >> d;
        for (int j = m; j >= w; --j) {
            dp[j] = max(dp[j], dp[j - w] + d);
        }
    }
    cout << dp[m] << endl;
    return 0;
}