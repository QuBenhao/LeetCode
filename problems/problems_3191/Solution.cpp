//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minOperations(vector<int> &nums) {
    int ans = 0, n = static_cast<int>(nums.size());
    for (int i = 0; i < n - 2; i++) {
      if (nums[i] == 0) {
        ans++;
        nums[i + 1] ^= 1;
        nums[i + 2] ^= 1;
      }
    }
    return nums[n - 2] == 1 && nums[n - 1] == 1 ? ans : -1;
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
  return solution.minOperations(nums);
}
