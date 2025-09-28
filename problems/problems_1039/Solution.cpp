//go:build ignore
#include "cpp/common/Solution.h"
#include <climits>
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minScoreTriangulation(const vector<int> &values) {
    int n = values.size();
    vector<vector<int>> dp(n, vector<int>(n, INT_MAX));
    for (int i = 0; i < n; ++i) {
      dp[i][i] = 0;
      if (i < n - 1) {
        dp[i][i + 1] = 0;
      }
    }
    for (int len = 2; len < n; ++len) {
      for (int l = 0; l < n - len; ++l) {
        int r = l + len;
        for (int k = l + 1; k < r; ++k) {
          dp[l][r] = min(dp[l][r], dp[l][k] + dp[k][r] +
                                       values[l] * values[k] * values[r]);
        }
      }
    }
    return dp[0][n - 1];
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
  vector<int> values = json::parse(inputArray.at(0));
  return solution.minScoreTriangulation(values);
}
