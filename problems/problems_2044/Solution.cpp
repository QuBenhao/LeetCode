//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int countMaxOrSubsets(const vector<int> &nums) {
    int n = nums.size();
    int mask = 1 << n;
    vector<int> dp(mask);
    int ans = 0, maxOr = 0;
    for (int i = 1; i < mask; ++i) {
      int lowbit = i & -i;
      int prev = i - lowbit, idx = __builtin_ctz(lowbit);
      dp[i] = dp[prev] | nums[idx];
      if (dp[i] > maxOr) {
        maxOr = dp[i];
        ans = 1;
      } else if (dp[i] == maxOr) {
        ++ans;
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
  vector<int> nums = json::parse(inputArray.at(0));
  return solution.countMaxOrSubsets(nums);
}
