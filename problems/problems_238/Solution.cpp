//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> productExceptSelf(vector<int> &nums) {
    size_t n = nums.size();
    vector<int> output(n, 1);
    for (size_t i = 1; i < n; i++) {
      output[i] = output[i - 1] * nums[i - 1];
    }
    int right = 1;
    for (int i = n - 1; i >= 0; i--) {
      output[i] *= right;
      right *= nums[i];
    }
    return output;
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
  return solution.productExceptSelf(nums);
}
