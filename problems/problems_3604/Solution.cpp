//go:build ignore
#include "cpp/common/Solution.h"
#include "cpp/models/TreeNode.h"

#include <queue>
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minTime(int n, const vector<vector<int>> &edges) {
    vector<vector<tuple<int, int, int>>> graph(n);
    for (const auto &edge : edges) {
      graph[edge[0]].emplace_back(edge[1], edge[2], edge[3]);
    }
    priority_queue<pair<int, int>> pq;
    vector<int> dist(n, INT_MAX);
    pq.push({0, 0});  // {time, node}
    dist[0] = 0;
    while (!pq.empty()) {
      auto [time, node] = pq.top();
      time = -time;
      if (node == n - 1) {
        return time;
      }
      pq.pop();
      for (const auto &[next_node, start, end] : graph[node]) {
        if (time <= end) {
          int nxt_time = max(time, start) + 1;
          if (nxt_time < dist[next_node]) {
            dist[next_node] = nxt_time;
            pq.push({-nxt_time, next_node});
          }
        }
      }
    }
    return -1;  // If no path found
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
  return solution.minTime(n, edges);
}
