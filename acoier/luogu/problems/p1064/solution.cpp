//
// Created by benhao on 2025/12/30.
//

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector a(m, vector<int>(2));
    unordered_map<int, vector<int>> mp;
    for (int i = 0; i < m; ++i) {
        int q;
        cin >> a[i][0] >> a[i][1] >> q;
        if (q != 0) {
            mp[q - 1].emplace_back(i);
        } else {
            mp[i].emplace_back(i);
        }
    }

    auto f = [&a](int idx) -> long long {
        return 1LL * a[idx][0] * a[idx][1];
    };
    vector<long long> dp(n + 1);
    for (const auto& [k, v]: mp) {
        for (int i = n; i >= 0; --i) {
            // 只买主键
            if (i >= a[k][0]) {
                dp[i] = max(dp[i], dp[i - a[k][0]] + f(k));
            }
            if (v.size() > 1) {
                // 买主键和其中一个附件
                for (const auto& j: v) {
                    if (j == k) {
                        continue;
                    }
                    if (i >= a[k][0] + a[j][0]) {
                        dp[i] = max(dp[i], dp[i - a[k][0] - a[j][0]] + f(k) + f(j));
                    }
                }
                // 买两个附件
                if (v.size() == 3) {
                    int s = a[k][0];
                    long long val = f(k);
                    for (const auto& j: v) {
                        if (j == k) {
                            continue;
                        }
                        s += a[j][0];
                        val += f(j);
                    }
                    if (i >= s) {
                        dp[i] = max(dp[i], dp[i - s] + val);
                    }
                }
            }
        }
    }
    cout << dp[n] << endl;
    return 0;
}