//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> minBitwiseArray(const vector<int> &nums) {
    vector<int> ans(nums.size(), -1);
    for (size_t i = 0; i < nums.size(); ++i) {
      if (!(nums[i] & 1))
        continue;
      const int v = ((nums[i] + 1) & -(nums[i] + 1)) - 1;
      ans[i] = (nums[i] - v) | v >> 1;
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
  return solution.minBitwiseArray(nums);
}
