//
// Created by benhao on 2026/1/3.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// state，从右上角开始走出当前斜线的路径，长度必然是n+m-1
// 假设要往左走，即列变小，该位为1; 否则是往下走, 即行变大，该位为0
// 初始在左上角，所以是后m位为1,前n位为0
// 最终在右下角，即后n位为0,前m位为1

int memo[1048580]; // 1 << 20 = 1048576
int n, m;
int matrix_a[11][11], matrix_b[11][11];
int min_max(const int st, const int turn) {
    if (~memo[st]) {
        return memo[st];
    }
    int res = turn == 0 ? INT_MIN : INT_MAX;
    // 右上角
    int y = m, x = 0;
    for (int i = 0; i < n + m && y >= 0 && x < n; ++i) {
        if (st >> i & 1) {
            --y;
        } else {
            ++x;
        }
        // 判断当前是合法拐点, 00是一直往下走, 11是一直往左走, 01是反拐填不了
        if ((st >> i & 3) != 1) {
            continue;
        }
        if (turn == 0) {
            // 假设下了(x, y)这个点, 那么要修改这两位的行走方式, 即 ^ 3<<i
            res = max(res, min_max(st ^ 3 << i, turn ^ 1) + matrix_a[x][y]);
        } else {
            res = min(res, min_max(st ^ 3 << i, turn ^ 1) - matrix_b[x][y]);
        }
    }
    // cout << st << ", " << res << endl;
    return memo[st] = res;
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> matrix_a[i][j];
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> matrix_b[i][j];
        }
    }
    memset(memo, -1, sizeof memo);
    // 终点状态, 无分可拿了
    memo[((1 << m) - 1) << n] = 0;
    cout << min_max((1 << m) - 1, 0) << endl;
    return 0;
}