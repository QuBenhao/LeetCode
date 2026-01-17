//
// Created by benhao on 2026/1/16.
// 例题: 非递归实现组合型枚举 acwing93
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))

/**
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

dfs(1, m, path);
 */

int st[100010], top = 0, address = 0;
void call(int x, int ret_addr) {
    int old_top = top;
    st[++top] = x; // 存参数
    st[++top] = ret_addr; // 存返回处理
    st[++top] = old_top; // 存之前的top
}

int ret() {
    int ret_addr = st[top - 1]; // 读返回
    top = st[top]; // 重置原来的top
    return ret_addr;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> chosen;
    call(1, 0); // 相当于dfs(1)
    while (top) {
        int x = st[top - 2]; // 当前计算的参数
        switch (address) { // address按原来的dfs拆分, 原来函数里有两个dfs, 所以有三种address
            case 0: {
                if (chosen.size() > m || chosen.size() + (n - x + 1) < m) {
                    address = ret(); // 结束计算, return
                    continue;
                }
                if (x == n + 1) {
                    for (const auto& v: chosen) cout << v << " ";
                    cout << endl;
                    address = ret();
                    continue;
                }
                chosen.push_back(x);
                call(x + 1, 1); // 这里返回要有不一样的处理, 所以不是0
                address = 0; // 重新进dfs(x+1)
                continue;
            }
            case 1: {
                chosen.pop_back();
                call(x + 1, 2); // 这里的返回有不一样的处理, 所以不是0, 1
                address = 0; // 重新进dfs(x+1)
                continue;
            }
            case 2: {
                address = ret(); // 原来最后的return
            }
        }
    }
    return 0;
}