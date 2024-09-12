//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxNumOfMarkedIndices(vector<int> &nums) {
    sort(nums.begin(), nums.end());
    int left = 0, n = static_cast<int>(nums.size());
    for (int right = (n + 1) / 2; right < n; ++right) {
      if (nums[left] * 2 <= nums[right]) {
        ++left;
      }
    }
    return left << 1;
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
  return solution.maxNumOfMarkedIndices(nums);
}
