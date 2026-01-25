//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> rotateElements(vector<int> &nums, int k) {
    vector<int> values;
    for (const auto &num : nums) {
      if (num < 0)
        continue;
      values.emplace_back(num);
    }
    if (values.empty()) {
      return nums;
    }
    int l = values.size();
    for (int i = 0, j = k % l; i < nums.size(); ++i) {
      if (nums[i] < 0)
        continue;
      nums[i] = values[j];
      j = (j + 1) % l;
    }
    return nums;
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
  return solution.rotateElements(nums, k);
}
