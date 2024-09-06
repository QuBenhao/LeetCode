//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool isBipartite(vector<vector<int>> &graph) {
    int n = static_cast<int>(graph.size());
    vector<int> color = vector<int>(n, -1);
    function<bool(int, int)> dfs = [&](int node, int c) {
      if (color[node] != -1) {
        return color[node] == c;
      }
      color[node] = c;
      int nxt = 1 ^ c;
      for (int other : graph[node]) {
        if (!dfs(other, nxt)) {
          return false;
        }
      }
      return true;
    };
    for (int i = 0; i < n; i++) {
      if (color[i] != -1) {
        continue;
      }
      if (!dfs(i, 0)) {
        return false;
      }
    }
    return true;
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
  vector<vector<int>> graph = json::parse(inputArray.at(0));
  return solution.isBipartite(graph);
}
