//
// Created by benhao on 2025/12/19.
//
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <array>

constexpr int MOD = 998244353;
using namespace std;

int fast_pow(int64_t base, int64_t exp, int64_t mod) {
  int64_t res = 1;
  while (exp) {
    if (exp & 1) res = (1LL * res * base) % mod;
    base = (1LL * base * base) % mod;
    exp >>= 1;
  }
  return static_cast<int>(res);
}

class TreeAncestor {
  int n;
  int m;
  vector<int> depth;
  void dfs(int node, int parent,
           const unordered_map<int, vector<array<int, 2>>> &graph) {
    pa[node][0] = parent;

    auto it = graph.find(node);
    if (it == graph.end()) {
      return;
    }
    for (auto& [k, v]: presum) {
      v[node] = (v[node] + fast_pow(distance[node], k, MOD)) % MOD;
      if (parent != -1) {
        v[node] = (v[parent] + v[node]) % MOD;
      }
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
  vector<vector<int>> pa;
  vector<int> distance;
  std::unordered_map<int, vector<int>> presum;

  explicit TreeAncestor(const vector<vector<int>> &edges, const std::unordered_set<int>& ks)
      : n(edges.size() + 1), m(32 - __builtin_clz(n)), depth(n, 0),
        pa(n, vector<int>(m, -1)), distance(n, 0) {
    for (const auto& k: ks) {
      presum[k] = vector<int>(n);
    }
    unordered_map<int, vector<array<int, 2>>> graph(n);
    for (const auto &edge : edges) {
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

  int getDistance(int u, int v, int k) {
    int lca = getLCA(u, v);
    return ((((presum[k][u] + presum[k][v]) % MOD - presum[k][lca] + MOD) % MOD) - (lca == 0 ? 0 : presum[k][getKthAncestor(lca, 1)]) + MOD) % MOD;
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
  int n;
  std::cin >> n;
  std::vector<std::vector<int>> edges(n - 1);
  for (int i = 0; i < n - 1; ++i) {
    int u, v;
    std::cin >> u >> v;
    --u, --v;
    edges[i] = {u, v};
  }
  int m;
  std::cin >> m;
  std::unordered_set<int> ks;
  std::vector<std::array<int, 3>> query(m);
  for (int i = 0; i < m; ++i) {
    int x, y, k;
    std::cin >> x >> y >> k;
    ks.insert(k);
    query[i] = {x - 1, y - 1, k};
  }
  TreeAncestor ta(edges, ks);
  for (const auto& ar: query) {
    std::cout << ta.getDistance(ar[0], ar[1], ar[2]) << std::endl;
  }
}