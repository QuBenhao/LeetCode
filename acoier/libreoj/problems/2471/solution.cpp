//
// Created by benhao on 2026/1/3.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// state describes the path tracing the current boundary from the upper-right corner. Its length is n+m; only n+m-1 steps need consideration because the last step always leads to the lower-left corner
// Moving left decreases the column and uses a 1 bit; moving down increases the row and uses a 0 bit
// Initially at the upper-left corner, so the last m bits are 1 and the first n bits are 0
// Finally at the lower-right corner, so the last n bits are 0 and the first m bits are 1
// Note: this is the contour DP idea!

int memo[1048580]; // 1 << 20 = 1048576
int n, m;
int matrix_a[11][11], matrix_b[11][11];
int min_max(const int st, const int turn) {
    if (~memo[st]) {
        return memo[st];
    }
    int res = turn == 0 ? INT_MIN : INT_MAX;
    // Upper-right corner
    int y = m, x = 0;
    for (int i = 0; i < n + m - 1; ++i) {
        if (st >> i & 1) {
            --y;
        } else {
            ++x;
        }
        // Check for a valid corner: 00 keeps moving down, 11 keeps moving left, and 01 is an inward corner that cannot be filled
        if ((st >> i & 3) != 1) {
            continue;
        }
        if (turn == 0) {
            // Placing at (x, y) changes the two path-direction bits with ^ 3<<i
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
    // Terminal state: no score remains to collect
    memo[((1 << m) - 1) << n] = 0;
    cout << min_max((1 << m) - 1, 0) << endl;
    return 0;
}
