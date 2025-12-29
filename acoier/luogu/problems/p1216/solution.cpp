//
// Created by benhao on 2025/12/30.
//

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector dp(n, 0);
    for (int i = 0; i < n; ++i) {
        vector<int> arr(i+1);
        for (int j = 0; j < i + 1; ++j) {
            cin >> arr[j];
        }
        for (int j = i; j > 0; --j) {
            dp[j] = max(dp[j], dp[j - 1]) + arr[j];
        }
        dp[0] += arr[0];
    }
    cout << *ranges::max_element(dp) << endl;
    return 0;
}