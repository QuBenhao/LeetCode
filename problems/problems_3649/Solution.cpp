//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long perfectPairs(const vector<int> &nums) {
    vector<int> abs_nums;
    for (int num : nums) {
      abs_nums.push_back(abs(num));
    }
    ranges::sort(abs_nums);
    uint64_t ans = 0;
    int n = abs_nums.size();
    for (int l = 0, r = 1; r < n; ++r) {
      while (abs_nums[l] * 2 < abs_nums[r]) {
        ++l;
      }
      ans += r - l;
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
  return solution.perfectPairs(nums);
}
