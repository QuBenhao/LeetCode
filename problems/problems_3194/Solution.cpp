//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  double minimumAverage(vector<int> &nums) {
    sort(nums.begin(), nums.end());
    int n = static_cast<int>(nums.size());
    int ans = nums[0] + nums[n - 1];
    for (int i = 1; i < n / 2; i++) {
      ans = min(ans, nums[i] + nums[n - i - 1]);
    }
    return static_cast<double>(ans) / 2.0;
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
  return solution.minimumAverage(nums);
}
