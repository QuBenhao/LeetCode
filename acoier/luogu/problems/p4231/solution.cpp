//
// Created by benhao on 2025/12/23.
//

#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    // 数组变化为等差数列
    // 那么一阶差分是[0, s, d, d, d, -e, 0] 起始变化为s,中间变化全部为d,最终变化为-e
    // 二阶差分变化就是[0, s, d-s, 0, 0, -d-e, e]
    std::vector<long long> diff(n + 4);
    for (int i = 0; i < m; ++i) {
        int l, r;
        long long s, e;
        scanf("%d%d%lld%lld", &l, &r, &s, &e);
        long long d = (e - s) / (r - l);
        diff[l] += s;
        diff[l + 1] += d - s;
        diff[r + 1] -= d + e;
        diff[r + 2] += e;
    }
    long long a = 0LL, b = 0LL, ans1 = 0LL, ans2 = 0LL;
    for (int i = 1; i <= n; ++i) {
        b += diff[i];
        a += b;
        ans2 = std::max(ans2, a);
        ans1 ^= a;
    }
    printf("%lld %lld", ans1, ans2);
    return 0;
}