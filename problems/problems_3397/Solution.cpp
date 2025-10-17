//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxDistinctElements(vector<int> &nums, int k) {
    ranges::sort(nums.begin(), nums.end());
    int ans = 0, cur = nums[0] - k - 1;
    for (const auto &num : nums) {
      if (num + k == cur) {
        continue;
      }
      ++ans;
      if (num - k > cur) {
        cur = num - k;
      } else {
        ++cur;
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
  int k = json::parse(inputArray.at(1));
  return solution.maxDistinctElements(nums, k);
}
