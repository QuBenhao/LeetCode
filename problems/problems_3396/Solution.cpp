//go:build ignore
#include "cpp/common/Solution.h"

#include <set>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minimumOperations(vector<int> &nums) {
    auto s = set<int>();
    int ans = 0;
    for (int idx = nums.size() - 1; idx >= 0; idx--) {
      if (s.contains(nums[idx])) {
        ans = idx / 3 + 1;
        break;
      }
      s.insert(nums[idx]);
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
  return solution.minimumOperations(nums);
}
