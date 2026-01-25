//
// Created by benhao on 2026/1/25.
// 例题: Best Cow Fences acwing102
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))

int N, F;
vector<int> nums;
constexpr double EPS = 1e-5;

bool check(double x) {
    // 长度至少为F的最大子段和(每个值减去平均值)是否大于0
    vector<double> sum(N + 1);
    for (int i = 1; i <= N; ++i) {
        sum[i] = sum[i - 1] + nums[i - 1] - x;
    }
    // 维护前面的最小和, 这样后续区间减去最小一定是最大区间和, 双指针保证长度至少为F即可
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
    // 结果要最大值必须用right, 不能用left, 否则可能有精度问题
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
