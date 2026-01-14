//
// Created by benhao on 2026/1/14.
// 例题: 递归实现组合型枚举 acwing93
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))

int n;

void dfs(const int cur, int remain, vector<int>& path) {
    if (remain == 0 || cur == n + 1) {
        for (const auto& v: path) cout << v << " ";
        cout << endl;
        return;
    }
    // 可选
    path.push_back(cur);
    dfs(cur + 1, remain - 1, path);
    path.pop_back();
    if (n - cur + 1 == remain) {
        // 不可不选
        return;
    }
    // 可以不选
    dfs(cur + 1, remain, path);
}

int main() {
    int m;
    cin >> n >> m;
    vector<int> path;
    dfs(1, m, path);
    return 0;
}
