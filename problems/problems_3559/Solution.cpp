//go:build ignore
#include "cpp/common/Solution.h"
#include <bit>
#include <vector>

using namespace std;
using json = nlohmann::json;

constexpr int MOD = 1e9 + 7;

class TreeLca {
  vector<int> depth;
  vector<vector<int>> pa;

public:
  explicit TreeLca(const vector<vector<int>> &edges) {
    const int n = edges.size() + 1;
    const int m = bit_width((unsigned)n);

    vector<vector<int>> graph(n);
    for (const auto &edge : edges) {
      graph[edge[0] - 1].emplace_back(edge[1] - 1);
      graph[edge[1] - 1].emplace_back(edge[0] - 1);
    }

    depth.resize(n);
    pa.resize(m, vector<int>(n, -1));

    auto dfs = [&](this auto &&dfs, int x, int fa) -> void {
      pa[0][x] = fa;
      for (const auto &y : graph[x]) {
        if (y != fa) {
          depth[y] = depth[x] + 1;
          dfs(y, x);
        }
      }
    };
    dfs(0, -1);
    for (int i = 0; i < m - 1; ++i) {
      for (int x = 0; x < n; ++x) {
        if (int p = pa[i][x]; p != -1) {
          pa[i + 1][x] = pa[i][p];
        }
      }
    }
  }

  int get_k_parent(int x, int k) {
    for (; k > 0 && x >= 0; k &= k - 1) {
      x = pa[countr_zero((unsigned(k)))][x];
    }
    return x;
  }

  int get_lca(int x, int y) {
    if (depth[x] > depth[y]) {
      swap(x, y);
    }
    // 对齐
    y = get_k_parent(y, depth[y] - depth[x]);
    if (y == x) {
      return x;
    }
    for (int i = pa.size() - 1; i >= 0; --i) {
      int px = pa[i][x], py = pa[i][y];
      if (px != py) {
        x = px;
        y = py;
      }
    }
    return pa[0][x];
  }

  int get_distance(int x, int y) {
    return depth[x] + depth[y] - depth[get_lca(x, y)] * 2;
  }
};

class Solution {
  int fast_pow(int base, int exp) {
    int res = 1;
    while (exp > 0) {
      if (exp & 1) {
        res = (1LL * res * base) % MOD;
      }
      base = (1LL * base * base) % MOD;
      exp >>= 1;
    }
    return res;
  }

public:
  vector<int> assignEdgeWeights(const vector<vector<int>> &edges,
                                const vector<vector<int>> &queries) {
    TreeLca ta(edges);
    vector<int> ans(queries.size(), 0);
    for (int i = 0; i < queries.size(); ++i) {
      const auto &query = queries[i];
      int u = query[0] - 1, v = query[1] - 1;
      int dist = ta.get_distance(u, v);
      ans[i] = dist == 0 ? 0 : fast_pow(2, dist - 1);
    }
    return ans;
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
  return solution.assignEdgeWeights(edges, queries);
}
