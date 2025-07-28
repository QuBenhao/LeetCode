//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> smallestSubarrays(vector<int> &nums) {
    int n = nums.size();
    vector<int> ans(n, 1);
    for (int i = 0; i < n; ++i) {
      int x = nums[i];
      for (int j = i - 1; j >= 0; --j) {
        if ((nums[j] | x) == nums[j]) {
          break;
        }
        nums[j] |= x;
        ans[j] = i - j + 1;
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
  return solution.smallestSubarrays(nums);
}
