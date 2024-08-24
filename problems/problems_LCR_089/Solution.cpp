//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int rob(vector<int> &nums) {
    int dp_not_rob = 0, dp_rob = 0;
    for (int num : nums) {
      int tmp = dp_not_rob;
      dp_not_rob = max(dp_not_rob, dp_rob);
      dp_rob = tmp + num;
    }
    return max(dp_not_rob, dp_rob);
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
