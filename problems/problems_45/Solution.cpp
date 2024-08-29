//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int jump(vector<int> &nums) {
    int ans = 0;
    for (size_t cur = 0, nxt = 0, n = nums.size(); nxt + 1 < n; ans++) {
      size_t tmp = nxt;
      for (size_t i = cur; i <= tmp; i++) {
        nxt = max(nxt, i + nums[i]);
      }
      cur = tmp + 1;
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
  return solution.jump(nums);
}
