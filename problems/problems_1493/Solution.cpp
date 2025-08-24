//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int longestSubarray(const vector<int> &nums) {
    int n = nums.size();
    if (all_of(nums.begin(), nums.end(), [](int x) { return x == 1; })) {
      return n - 1;
    }
    int ans = 0;
    for (int i = 0, last = 0, cur = 0; i <= n; ++i) {
      if (i == n || nums[i] != 1) {
        ans = max(ans, last + cur);
        last = cur;
        cur = 0;
      } else {
        ++cur;
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
  return solution.longestSubarray(nums);
}
