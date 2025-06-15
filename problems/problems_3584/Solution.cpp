//go:build ignore
#include "cpp/common/Solution.h"
#include <climits>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long maximumProduct(vector<int> &nums, int m) {
    int n = nums.size();
    vector<int> preMax(n), preMin(n);
    preMax[0] = nums[0];
    preMin[0] = nums[0];
    long long ans = LLONG_MIN;
    for (int i = 0; i < n; ++i) {
      if (i > 0) {
        preMax[i] = max(preMax[i - 1], nums[i]);
        preMin[i] = min(preMin[i - 1], nums[i]);
      }
      if (i >= m - 1) {
        ans = max(ans, 1LL * preMax[i - m + 1] * nums[i]);
        ans = max(ans, 1LL * preMin[i - m + 1] * nums[i]);
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
  int m = json::parse(inputArray.at(1));
  return solution.maximumProduct(nums, m);
}
