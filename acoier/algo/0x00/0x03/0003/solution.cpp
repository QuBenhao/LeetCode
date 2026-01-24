//
// Created by benhao on 2026/1/24.
// 例题: Tallest Cow acwing101
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))


int main() {
    int N, P, H, M;
    cin >> N >> P >> H >> M;
    vector<int> diff(N);
    diff[0] = H;
    unordered_set<int> explored;
    int a, b;
    while (M--) {
        cin >> a >> b;
        --a, --b;
        const int mn = min(a, b), mx = max(a, b);
        const int key = mn * 10000 + mx;
        if (explored.find(key) != explored.end()) continue;
        explored.insert(key);
        --diff[mn + 1];
        ++diff[mx];
    }
    int cur = 0;
    for (int i = 0; i < N; ++i) {
        cur += diff[i];
        cout << cur << endl;
    }
    return 0;
}