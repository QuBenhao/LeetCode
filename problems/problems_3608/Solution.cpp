//go:build ignore
#include "cpp/common/Solution.h"

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
  int minTime(int n, vector<vector<int>> &edges, int k) {
    UnionFind uf(n);
    sort(
        edges.begin(), edges.end(),
        [](const vector<int> &a, const vector<int> &b) { return a[2] > b[2]; });
    for (const auto &edge : edges) {
      uf.merge(edge[0], edge[1]);
      if (uf.cc < k) {
        return edge[2];
      }
    }
    return 0;
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
  return solution.minTime(n, edges, k);
}
