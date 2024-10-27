//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
private:
  int find(vector<int> &parent, int x) {
    if (parent[x] != x) {
      parent[x] = find(parent, parent[x]);
    }
    return parent[x];
  }

public:
  vector<int> findRedundantConnection(vector<vector<int>> &edges) {
    int n = edges.size();
    vector<int> parent(n + 1);
    for (int i = 1; i <= n; i++) {
      parent[i] = i;
    }
    for (auto &edge : edges) {
      int x = edge[0], y = edge[1];
      if (find(parent, x) != find(parent, y)) {
        parent[find(parent, x)] = find(parent, y);
      } else {
        return edge;
      }
    }
    return {};
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
  return solution.findRedundantConnection(edges);
}
