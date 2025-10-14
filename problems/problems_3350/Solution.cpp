//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxIncreasingSubarrays(const vector<int> &nums) {
    int ans = 0;
    int last = 0, cur = 1, n = nums.size();
    for (int i = 1; i <= n; ++i) {
      if (i == n || nums[i - 1] >= nums[i]) {
        ans = max(ans, min(last, cur));
        ans = max(ans, cur / 2);
        last = cur;
        cur = 1;
        continue;
      }
      ++cur;
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
  return solution.maxIncreasingSubarrays(nums);
}
