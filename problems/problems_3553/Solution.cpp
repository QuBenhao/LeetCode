//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class TreeAncestor {
  int n;
  int m;
  vector<vector<int>> pa;
  vector<int> depth;
  vector<int> distance;
  void dfs(int node, int parent,
           const unordered_map<int, vector<array<int, 2>>> &graph) {
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
  explicit TreeAncestor(const vector<vector<int>> &edges)
      : n(edges.size()+1), m(32 - __builtin_clz(n)), pa(n, vector<int>(m, -1)),
        depth(n, 0), distance(n, 0) {
    unordered_map<int, vector<array<int, 2>>> graph(n);
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
};

class Solution {
public:
  vector<int> minimumWeight(const vector<vector<int>> &edges,
                            const vector<vector<int>> &queries) {
    TreeAncestor treeAncestor = TreeAncestor(edges);
    vector<int> result(queries.size());
    for (int i = 0; i < queries.size(); ++i) {
      int u = queries[i][0], v = queries[i][1], k = queries[i][2];
      result[i] =
          (treeAncestor.getDistance(u, v) + treeAncestor.getDistance(u, k) +
           treeAncestor.getDistance(v, k)) /
          2;
    }
    return result;
  }
};

json leetcode::qubh::Solve(string input_json_values) {
  vector<string> inputArray;
  size_t pos = input_json_values.find('\n');
  while (pos != string::npos) {
    inputArray.push_back(input_json_values.substr(0, pos));
    input_json_values = input_json_values.substr(pos + 1);
    pos = input_json_values.find('\n');
  }
  inputArray.push_back(input_json_values);

  Solution solution;
  vector<vector<int>> edges = json::parse(inputArray.at(0));
  vector<vector<int>> queries = json::parse(inputArray.at(1));
  return solution.minimumWeight(edges, queries);
}
