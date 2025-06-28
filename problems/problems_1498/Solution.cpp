//go:build ignore
#include "cpp/common/Solution.h"

#include <ranges>

using namespace std;
using json = nlohmann::json;

const int MOD = 1e9 + 7;

class Solution {
public:
  int numSubseq(vector<int> &nums, int target) {
    ranges::sort(nums);
    int n = nums.size();
    vector<int> pow2(n, 1);
    for (int i = 1; i < n; ++i) {
      pow2[i] = (pow2[i - 1] * 2) % MOD;
    }
    int left = 0, right = n - 1;
    int ans = 0;
    while (left <= right) {
      while (right >= left && nums[left] + nums[right] > target) {
        --right;
      }
      if (right < left)
        break;
      ans = (ans + pow2[right - left]) % MOD;
      ++left;
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
  return solution.numSubseq(nums, target);
}
