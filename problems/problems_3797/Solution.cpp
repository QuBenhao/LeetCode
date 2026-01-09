//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;
using json = nlohmann::json;

constexpr int MOD = 1e9 + 7;

class Solution {
public:
  int numberOfRoutes(const vector<string> &grid, const int d) {
    const int n = grid.size(), m = grid[0].length();
    const int D = floor(sqrt(d * d - 1));
    vector dp(2, vector(m, 0));
    // dp[i][j][0] = sum(dp[i+1][j-D][0], dp[i+1][j+D][0]) +
    // sum(dp[i+1][j-D][1],dp[i+1][j+D][1])
    for (int i = n - 1; i >= 0; --i) {
      int cur_idx = i % 2, pre_idx = 1 ^ cur_idx;
      vector<int> pre(m + 1, 0);
      for (int j = 0; j < m; ++j) {
        pre[j + 1] = (pre[j] + dp[pre_idx][j]) % MOD;
      }
      for (int j = 0; j < m; ++j) {
        if (grid[i][j] == '#') {
          dp[cur_idx][j] = 0;
          continue;
        }
        if (i == n - 1) {
          dp[cur_idx][j] = 1;
        } else {
          dp[cur_idx][j] =
              ((pre[min(j + D + 1, m)] - pre[max(0, j - D)]) % MOD + MOD) % MOD;
        }
      }
      ranges::fill(pre, 0);
      for (int j = 0; j < m; ++j) {
        pre[j + 1] = (pre[j] + dp[cur_idx][j]) % MOD;
      }
      for (int j = 0; j < m; ++j) {
        if (grid[i][j] == '#') {
          continue;
        }
        dp[cur_idx][j] =
            (((pre[min(j + d + 1, m)]) % MOD - pre[max(0, j - d)]) % MOD +
             MOD) %
            MOD;
      }
    }
    int ans = 0;
    for (int j = 0; j < m; ++j) {
      ans = (ans + dp[0][j]) % MOD;
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
  vector<string> grid = json::parse(inputArray.at(0));
  int d = json::parse(inputArray.at(1));
  return solution.numberOfRoutes(grid, d);
}
