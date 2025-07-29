//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int longestSubarray(const vector<int> &nums) {
    int ans = 0, cur = 0, mx = 0;
    for (const auto &num : nums) {
      if (num > mx) {
        ans = cur = 1;
        mx = num;
      } else if (num == mx) {
        ans = max(++cur, ans);
      } else {
        cur = 0;
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
