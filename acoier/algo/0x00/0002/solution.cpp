//
// Created by benhao on 2026/1/13.
// 例题: a*b acwing90
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))

ll fast_mul(ll a, ll b, ll p) {
    ll ans = 0LL;
    for (; b; b >>= 1) {
        if (b & 1) ans = (ans + a) % p;
        a = a * 2 % p;
    }
    return ans;
}

int main() {
    ll a, b, p;
    cin >> a >> b >> p;
    cout << fast_mul(a, b, p) << endl;
    return 0;
}
