//
// Created by benhao on 2025/12/30.
//

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m, t;
    cin >> n >> m >> t;
    vector dp(m + 1, vector<int>(t + 1, 0));
    for (int i = 0; i < n; ++i) {
        int cm, ct;
        cin >> cm >> ct;
        for (int j = m; j >= cm; --j) {
            for (int k = t; k >= ct; --k) {
                dp[j][k] = max(dp[j][k], dp[j - cm][k - ct] + 1);
            }
        }
    }
    cout << dp[m][t] << endl;
    return 0;
}