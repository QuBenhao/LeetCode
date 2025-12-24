//
// Created by benhao on 2025/12/24.
//

#include <iostream>

using namespace std;

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
        diff[lca] -= 2 * v;
    }

    void final_dfs(const int node, const int parent, std::vector<std::vector<int>>& graph, int& sum, int& ans) {
        for (int child: graph[node]) {
            if (child == parent) {
                continue;
            }
            final_dfs(child, node, graph, sum, ans);
            diff[node] += diff[child];
        }
        sum += getDistance(node, parent) * diff[node];
        ans = max(ans, getDistance(node, parent) * diff[node]);
    }
};

int main() {
    int n, m;
    cin >> n >> m;
    std::vector edges(n - 1, std::vector<int>(3));
    std::vector<std::vector<int>> graph(n);
    for (int i = 0; i < n - 1; ++i) {
        int u, v, t;
        cin >> u >> v >> t;
        --u, --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
        edges[i][0] = u;
        edges[i][1] = v;
        edges[i][2] = t;
    }
    TreeAncestor ta(edges);
    vector<int> arr(m);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u, --v;
        arr[i] = ta.getDistance(u, v);
        ta.update(u, v, 1);
    }

    int ans = 0, sum = 0;
    ta.final_dfs(0, -1, graph,sum, ans);
    std::cout << sum - ans << std::endl;
    return 0;
}