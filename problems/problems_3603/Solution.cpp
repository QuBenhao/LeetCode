//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long minCost(int m, int n, vector<vector<int>> &waitCost) {
    vector<vector<int64_t>> dp(m, vector<int64_t>(n, INT64_MAX));
    dp[0][0] = 1;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (i < m - 1) {
          dp[i + 1][j] = min(dp[i + 1][j],
                             dp[i][j] + (i + 2) * (j + 1) + waitCost[i + 1][j]);
        }
        if (j < n - 1) {
          dp[i][j + 1] = min(dp[i][j + 1],
                             dp[i][j] + (i + 1) * (j + 2) + waitCost[i][j + 1]);
        }
      }
    }
    return dp[m - 1][n - 1] - waitCost[m - 1][n - 1];
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
  int m = json::parse(inputArray.at(0));
  int n = json::parse(inputArray.at(1));
  vector<vector<int>> waitCost = json::parse(inputArray.at(2));
  return solution.minCost(m, n, waitCost);
}
