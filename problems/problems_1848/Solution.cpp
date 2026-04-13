//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int getMinDistance(const vector<int> &nums, int target, int start) {
    int n = nums.size();
    int ans = n + 1;
    for (int i = 0; i < n; ++i) {
      if (target == nums[i]) {
        ans = min(ans, abs(i - start));
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
  int target = json::parse(inputArray.at(1));
  int start = json::parse(inputArray.at(2));
  return solution.getMinDistance(nums, target, start);
}
