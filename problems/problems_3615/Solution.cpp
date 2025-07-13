//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxLen(int n, const vector<vector<int>> &edges, const string &label) {
    vector<vector<int>> graph(n);
    for (const auto &edge : edges) {
      graph[edge[0]].push_back(edge[1]);
      graph[edge[1]].push_back(edge[0]);
    }

    vector<vector<vector<int>>> dp(
        n, vector<vector<int>>(n, vector<int>(1 << n, -1)));
    auto dfs = [&graph, &dp, &label](this auto &&dfs, int x, int y,
                                     int explored) -> int {
      if (dp[x][y][explored] != -1) {
        return dp[x][y][explored];
      }
      int ans = 0;
      for (int nx : graph[x]) {
        if (explored & (1 << nx)) {
          continue;  // already explored
        }
        for (int ny : graph[y]) {
          if (nx == ny || (explored & (1 << ny)) || label[nx] != label[ny]) {
            continue;  // already explored or same node or not palindrome
          }
          if (nx > ny) {
            swap(nx, ny);
          }
          ans = max(ans, dfs(nx, ny, explored | (1 << nx) | (1 << ny)) + 2);
        }
      }
      dp[x][y][explored] = ans;
      return ans;
    };

    int ans = 1;
    for (int i = 0; i < n; ++i) {
      ans = max(ans, dfs(i, i, 1 << i) + 1);
      for (int j : graph[i]) {
        if (i > j) {
          continue;  // avoid duplicate pairs
        }
        if (label[i] == label[j]) {
          ans = max(ans, dfs(i, j, (1 << i) | (1 << j)) + 2);
        }
      }
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
  string label = json::parse(inputArray.at(2));
  return solution.maxLen(n, edges, label);
}
