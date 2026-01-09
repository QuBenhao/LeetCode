//
// Created by benhao on 2026/1/9.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define lowbit(x) ((x)&(-(x)))

struct FenwickTree {
    vector<ll> arr;
    const size_t n;

    explicit FenwickTree(const size_t n): arr(n + 1), n(n) {}

    void add(size_t x, ll val);
    ll query(size_t x) const;
    ll query_range(size_t x, size_t y) const;
};

void FenwickTree::add(const size_t x, const ll val)  {
    for (size_t i = x; i <= n; i += lowbit(i)) {
        arr[i] += val;
    }
}

ll FenwickTree::query(const size_t x) const {
    ll res = 0;
    for (size_t i = x; i > 0; i -= lowbit(i)) {
        res += arr[i];
    }
    return res;
}

ll FenwickTree::query_range(const size_t x, const size_t y) const {
    return query(y) - query(x - 1);
}

int main() {
    int n, q;
    cin >> n >> q;
    FenwickTree f(n);
    int a;
    for (int i = 1; i <= n; ++i) {
        cin >> a;
        f.add(i, a);
    }
    int op, x, y;
    for (int i = 0; i < q; ++i) {
        cin >> op >> x >> y;
        if (op == 1) {
            f.add(x, y);
        } else {
            cout << f.query_range(x, y) << endl;
        }
    }
    return 0;
}