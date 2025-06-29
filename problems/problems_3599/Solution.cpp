//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minXor(const vector<int> &nums, int k) {
    int n = nums.size();
    vector<int> pre_xor(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      pre_xor[i + 1] = pre_xor[i] ^ nums[i];
    }
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, INT_MAX));
    // Base case: 1 part
    for (int i = 0; i < n; ++i) {
      dp[i][1] = pre_xor[n] ^ pre_xor[i];
    }
    dp[n][1] = 0;  // edge case: empty suffix

    for (int kk = 2; kk <= k; ++kk) {
      for (int i = 0; i <= n - kk; ++i) {
        for (int j = i + 1; j <= n - kk + 1; ++j) {
          int left = pre_xor[j] ^ pre_xor[i];
          int right = dp[j][kk - 1];
          dp[i][kk] = min(dp[i][kk], max(left, right));
        }
      }
    }
    return dp[0][k];
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
  vector<int> nums = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.minXor(nums, k);
}
