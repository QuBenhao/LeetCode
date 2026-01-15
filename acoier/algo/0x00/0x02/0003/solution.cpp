//
// Created by benhao on 2026/1/15.
// 例题: 递归实现排列型枚举 acwing94
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))

int n;
vector<bool> used;

void dfs(const int cur, vector<int>& path) {
    if (cur == n) {
        for (const auto& v: path) cout << v << " ";
        cout << endl;
        return;
    }
    // 要求字典序，所以只能按数枚举，不能按位值枚举
    // for (int i = 0; i < n; ++i) {
    //     if (path[i] != -1) continue;
    //     path[i] = cur;
    //     dfs(cur + 1, path);
    //     path[i] = -1;
    // }
    for (int i = 1; i <= n; ++i) {
        if (used[i]) continue;
        used[i] = true;
        path[cur] = i;
        dfs(cur + 1, path);
        used[i] = false;
    }
}

int main() {
    cin >> n;
    vector path(n, -1);
    used.resize(n, false);
    dfs(0, path);
    return 0;
}