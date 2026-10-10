# 差分数组

## 二维差分数组

```python
from typing import *


def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
    diff = [[0] * (n + 1) for _ in range(n + 1)]
    for x1, y1, x2, y2 in queries:
        diff[x1][y1] += 1
        diff[x1][y2 + 1] -= 1
        diff[x2 + 1][y1] -= 1
        diff[x2 + 1][y2 + 1] += 1
    ans = [[0] * n for _ in range(n)]
    # 还原原数组 - 方法1：直接计算前缀和
    for i in range(n):
        for j in range(n):
            # 当前位置的值
            ans[i][j] = diff[i][j]
            # 加上左边的值
            if i > 0:
                ans[i][j] += ans[i - 1][j]
            # 加上上边的值
            if j > 0:
                ans[i][j] += ans[i][j - 1]
            # 减去左上角的值（因为加了两次）
            if i > 0 and j > 0:
                ans[i][j] -= ans[i - 1][j - 1]

    return ans
```
```c++
//
// Created by benhao on 2025/12/23.
//

#include <cstdio>
#include <vector>
using namespace std;

// Add v to each element from [x1, y1] to [x2, y2].
void add(vector<vector<int> > &diff, int n, int m, int x1, int y1, int x2, int y2, int v) {
    diff[x1][y1] += v;
    if (x2 < n) diff[x2 + 1][y1] -= v;
    if (y2 < m) diff[x1][y2 + 1] -= v;
    if (x2 < n && y2 < m) diff[x2 + 1][y2 + 1] += v;
}

// Execute this after all modifications and before all queries.
void prefix_sum(const vector<vector<int> > &diff, vector<vector<int> >& a, int n, int m) {
    a = diff;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j) a[i][j] += a[i - 1][j];

    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j) a[i][j] += a[i][j - 1];
}

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    vector matrix(n + 1, vector<int>(n + 1, 0));
    for (int i = 0; i < m; ++i) {
        int x1, x2, y1, y2;
        scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
        add(matrix, n, n, x1, y1, x2, y2, 1);
    }
    vector<vector<int> > a;
    prefix_sum(matrix, a, n, n);
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (j < n) {
                printf("%d ", a[i][j]);
            } else {
                printf("%d\n", a[i][j]);
            }
        }
    }
    return 0;
}
```

## 树差分
```c++
//
// Created by benhao on 2025/12/24.
//
#include <iostream>
#include <vector>
#include <unordered_map>
#include <array>
#include <algorithm>

using namespace std;

class TreeAncestor {
    int n;
    int m;
    vector<int> depth;

    void dfs(const int node, int parent,
             const unordered_map<int, vector<array<int, 2> > > &graph) {
        pa[node][0] = parent;

        auto it = graph.find(node);
        if (it == graph.end()) {
            return;
        }
        for (const auto &[child, weight]: it->second) {
            if (child == parent)
                continue;
            depth[child] = depth[node] + 1;
            distance[child] = distance[node] + weight;
            dfs(child, node, graph);
        }
    }

public:
    vector<vector<int> > pa;
    vector<uint64_t> distance;
    vector<int> diff;

    explicit TreeAncestor(const vector<vector<int> > &edges)
        : n(edges.size() + 1), m(32 - __builtin_clz(n)), depth(n, 0),
          pa(n, vector<int>(m, -1)), distance(n, 0), diff(n, 0) {
        unordered_map<int, vector<array<int, 2> > > graph(n);
        for (const auto &edge: edges) {
            int u = edge[0], v = edge[1], w = edge.size() > 2 ? edge[2] : 1;
            graph[u].push_back({v, w});
            graph[v].push_back({u, w});
        }

        dfs(0, -1, graph);
        for (int j = 1; j < m; ++j) {
            for (int i = 0; i < n; ++i) {
                if (pa[i][j - 1] != -1) {
                    pa[i][j] = pa[pa[i][j - 1]][j - 1];
                }
            }
        }
    }

    ~TreeAncestor() = default;

    int getKthAncestor(int node, int k) {
        for (; k > 0 && node != -1; k &= k - 1) {
            node = pa[node][31 - __builtin_clz(k & -k)];
        }
        return node;
    }

    int getLCA(int u, int v) {
        if (depth[u] > depth[v])
            swap(u, v);
        int diff = depth[v] - depth[u];
        v = getKthAncestor(v, diff);
        if (u == v)
            return u;
        for (int j = m - 1; j >= 0; --j) {
            if (pa[u][j] != pa[v][j]) {
                u = pa[u][j];
                v = pa[v][j];
            }
        }
        return pa[u][0];
    }

    int getDistance(int u, int v) {
        int lca = getLCA(u, v);
        return distance[u] + distance[v] - 2 * distance[lca];
    }

    int findDistance(int u, uint64_t d) {
        d = distance[u] - d;
        for (int j = m - 1; j >= 0; --j) {
            int p = pa[u][j];
            if (p != -1 && distance[p] >= d) {
                u = p;
            }
        }
        return u;
    }

    void update(int x, int y, int  v) {
        diff[x] += v;
        diff[y] += v;
        int lca = getLCA(x, y);
        diff[lca] -= v;
        int parent = getKthAncestor(lca, 1);
        if (parent != -1) {
            diff[parent] -= v;
        }
    }

    void final_dfs(const int node, const int parent, std::vector<std::vector<int>>& graph) {
        for (int child: graph[node]) {
            if (child == parent) {
                continue;
            }
            final_dfs(child, node, graph);
            diff[node] += diff[child];
        }
    }
};

int main() {
    int n;
    std::cin >> n;
    std::vector<int> visit(n);
    for (int i = 0; i < n; ++i) {
        int u;
        std::cin >> u;
        --u;
        visit[i] = u;
    }
    std::vector edges(n - 1, std::vector<int>(2));
    std::vector<std::vector<int>> graph(n);
    for (int i = 0; i < n - 1; ++i) {
        // std::cin >> edges[i][0] >> edges[i][1];
        int u, v;
        std::cin >> u >> v;
        --u, --v;
        edges[i][0] = u;
        edges[i][1] = v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    TreeAncestor ta(edges);
    for (int i = 0; i < n - 1; ++i) {
        ta.update(visit[i], visit[i + 1], 1);
        ta.update(visit[i + 1], visit[i + 1], -1);
    }
    ta.final_dfs(0, -1, graph);
    for (const auto& d: ta.diff) {
        std::cout << d << std::endl;
    }
    return 0;
}
```