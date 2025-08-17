//go:build ignore
#include "cpp/common/Solution.h"
#include <climits>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minCost(const vector<vector<int>> &grid, int k) {
    int m = grid.size(), n = grid[0].size();
    vector<vector<vector<int>>> dp(
        k + 1, vector<vector<int>>(m, vector<int>(n, INT_MAX)));
    map<int, vector<pair<int, int>>> graph;
    dp[0][0][0] = 0;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        graph[-grid[i][j]].emplace_back(i, j);
        if (i + 1 < m) {
          dp[0][i + 1][j] = min(dp[0][i + 1][j], dp[0][i][j] + grid[i + 1][j]);
        }
        if (j + 1 < n) {
          dp[0][i][j + 1] = min(dp[0][i][j + 1], dp[0][i][j] + grid[i][j + 1]);
        }
      }
    }
    for (int kk = 1; kk <= k; ++kk) {
      int mn = INT_MAX;
      for (const auto &[_, points] : graph) {
        for (const auto &[x, y] : points) {
          mn = min(mn, dp[kk - 1][x][y]);
        }
        for (const auto &[x, y] : points) {
          dp[kk][x][y] = mn;
        }
      }
      for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
          if (i + 1 < m) {
            dp[kk][i + 1][j] =
                min(dp[kk][i + 1][j], dp[kk][i][j] + grid[i + 1][j]);
          }
          if (j + 1 < n) {
            dp[kk][i][j + 1] =
                min(dp[kk][i][j + 1], dp[kk][i][j] + grid[i][j + 1]);
          }
        }
      }
    }
    int ans = INT_MAX;
    for (int kk = 0; kk <= k; ++kk) {
      ans = min(ans, dp[kk][m - 1][n - 1]);
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
  vector<vector<int>> grid = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.minCost(grid, k);
}
