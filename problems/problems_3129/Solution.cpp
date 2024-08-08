//go:build ignore
#include "cpp/common/Solution.h"
#include <array>

using std::vector;
using json = nlohmann::json;

class Solution {
public:
  int numberOfStableArrays(int zero, int one, int limit) {
    const int MOD = 1'000'000'007;
    vector<vector<array<int, 2>>> dp(zero + 1, vector<array<int, 2>>(one + 1));
    for (int i = 1; i <= min(limit, zero); i++) {
      dp[i][0][0] = 1;
    }
    for (int j = 1; j <= min(limit, one); j++) {
      dp[0][j][1] = 1;
    }
    for (int i = 1; i <= zero; i++) {
      for (int j = 1; j <= one; j++) {
        dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD;
        if (i > limit) {
          dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + MOD) % MOD;
        }
        dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD;
        if (j > limit) {
          dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + MOD) % MOD;
        }
      }
    }
    return (dp[zero][one][0] + dp[zero][one][1]) % MOD;
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
  int zero = json::parse(inputArray.at(0));
  int one = json::parse(inputArray.at(1));
  int limit = json::parse(inputArray.at(2));
  return solution.numberOfStableArrays(zero, one, limit);
}
