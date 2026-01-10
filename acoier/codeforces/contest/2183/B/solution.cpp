//
// Created by benhao on 2026/1/10.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define lowbit(x) ((x)&(-(x)))

int main() {
    int t;
    cin >> t;
    int n, k, v;
    unordered_set<int> s;
    while (t-- > 0) {
        s.clear();
        cin >> n >> k;
        for (int i = 0; i < n; ++i) {
            cin >> v;
            s.insert(v);
        }
        int i;
        for (i = 0; i < k - 1; ++i) {
            if (!s.contains(i)) {
                break;
            }
        }
        cout << i << endl;
    }
    return 0;
}