//
// Created by benhao on 2026/1/14.
// 例题:  递归实现指数型枚举 acwing92
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))

int n;

void dfs(int cur, vector<int>& path) {
    if (cur > n) {
        for (const auto& v: path) cout << v << " ";
        cout << endl;
        return;
    }
    // 不选当前
    dfs(cur + 1, path);
    // 选当前
    path.emplace_back(cur);
    dfs(cur + 1, path);
    path.pop_back();
}

int main() {
    cin >> n;
    vector<int> path;
    dfs(1, path);
    return 0;
}
