//
// Created by benhao on 2026/1/15.
// 例题: Strange Towers of Hanoi acwing96
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))

/*
 * d[x]表示3塔中搬运x盘的最小步数
 * 需要先把x-1盘搬到B塔, 再把最大盘搬到C塔, 再把x-1盘搬到C塔
 * 即: d[x] = 2 * d[x - 1] + 1
 * d[1] = 1
 *
 * f[x]表示4塔中搬运x盘的最小步数
 * 可以先搬i个盘子到B塔, 剩下的就是x-i个盘的3塔问题, 再把i盘搬到D塔的4塔问题
 * 即: f[x] = min(f[i] * 2 + d[x-i])
 * f[1] =1
*/

int memo_d[13];
int memo_f[13];

int dfs_d(int x) {
    if (x == 1) return 1;
    if (memo_d[x] != -1) return memo_d[x];
    return memo_d[x] = dfs_d(x - 1) * 2 + 1;
}

int dfs_f(int x) {
    if (x == 1) return 1;
    if (memo_f[x] != -1) return memo_f[x];
    int res = INT_MAX;
    for (int i = 1; i < x; ++i) {
        res = min(res, dfs_f(i) * 2 + dfs_d(x - i));
    }
    return memo_f[x] = res;
}

int main() {
    memset(memo_d, -1, sizeof(memo_d));
    memset(memo_f, -1, sizeof(memo_f));
    for (int n = 1; n <= 12; ++n) {
        cout << dfs_f(n) << endl;
    }
    return 0;
}
