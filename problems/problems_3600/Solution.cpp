//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

class UnionFind {
  vector<int> fa;
  vector<int> size;

public:
  int cc;
  explicit UnionFind(int n) : fa(n), size(n, 1), cc(n) {
    for (int i = 0; i < n; i++) {
      fa[i] = i;
    }
  }

  // copy constructor
  UnionFind(const UnionFind &uf) : fa(uf.fa), size(uf.size), cc(uf.cc) {}

  int find(int x) {
    if (fa[x] != x) {
      fa[x] = find(fa[x]);
    }
    return fa[x];
  }

  bool merge(int x, int y) {
    int px = find(x), py = find(y);
    if (px == py) {
      return false;
    }
    fa[px] = py;
    size[py] += size[px];
    cc--;
    return true;
  }

  int get_size(int x) { return size[find(x)]; }
};

class Solution {
public:
  int maxStability(int n, const vector<vector<int>> &edges, int k) {
    UnionFind all_uf(n);
    UnionFind uf(n);
    vector<vector<int>> must_edges, optional_edges;
    int right = 200000;
    for (const auto &edge : edges) {
      int u = edge[0], v = edge[1], w = edge[2], must = edge[3];
      if (must) {
        must_edges.push_back({u, v, w});
        if (!uf.merge(u, v)) {
          return -1;
        }
        right = min(right, w);
      } else {
        optional_edges.push_back({u, v, w});
      }
      all_uf.merge(u, v);
    }

    if (all_uf.cc > 1) {
      return -1;
    }

    sort(
        optional_edges.begin(), optional_edges.end(),
        [](const vector<int> &a, const vector<int> &b) { return a[2] < b[2]; });

    auto check = [&uf, &optional_edges](int k, int mid) {
      UnionFind cur_uf(uf);
      auto fit = lower_bound(
          optional_edges.begin(), optional_edges.end(), mid,
          [](const vector<int> &edge, int value) { return edge[2] < value; });
      for (auto it = fit; it != optional_edges.end(); ++it) {
        int u = (*it)[0], v = (*it)[1];
        if (cur_uf.merge(u, v) && cur_uf.cc == 1) {
          return true;
        }
      }
      auto double_it = lower_bound(
          optional_edges.begin(), optional_edges.end(), (mid + 1) / 2,
          [](const vector<int> &edge, int value) { return edge[2] < value; });
      for (auto it = double_it; it != fit; ++it) {
        if (k == 0) {
          break;
        }
        int u = (*it)[0], v = (*it)[1];
        if (cur_uf.merge(u, v)) {
          if (cur_uf.cc == 1) {
            return true;
          }
          --k;
        }
      }
      return cur_uf.cc == 1;
    };

    int left = 1;
    while (left < right) {
      int mid = left + (right - left + 1) / 2;
      if (check(k, mid)) {
        left = mid;
      } else {
        right = mid - 1;
      }
    }
    return left;
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
  int n = json::parse(inputArray.at(0));
  vector<vector<int>> edges = json::parse(inputArray.at(1));
  int k = json::parse(inputArray.at(2));
  return solution.maxStability(n, edges, k);
}
