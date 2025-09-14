//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<bool> subsequenceSumAfterCapping(const vector<int> &nums, int k) {
    int n = nums.size();
    vector<int> freq(n + 1);
    for (const auto &num : nums) {
      ++freq[num];
    }
    vector<bool> ans(n);
    vector<bool> dp(k + 1);
    dp[0] = true;
    int used = 0;
    for (int i = 1; i <= n; ++i) {
      for (int j = 0; j < freq[i]; ++j) {
        for (int x = k; x >= i; --x) {
          dp[x] = dp[x] || dp[x - i];
        }
      }
      used += freq[i];
      for (int j = 0; j <= min(k / i, n - used); ++j) {
        if (dp[k - j * i]) {
          ans[i - 1] = true;
          break;
        }
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
  int k = json::parse(inputArray.at(1));
  return solution.subsequenceSumAfterCapping(nums, k);
}
