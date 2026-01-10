//
// Created by benhao on 2026/1/10.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define lowbit(x) ((x)&(-(x)))

int main() {
    int t, n;
    cin >> t;
    vector<int> arr;
    for (int i = 0; i < t; ++i) {
        cin >> n;
        arr.resize(n);
        for (int j = 0; j < n; ++j) {
            cin >> arr[j];
        }
        if (arr[0] == 0 && arr[n - 1] == 0) {
            cout << "Bob" << endl;
        } else {
            cout << "Alice" << endl;
        }
    }
    return 0;
}