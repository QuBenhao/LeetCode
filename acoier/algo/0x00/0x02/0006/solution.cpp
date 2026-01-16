//
// Created by benhao on 2026/1/16.
// 例题: Sumdiv acwing97
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))

constexpr int MOD = 9901;

int A, B;

void factors(int n, vector<pair<int, int>>& fs) {
    for (int i = 2; i * i <= n; ++i) {
        if (!(n % i)) {
            int d = 0;
            while (!(n % i)) {
                ++d;
                n /= i;
            }
            fs.emplace_back(i, d);
        }
    }
    if (n != 1) fs.emplace_back(n, 1);
}

ll fast_pow(ll base, ll exp) {
    ll result = 1;
    for (; exp; exp >>= 1) {
        if (exp & 1) result = result * base % MOD;
        base = base * base % MOD;
    }
    return result;
}

ll sum_p(ll p, ll r) {
    if (!p) return 0;
    if (!r) return 1;
    if (r % 2 == 1) {
        // (1 + p + p^2 + ... + p^((r-1)/2)) + p^((r+1)/2) * (1 + p + p^2 + ... + p^((r-1)/2))
        return (1 + fast_pow(p, (r + 1) / 2)) * sum_p(p, (r - 1) / 2) % MOD;
    }
    // (1 + p + p^2 + ... + p^(r/2)) + p^(r/2) * (1 + p + p^2 + ... + p^(r/2)) - p^(r/2)
    ll half = fast_pow(p, r / 2);
    return ((1 + half) * sum_p(p, r / 2) % MOD - half + MOD) % MOD;
}

int main() {
    cin >> A >> B;
    vector<pair<int, int>> fs;
    factors(A, fs);
    ll ans = 1;
    for (const auto& [x, y]: fs) {
        // 0 ~ y * B
        ans = ans * sum_p(x, y * B) % MOD;
    }
    cout << ans << endl;
    return 0;
}
