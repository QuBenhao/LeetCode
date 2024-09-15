//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int numberOfPoints(vector<vector<int>> &nums) {
    sort(nums.begin(), nums.end());
    int ans = 0, cur = nums[0][0] - 1;
    for (auto &p : nums) {
      int left = p[0], right = p[1];
      if (left > cur) {
        ans += right - left + 1;
        cur = right;
      } else if (right > cur) {
        ans += right - cur;
        cur = right;
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
  vector<vector<int>> nums = json::parse(inputArray.at(0));
  return solution.numberOfPoints(nums);
}
