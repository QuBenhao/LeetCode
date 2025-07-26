//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int countHillValley(const vector<int> &nums) {
    auto diffToSign = [](int diff) {
      if (diff > 0)
        return 1;
      if (diff < 0)
        return -1;
      return 0;
    };

    int ans = 0;
    int n = nums.size();
    for (int i = 0, last = nums[0], last_diff = 0; i < n; ++i) {
      while (i < n - 1 && nums[i] == nums[i + 1]) {
        ++i;
      }
      int cur_diff = diffToSign(nums[i] - last);
      if (last_diff * cur_diff < 0) {
        ++ans;
      }
      last = nums[i];
      last_diff = cur_diff;
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
  return solution.countHillValley(nums);
}
