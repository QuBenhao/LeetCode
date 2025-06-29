//go:build ignore
#include "cpp/common/Solution.h"
#include <climits>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minSubArrayLen(int target, vector<int> &nums) {
    int ans = INT_MAX, prefix = 0, left = 0;
    int n = nums.size();
    for (int right = 0; right < n; ++right) {
      prefix += nums[right];
      while (prefix >= target) {
        ans = min(ans, right - left + 1);
        prefix -= nums[left++];
      }
    }
    return ans == INT_MAX ? 0 : ans;
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
  int target = json::parse(inputArray.at(0));
  vector<int> nums = json::parse(inputArray.at(1));
  return solution.minSubArrayLen(target, nums);
}
