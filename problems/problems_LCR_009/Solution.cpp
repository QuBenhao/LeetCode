//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int numSubarrayProductLessThanK(vector<int> &nums, int k) {
    int ans = 0;
    int cur = 1;
    int left = 0, right = 0;
    int n = static_cast<int>(nums.size());
    while (right < n) {
      cur *= nums[right];
      while (left <= right && cur >= k) {
        cur /= nums[left];
        left++;
      }
      ans += right - left + 1;
      right++;
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
  int k = json::parse(inputArray.at(1));
  return solution.numSubarrayProductLessThanK(nums, k);
}
