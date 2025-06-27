//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<string> summaryRanges(const vector<int> &nums) {
    vector<string> result;
    int n = nums.size();
    int left, right;
    for (int i = 0; i <= n; ++i) {
      if (i == 0 || i == n || nums[i] != nums[i - 1] + 1) {
        if (i != 0) {
          result.push_back(left == right
                               ? to_string(left)
                               : to_string(left) + "->" + to_string(right));
        }
        if (i < n) {
          left = right = nums[i];
        }
      } else {
        ++right;
      }
    }
    return result;
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
  return solution.summaryRanges(nums);
}
