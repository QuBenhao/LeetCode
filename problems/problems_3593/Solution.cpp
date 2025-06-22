//go:build ignore
#include "cpp/common/Solution.h"
#include <utility>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minIncrease(int n, vector<vector<int>> &edges, vector<int> &cost) {
    vector<vector<int>> graph(n);
    for (const auto &edge : edges) {
      int u = edge[0], v = edge[1];
      graph[u].push_back(v);
      graph[v].push_back(u);
    }

    auto dfs = [&graph, &cost](this auto &&dfs, int node, int parent) -> pair<int64_t, int> {
      int64_t cur_sum = 0;
      int cur_cost = 0, max_count = 0, other_count = 0;
      for (auto child : graph[node]) {
        if (child == parent)
          continue;
        auto [child_sum, child_cost] = dfs(child, node);
        cur_cost += child_cost;
        if (child_sum > cur_sum) {
          cur_sum = child_sum;
          other_count += max_count;
          max_count = 1;
        } else if (child_sum == cur_sum) {
          ++max_count;
        } else {
          ++other_count;
        }
      }
      cur_sum += cost[node];
      cur_cost += other_count;
      return make_pair(cur_sum, cur_cost);
    };

    return dfs(0, -1).second;
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
  vector<int> cost = json::parse(inputArray.at(2));
  return solution.minIncrease(n, edges, cost);
}
