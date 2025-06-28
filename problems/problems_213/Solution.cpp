//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
  int robHelper(const vector<int> &nums, int start, int end) {
    int rob = nums[start], notRob = 0;
    for (int i = start + 1; i <= end; ++i) {
      int newRob = notRob + nums[i];
      notRob = max(rob, notRob);
      rob = newRob;
    }
    return max(rob, notRob);
  }

public:
  int rob(const vector<int> &nums) {
    int n = nums.size();
    if (n == 1)
      return nums[0];
    return max(robHelper(nums, 0, n - 2), robHelper(nums, 1, n - 1));
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
  return solution.rob(nums);
}
