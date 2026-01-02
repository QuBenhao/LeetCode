//
// Created by benhao on 2026/1/1.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n, m;
vector<int> score;
unordered_map<int, vector<int>> graph;
vector<vector<int>> dp;

int dfs(int u) { // 返回统计当前根有多少个节点
    int p = 1; // 加上自己
    dp[u][1] = score[u];
    for (const auto& v : graph[u]) {
        int sz = dfs(v); // 子树有多少个节点
        for (int i = min(p, m + 1); i; --i) { // 当前选了多少个， 至多选m + 1个
            for (int j = 1; j <= sz && i + j <= m + 1; ++j) { // 至少取一个，不然没有遍历的意义
                dp[u][i + j] = max(dp[u][i + j], dp[u][i] + dp[v][j]); // 递推方程
            }
        }
        p += sz;
    }
    return p;
}

int main() {
    cin >> n >> m;
    score.resize(n+1);
    dp = vector (n+1, vector(m+2, 0));
    graph.clear();
    // 添加一个0节点为所有树的根
    for (int i = 1; i <= n; ++i) {
        int k, s;
        cin >> k >> s;
        score[i] = s;
        graph[k].push_back(i);
    }
    dfs(0);
    cout << dp[0][m + 1] << endl;
    return 0;
}