//
// Created by benhao on 2025/12/19.
//
#include <iostream>
#include <vector>
#include <array>
#include <unordered_map>

class TreeAncestor {
  int n;
  int m;
  std::vector<int> depth;
  void dfs(int node, int parent,
           const std::unordered_map<int, std::vector<std::array<int, 2>>> &graph) {
    pa[node][0] = parent;

    auto it = graph.find(node);
    if (it == graph.end()) {
      return;
    }
    for (const auto &[child, weight] : it->second) {
      if (child == parent)
        continue;
      depth[child] = depth[node] + 1;
      distance[child] = distance[node] + weight;
      dfs(child, node, graph);
    }
  }

public:
  std::vector<std::vector<int>> pa;
  std::vector<uint64_t> distance;

  explicit TreeAncestor(const std::vector<std::vector<int>> &edges)
      : n(edges.size() + 1), m(32 - __builtin_clz(n)), depth(n, 0),
        pa(n, std::vector<int>(m, -1)), distance(n, 0) {
    std::unordered_map<int, std::vector<std::array<int, 2>>> graph(n);
    for (const auto &edge : edges) {
      int u = edge[0], v = edge[1], w = edge[2];
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
      std::swap(u, v);
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
};

int main() {
  int n, m;
  std::cin >> n >> m;
  std::vector<std::vector<int>> edges(n - 1);
  for (int i = 0; i < n - 1; ++i) {
    int u, v, w;
    std::cin >> u >> v >> w;
    edges[i] = {u - 1, v - 1, w};
  }
  TreeAncestor ta(edges);
  for (int i = 0; i < m; ++i) {
    int x, y;
    std::cin >> x >> y;
    --x; --y;
    std::cout << ta.getDistance(x, y) << std::endl;
  }
  return 0;
}