//go:build ignore
#include "cpp/common/Solution.h"
#include <queue>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minCost(int n, const vector<vector<int>> &edges) {
    vector<unordered_map<int, int>> graph(n);
    for (const auto &edge : edges) {
      int u = edge[0], v = edge[1], cost = edge[2];
      graph[u][v] =
          graph[u].find(v) != graph[u].end() ? min(graph[u][v], cost) : cost;
      graph[v][u] = graph[v].find(u) != graph[v].end()
                        ? min(graph[v][u], cost * 2)
                        : cost * 2;
    }
    vector<int> dist(n, INT_MAX);
    dist[0] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>,
                   greater<pair<int, int>>>
        pq;
    pq.push({0, 0});
    while (!pq.empty()) {
      const auto [cost, u] = pq.top();
      pq.pop();
      if (u == n - 1) {
        return cost;
      }
      if (cost > dist[u])
        continue;
      for (const auto &[v, w] : graph[u]) {
        int newCost = cost + w;
        if (newCost < dist[v]) {
          dist[v] = newCost;
          pq.push({newCost, v});
        }
      }
    }
    return -1;
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
  return solution.minCost(n, edges);
}
