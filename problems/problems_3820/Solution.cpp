//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int specialNodes(int n, vector<vector<int>> &edges, int x, int y, int z) {
    vector<vector<int>> graph(n);
    for (const auto &edge : edges) {
      int u = edge[0], v = edge[1];
      graph[u].emplace_back(v);
      graph[v].emplace_back(u);
    }
    auto dfs = [&graph](this auto &&dfs, int node, int pa,
                        vector<int> &dis) -> void {
      for (const auto &child : graph[node]) {
        if (child == pa)
          continue;
        dis[child] = dis[node] + 1;
        dfs(child, node, dis);
      }
    };

    vector<int> dis_x(n), dis_y(n), dis_z(n);
    dis_x[x] = 0, dis_y[y] = 0, dis_z[z] = 0;
    dfs(x, -1, dis_x);
    dfs(y, -1, dis_y);
    dfs(z, -1, dis_z);

    int ans = 0;
    for (int i = 0; i < n; ++i) {
      vector<long long> vec{dis_x[i], dis_y[i], dis_z[i]};
      ranges::sort(vec);
      if (vec[0] * vec[0] + vec[1] * vec[1] == vec[2] * vec[2])
        ++ans;
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
  int n = json::parse(inputArray.at(0));
  vector<vector<int>> edges = json::parse(inputArray.at(1));
  int x = json::parse(inputArray.at(2));
  int y = json::parse(inputArray.at(3));
  int z = json::parse(inputArray.at(4));
  return solution.specialNodes(n, edges, x, y, z);
}
