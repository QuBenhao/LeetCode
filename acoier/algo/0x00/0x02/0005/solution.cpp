//
// Created by benhao on 2026/1/15.
// Example: Strange Towers of Hanoi acwing96
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))

/*
 * d[x] is the minimum number of moves for x disks on 3 pegs
 * Move x-1 disks to peg B, move the largest disk to peg C, then move the x-1 disks to peg C
 * Thus: d[x] = 2 * d[x - 1] + 1
 * d[1] = 1
 *
 * f[x] is the minimum number of moves for x disks on 4 pegs
 * Move i disks to peg B, solve the 3-peg problem for the remaining x-i disks, then solve the 4-peg problem to move the i disks to peg D
 * Thus: f[x] = min(f[i] * 2 + d[x-i])
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
