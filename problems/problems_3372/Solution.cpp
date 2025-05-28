//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
  vector<vector<int>> buildTree(const vector<vector<int>> &edges) {
    vector<vector<int>> g(edges.size() + 1);
    for (auto &e : edges) {
      int x = e[0], y = e[1];
      g[x].push_back(y);
      g[y].push_back(x);
    }
    return g;
  }
  int dfs(int node, int pa, int k, const vector<vector<int>> &g) {
    if (k < 0) {
      return 0;
    }
    if (k == 0) {
      return 1;
    }
    k--;
    int res = 1;
    for (int neigh : g[node]) {
      if (neigh == pa) {
        continue;
      }
      res += dfs(neigh, node, k, g);
    }
    return res;
  }

public:
  vector<int> maxTargetNodes(vector<vector<int>> &edges1, vector<vector<int>> &edges2, int k) {
    auto t2 = buildTree(edges2);
    int max2 = 0;
    for (int i = 0; i < edges2.size() + 1; i++) {
      max2 = max(max2, dfs(i, -1, k - 1, t2));
    }
    auto t1 = buildTree(edges1);
    vector<int> ans(edges1.size() + 1);
    for (int i = 0; i < edges1.size() + 1; i++) {
      ans[i] = max2 + dfs(i, -1, k, t1);
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
  vector<vector<int>> edges1 = json::parse(inputArray.at(0));
  vector<vector<int>> edges2 = json::parse(inputArray.at(1));
  int k = json::parse(inputArray.at(2));
  return solution.maxTargetNodes(edges1, edges2, k);
}
