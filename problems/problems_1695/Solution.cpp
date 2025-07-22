//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maximumUniqueSubarray(const vector<int> &nums) {
    int ans = 0, cur = 0, left = 0;
    unordered_set<int> seen;
    for (const auto& num : nums) {
      while (seen.contains(num)) {
        seen.erase(nums[left]);
        cur -= nums[left];
        ++left;
      }
      seen.insert(num);
      cur += num;
      ans = max(ans, cur);
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
  return solution.maximumUniqueSubarray(nums);
}
