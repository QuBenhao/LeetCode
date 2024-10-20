//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int smallestRangeI(vector<int> &nums, int k) {
    int min_val = nums[0], max_val = nums[0];
    for (int num : nums) {
      min_val = min(min_val, num);
      max_val = max(max_val, num);
    }
    return max(0, max_val - min_val - 2 * k);
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
  return solution.smallestRangeI(nums, k);
}
