//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long zeroFilledSubarray(const vector<int> &nums) {
    uint64_t ans = 0;
    int left = 0, n = nums.size();
    for (int right = 0; right < n; ++right) {
      while (left < n && nums[left] != 0) {
        ++left;
      }
      right = left;
      while (right < n && nums[right] == 0) {
        ++right;
      }
      ans += 1LL * (right - left) * (right - left + 1) / 2;
      left = right;
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
  return solution.zeroFilledSubarray(nums);
}
