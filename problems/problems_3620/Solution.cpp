//go:build ignore
#include "cpp/common/Solution.h"
#include <climits>
#include <queue>
#include <utility>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int findMaxPathScore(const vector<vector<int>> &edges,
                       const vector<bool> &online, long long k) {
    int n = online.size();
    vector<vector<pair<int, int>>> graph(n);
    int right = 0;
    for (const auto &edge : edges) {
      int u = edge[0], v = edge[1], cost = edge[2];
      if (online[u] && online[v]) {
        graph[u].emplace_back(v, cost);
        right = max(right, cost);
      }
    }
    for (auto &g : graph) {
      sort(g.begin(), g.end(),
           [](const pair<int, int> &a, const pair<int, int> &b) {
             return a.second > b.second;
           });
    }
    auto helper = [&](int min_cost) {
      vector<int64_t> distance(n, LLONG_MAX);
      distance[0] = 0;
      priority_queue<pair<int64_t, int>, vector<pair<int64_t, int>>, greater<>>
          pq;
      pq.emplace(0, 0);
      while (!pq.empty()) {
        auto [dist, u] = pq.top();
        if (u == n - 1) {
          return true;
        }
        pq.pop();
        if (dist > distance[u])
          continue;
        for (const auto &[v, cost] : graph[u]) {
          if (cost < min_cost)
            break;
          int64_t new_dist = dist + cost;
          if (new_dist > k || new_dist >= distance[v])
            continue;
          distance[v] = new_dist;
          pq.emplace(new_dist, v);
        }
      }
      return false;
    };

    int left = 0;
    while (left < right) {
      int mid = left + (right - left + 1) / 2;
      if (helper(mid)) {
        left = mid;
      } else {
        right = mid - 1;
      }
    }
    return left > 0 ? left : -1;
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
  vector<bool> online = json::parse(inputArray.at(1));
  long long k = json::parse(inputArray.at(2));
  return solution.findMaxPathScore(edges, online, k);
}
