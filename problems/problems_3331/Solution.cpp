//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> findSubtreeSizes(const vector<int> &parent, const string &s) {
    int n = parent.size();
    vector<int> ans(n, 1);
    vector<vector<int>> graph(n);
    for (int i = 1; i < n; ++i) {
      graph[parent[i]].push_back(i);
    }
    int mapping[26];
    ranges::fill(mapping, -1);

    auto dfs = [&](auto&& dfs, int node) -> void {
      int old = mapping[s[node] - 'a'];
      mapping[s[node] - 'a'] = node;
      for (int child : graph[node]) {
        dfs(dfs, child);
      }
      mapping[s[node] - 'a'] = old;
      int pa = old != -1 ? old : parent[node];
      if (pa != -1) {
        ans[pa] += ans[node];
      }
    };
    dfs(dfs, 0);
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
  vector<int> parent = json::parse(inputArray.at(0));
  string s = json::parse(inputArray.at(1));
  return solution.findSubtreeSizes(parent, s);
}
