//
// Created by benhao on 2026/1/16.
// 例题: Fractal Streets acwing98
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))

// 坐标
pair<ll, ll> dfs(const int n, const ll a) {
    if (n == 0) return {0, 0};
    const ll d = 1LL << (n - 1);
    const ll dd = 1LL << (2 * n - 2);
    const ll div = a / dd, rem = a % dd;
    const auto [x, y] = dfs(n - 1, rem);
    if (div == 0) return {y, x};
    if (div == 1) return {x, y + d};
    if (div == 2) return {d + x, d + y};
    return {2 * d - y - 1, d - x - 1};
}

int main() {
    int T;
    cin >> T;
    int N;
    ll A, B;
    while (T--) {
        cin >> N;
        cin >> A >> B;
        --A, --B;
        if (A == B) {
            cout << 0 << endl;
            continue;
        }
        const auto [xa, ya] = dfs(N, A);
        const auto [xb, yb] = dfs(N, B);
        const ll x = abs(xa - xb), y = abs(ya - yb);
        printf("%.0f\n", (double)sqrt(x * x + y * y) * 10);
    }
    return 0;
}
