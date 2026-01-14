//
// Created by benhao on 2026/1/13.
// 例题: 起床困难综合症 acwing998
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))

int main() {
    int n, m;
    cin >> n >> m;
    int zero = 0, one = INT_MAX;
    for (int i = 0; i < n; ++i) {
        string op;
        int t;
        cin >> op >> t;
        if (op == "AND") {
            zero &= t;
            one &= t;
        } else if (op == "OR") {
            zero |= t;
            one |= t;
        } else {
            zero ^= t;
            one ^= t;
        }
    }
    if (m == 0) {
        cout << zero << endl;
        return 0;
    }
    const int bits = 32 - __builtin_clz(m);
    int ans_t = zero & ~((1 << (bits + 1)) - 1);
    bool limit = true;
    for (int i = bits; i >= 0; --i) {
        const int t1 = one >> i & 1;
        if (const int t0 = zero >> i & 1; t0 >= t1) {
            if (limit) {
                limit = (m >> i & 1) == 0;
            }
            ans_t |= t0 << i;
        } else {
            if (limit && (m >> i & 1) == 0) {
                continue;
            }
            ans_t |= t1 << i;
        }
    }
    cout << ans_t << endl;
    return 0;
}
