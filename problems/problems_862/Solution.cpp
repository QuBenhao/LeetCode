//go:build ignore
#include "cpp/common/Solution.h"
#include <deque>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int shortestSubarray(const vector<int> &nums, int k) {
    deque<pair<int64_t, int>> dq;
    int ans = INT_MAX;
    int n = nums.size();
    dq.emplace_back(0, -1);  // (sum, index)
    int64_t prefixSum = 0;
    for (int i = 0; i < n; ++i) {
      prefixSum += nums[i];
      while (!dq.empty() && dq.front().first <= prefixSum - k) {
        ans = min(ans, i - dq.front().second);
        dq.pop_front();
      }
      while (!dq.empty() && dq.back().first >= prefixSum) {
        dq.pop_back();
      }
      dq.emplace_back(prefixSum, i);
    }
    return ans == INT_MAX ? -1 : ans;
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
  int k = json::parse(inputArray.at(1));
  return solution.shortestSubarray(nums, k);
}
