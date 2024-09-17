//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int numBusesToDestination(vector<vector<int>> &routes, int source,
                            int target) {
    if (source == target)
      return 0;
    int n = routes.size();
    vector<vector<int>> g(n);
    unordered_map<int, vector<int>> to_routes;
    for (int i = 0; i < n; ++i) {
      for (int site : routes[i]) {
        for (int j : to_routes[site]) {
          g[i].push_back(j);
          g[j].push_back(i);
        }
        to_routes[site].push_back(i);
      }
    }
    vector<int> dis(n, -1);
    queue<int> q;
    for (int i : to_routes[source]) {
      dis[i] = 1;
      q.push(i);
    }
    while (!q.empty()) {
      int x = q.front();
      q.pop();
      for (int y : g[x]) {
        if (dis[y] == -1) {
          dis[y] = dis[x] + 1;
          q.push(y);
        }
      }
    }
    int ans = INT_MAX;
    for (int i : to_routes[target]) {
      if (dis[i] != -1) {
        ans = min(ans, dis[i]);
      }
    }
    return ans == INT_MAX ? -1 : ans;
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
  vector<vector<int>> routes = json::parse(inputArray.at(0));
  int source = json::parse(inputArray.at(1));
  int target = json::parse(inputArray.at(2));
  return solution.numBusesToDestination(routes, source, target);
}
