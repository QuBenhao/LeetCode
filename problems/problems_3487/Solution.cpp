//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxSum(const vector<int> &nums) {
    unordered_set<int> seen;
    int sum = 0, mx = -101;
    for (const auto &num : nums) {
      if (seen.count(num)) {
        continue;
      }
      seen.insert(num);
      if (num > 0) {
        sum += num;
      }
      mx = max(mx, num);
    }
    return mx > 0 ? sum : mx;
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
  return solution.maxSum(nums);
}
