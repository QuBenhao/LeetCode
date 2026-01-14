//
// Created by benhao on 2026/1/12.
// 例题: a^b acwing89
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int fast_pow(int a, int b, int p) {
    int res = 1 % p;
    for (; b; b >>= 1) {
        if (b & 1) res = (1LL * res * a) % p;
        a = (1LL * a * a) % p;
    }
    return res;
}

int main() {
    int a, b, p;
    cin >> a >> b >> p;
    cout << fast_pow(a, b, p) << endl;
    return 0;
}