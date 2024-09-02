//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long maxStrength(vector<int> &nums) {
    int64_t mx = nums[0], mn = nums[0];
    for (int i = 1; i < static_cast<int>(nums.size()); i++) {
      int64_t tmp = mx, num = static_cast<int64_t>(nums[i]);
      mx = max(max(max(num, tmp * num), mn * num), max(mx, mn));
      mn = min(min(min(num, tmp * num), mn * num), min(mx, mn));
    }
    return mx;
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
  return solution.maxStrength(nums);
}
