//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool canPartitionKSubsets(vector<int> &nums, int k) {
    int n = static_cast<int>(nums.size());
    int sum = accumulate(nums.begin(), nums.end(), 0);
    if (sum % k != 0) {
      return false;
    }
    int target = sum / k;
    for (int num : nums) {
      if (num > target) {
        return false;
      }
    }
    int all_picked = (1 << n) - 1;
    vector<int> dp(all_picked + 1, -1);
    dp[0] = 0;
    for (int mask = 0; mask <= all_picked; mask++) {
      for (int j = 0; j < n; j++) {
        if ((mask >> j & 1) != 0) {
          int before = mask & ~(1 << j);
          if (dp[before] != -1 && dp[before] + nums[j] <= target) {
            dp[mask] = (dp[before] + nums[j]) % target;
          }
        }
      }
    }
    return dp[all_picked] == 0;
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
  return solution.canPartitionKSubsets(nums, k);
}
