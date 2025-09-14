//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

constexpr int MOD = 1e9 + 7;

class Solution {
public:
  int countStableSubsequences(const vector<int> &nums) {
    int dp0 = 0, dp1 = 0, dp00 = 0, dp01 = 0, dp10 = 0, dp11 = 0;
    for (const auto &num : nums) {
      if ((num & 1) == 0) {
        dp00 = ((dp00 + dp0) % MOD + dp10) % MOD;
        dp10 = ((((dp10 + dp1) % MOD + dp01) % MOD) + dp11) % MOD;
        dp0 = (dp0 + 1) % MOD;
      } else {
        dp11 = ((dp11 + dp1) % MOD + dp01) % MOD;
        dp01 = (((dp01 + dp0) % MOD + dp00) % MOD + dp10) % MOD;
        dp1 = (dp1 + 1) % MOD;
      }
    }
    return (((((dp0 + dp1) % MOD + dp00) % MOD + dp01) % MOD + dp10) % MOD +
            dp11) %
           MOD;
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
  return solution.countStableSubsequences(nums);
}
