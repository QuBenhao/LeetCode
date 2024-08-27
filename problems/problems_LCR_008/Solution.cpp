//go:build ignore
#include "cpp/common/Solution.h"
#include <queue>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minSubArrayLen(int target, vector<int> &nums) {
    int n = static_cast<int>(nums.size());
    int ans = n + 1;
    queue<int> q;
    int cur_sum = 0;
    for (int num : nums) {
      q.push(num);
      cur_sum += num;
      while (cur_sum >= target) {
        ans = min(ans, static_cast<int>(q.size()));
        cur_sum -= q.front();
        q.pop();
      }
    }
    return ans == n + 1 ? 0 : ans;
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
  int target = json::parse(inputArray.at(0));
  vector<int> nums = json::parse(inputArray.at(1));
  return solution.minSubArrayLen(target, nums);
}
