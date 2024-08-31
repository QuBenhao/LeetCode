//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int rob(vector<int> &nums) {
    size_t n = nums.size();
    int ans = 0, dp_rob = nums[0], dp_not_rob = nums[0];
    for (size_t i = 2; i + 1 < n; i++) {
      int temp = dp_rob;
      dp_rob = dp_not_rob + nums[i];
      dp_not_rob = max(temp, dp_not_rob);
    }
    ans = max(dp_rob, dp_not_rob);
    dp_rob = 0, dp_not_rob = 0;
    for (size_t i = 1; i < n; i++) {
      int temp = dp_rob;
      dp_rob = dp_not_rob + nums[i];
      dp_not_rob = max(temp, dp_not_rob);
    }
    return max(ans, max(dp_rob, dp_not_rob));
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
  return solution.rob(nums);
}
