//go:build ignore
#include "cpp/common/Solution.h"

#include <algorithm>
#include <numeric>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  double largestSumOfAverages(vector<int> &nums, int k) {
    int n = nums.size();
    vector<vector<double>> dp(n + 1, vector<double>(k + 1));
    vector<int> prefixSum(n + 1, 0);
    partial_sum(nums.begin(), nums.end(), prefixSum.begin() + 1);
    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= min(i, k); ++j) {
        if (j == 1) {
          dp[i][j] = static_cast<double>(prefixSum[i]) / i;
        } else {
          for (int l = j - 1; l <= i; ++l) {
            dp[i][j] =
                max(dp[i][j], dp[l][j - 1] + static_cast<double>(prefixSum[i] -
                                                                 prefixSum[l]) /
                                                 (i - l));
          }
        }
      }
    }
    return dp[n][k];
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
  return solution.largestSumOfAverages(nums, k);
}
