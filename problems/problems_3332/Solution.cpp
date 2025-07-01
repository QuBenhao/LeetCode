//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxScore(int n, int k, const vector<vector<int>> &stayScore,
               const vector<vector<int>> &travelScore) {
    vector<vector<int>> dp(n, vector<int>(2, 0));
    for (int j = 0; j < k; ++j) {
      for (int i = 0; i < n; ++i) {
        for (int nc = 0; nc < n; ++nc) {
          if (i == nc) {
            dp[nc][(j + 1) % 2] = max(dp[nc][(j + 1) % 2], dp[i][j % 2] + stayScore[j][i]);
          } else {
            dp[nc][(j + 1) % 2] = max(dp[nc][(j + 1) % 2], dp[i][j % 2] + travelScore[i][nc]);
          }
        }
      }
    }
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      ans = max(ans, dp[i][k % 2]);
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
  int k = json::parse(inputArray.at(1));
  vector<vector<int>> stayScore = json::parse(inputArray.at(2));
  vector<vector<int>> travelScore = json::parse(inputArray.at(3));
  return solution.maxScore(n, k, stayScore, travelScore);
}
