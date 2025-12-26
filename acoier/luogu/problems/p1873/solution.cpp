//
// Created by benhao on 2025/12/26.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <ranges>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    ranges::sort(arr);
    vector<long long> presum(n+1);
    for (int i = 0; i < n; ++i) presum[i + 1] = presum[i] + arr[i];
    int left = arr[0], right = arr[n - 1];
    long long tm = presum[n] - m;
    while (left < right) {
        int mid = ((right - left + 1) >> 1) + left;
        int idx = lower_bound(arr.begin(), arr.end(), mid) - arr.begin();
        // presum[n] - presum[idx] - (n - idx) * mid < m
        if (presum[idx] + (1ll * n - idx) * mid > tm) {
            right = mid - 1;
        } else {
            left = mid;
        }
    }
    cout << left << endl;
    return 0;
}