//
// Created by benhao on 2026/1/9.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct DSU {
    vector<size_t> pa, size;

    explicit DSU(size_t n) : pa(n), size(n, 1) { iota(pa.begin(), pa.end(), 0); }

    size_t find(size_t x);
    void unite(size_t x, size_t y);
};

size_t DSU::find(size_t x) { return pa[x] == x ? x : pa[x] = find(pa[x]); }
void DSU::unite(size_t x, size_t y) {
    x = find(x); y = find(y);
    if (x == y) return;
    if (size[x] < size[y]) swap(x, y);
    pa[y] = x;
    size[x] += size[y];
}

int main() {
    int n, m;
    cin >> n >> m;
    DSU dsu(n);
    int z, x, y;
    for (int i = 0; i < m; ++i) {
        cin >> z >> x >> y;
        --x; --y;
        if (z == 1) {
            dsu.unite(x, y);
        } else {
            cout << (dsu.find(x) == dsu.find(y) ? "Y" : "N") << endl;
        }
    }
    return 0;
}