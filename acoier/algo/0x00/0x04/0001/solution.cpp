//
// Created by benhao on 2026/1/25.
// Example: Best Cow Fences acwing102
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))

int N, F;
vector<int> nums;
constexpr double EPS = 1e-5;

bool check(double x) {
    // Check whether the maximum subarray sum of length at least F is positive after subtracting the average from each value
    vector<double> sum(N + 1);
    for (int i = 1; i <= N; ++i) {
        sum[i] = sum[i - 1] + nums[i - 1] - x;
    }
    // Track the minimum preceding prefix sum; subtracting it maximizes the interval sum. Two pointers ensure a length of at least F
    double min_v = 0;
    for (int i = 0, j = F; j <= N; ++i, ++j) {
        min_v = min(min_v, sum[i]);
        if (sum[j] >= min_v) return true;
    }
    return false;
}

int solve() {
    double left = 1.0, right = 2000.0;
    while (left + EPS < right) {
        double mid = (left + right) / 2;
        if (check(mid)) left = mid;
        else right = mid;
    }
    // Use right for the maximum result; using left may cause precision errors
    return floor(right * 1000);
}

int main() {
    cin >> N >> F;
    nums.resize(N);
    for (int i = 0; i < N; ++i) {
        cin >> nums[i];
    }
    cout << solve() << endl;
    return 0;
}
