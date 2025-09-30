//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int triangularSum(vector<int> &nums) {
    int n = nums.size();
    for (int i = n - 1; i > 0; --i) {
      for (int j = 0; j < i; ++j) {
        nums[j] = (nums[j] + nums[j + 1]) % 10;
      }
    }
    return nums[0];
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
  return solution.triangularSum(nums);
}
