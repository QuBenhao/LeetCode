# 枚举子集

```c++
//
// Created by benhao on 2025/12/19.
//
#include <iostream>

#ifdef ONLINE_JUDGE
    // 在线评测系统通常使用GCC
    #include <bits/stdc++.h>
#else
    #include <iosfwd>
#endif
using namespace std;

const int MAX_A = 4e6 + 10;
const int MAX_MASK = 1 << 22;  // 2^22 > 4e6
const int FULL_MASK = (1 << 22) - 1;

int dp[MAX_MASK];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;
    vector<int> a(n);

    // 初始化 dp 数组为 -1
    memset(dp, -1, sizeof(dp));

    // 读入并标记存在的数字
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        dp[a[i]] = a[i];  // 直接标记
    }

    // 预处理 DP：dp[mask] 存储 mask 的某个存在的子集
    // 从子集向超集传递
    for (int mask = 0; mask < MAX_MASK; mask++) {
        if (dp[mask] != -1) {
            // 这个 mask 本身就在数组中
            continue;
        }

        // 尝试去掉一位 1，查看子集
        for (int i = 0; i < 22; i++) {
            if (mask & (1 << i)) {
                int sub = mask ^ (1 << i);
                if (dp[sub] != -1) {
                    dp[mask] = dp[sub];
                    break;
                }
            }
        }
    }

    // 为每个 a[i] 寻找答案
    for (int i = 0; i < n; i++) {
        // 取补集，只保留低 22 位
        int complement = (~a[i]) & FULL_MASK;
        cout << dp[complement] << " ";
    }

    return 0;
}
```