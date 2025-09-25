//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int triangleNumber(vector<int> &nums) {
    ranges::sort(nums);
    int n = nums.size();
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = i - 1, k = 0; k < j; --j) {
        while (k < j && nums[k] + nums[j] <= nums[i])
          ++k;
        ans += j - k;
      }
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
  return solution.triangleNumber(nums);
}
