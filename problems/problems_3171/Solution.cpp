//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minimumDifference(vector<int> &nums, int k) {
    int ans = abs(nums[0] - k), n = static_cast<int>(nums.size());
    for (int i = 1; i < n; i++) {
      ans = min(ans, abs(nums[i] - k));
      for (int j = i - 1; j >= 0 && (nums[j] | nums[i]) != nums[j]; j--) {
        nums[j] |= nums[i];
        ans = min(ans, abs(nums[j] - k));
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
  int k = json::parse(inputArray.at(1));
  return solution.minimumDifference(nums, k);
}
