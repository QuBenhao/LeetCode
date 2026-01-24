//
// Created by benhao on 2026/1/17.
// 例题: 激光炸弹 acwing99
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))

int N, R;
int pre_sum[5005][5005];

int main() {
    cin >> N >> R;
    for (int i = 0; i < N; ++i) {
        int x, y, w;
        cin >> x >> y >> w;
        pre_sum[x + 1][y + 1] += w;
    }
    if (R == 0) {
        cout << 0 << endl;
        return 0;
    }
    for (int x = 0; x <= 5000; ++x) {
        for (int y = 0; y <= 5000; ++y) {
            pre_sum[x + 1][y + 1] += pre_sum[x + 1][y] + pre_sum[x][y + 1] - pre_sum[x][y];
        }
    }
    if (R > 5000) {
        cout << pre_sum[5001][5001] << endl;
        return 0;
    }
    int ans = 0;
    for (int x = R; x <= 5001; ++x) {
        for (int y = R; y <= 5001; ++y) {
            ans = max(ans, pre_sum[x][y] - pre_sum[x - R][y] - pre_sum[x][y - R] + pre_sum[x - R][y - R]);
        }
    }
    cout << ans << endl;
    return 0;
}
