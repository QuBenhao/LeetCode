//go:build ignore
#include "cpp/common/Solution.h"
#include <cstdint>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxProduct(vector<int> &nums) {
    int ans = nums[0];
    int dp_max = nums[0], dp_min = nums[0];
    for (int i = 1; i < static_cast<int>(nums.size()); i++) {
      int tmp = dp_max;
      dp_max = max(max(dp_max * nums[i], dp_min * nums[i]), nums[i]);
      dp_min = min(min(tmp * nums[i], dp_min * nums[i]), nums[i]);
      ans = max(ans, dp_max);
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
  return solution.maxProduct(nums);
}
