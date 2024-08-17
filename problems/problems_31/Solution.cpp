//go:build ignore
#include "cpp/common/Solution.h"
#include <deque>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  void nextPermutation(vector<int> &nums) {
    int n = static_cast<int>(nums.size());
    int idx = n - 1;
    while (idx > 0 && nums[idx - 1] >= nums[idx]) {
      idx--;
    }
    if (idx == 0) {
      reverse(nums.begin(), nums.end());
      return;
    }
    int i = n - 1;
    while (i >= idx && nums[i] <= nums[idx - 1]) {
      i--;
    }
    swap(nums[i], nums[idx - 1]);
    reverse(nums.begin() + idx, nums.end());
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
  solution.nextPermutation(nums);
  return nums;
}
