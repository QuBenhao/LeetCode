//go:build ignore
#include "cpp/common/Solution.h"
#include <climits>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxDotProduct(const vector<int> &nums1, const vector<int> &nums2) {
    int m = nums1.size(), n = nums2.size();
    vector dp(2, vector<int>(n + 1, INT_MIN));
    for (int i = 0; i < m; ++i) {
      int cur = i % 2, nxt = 1 ^ cur;
      for (int j = 0; j < n; ++j) {
        dp[nxt][j + 1] = max(max(dp[cur][j], 0) + nums1[i] * nums2[j],
                             max(dp[nxt][j], dp[cur][j + 1]));
      }
    }
    return dp[m % 2][n];
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
  vector<int> nums1 = json::parse(inputArray.at(0));
  vector<int> nums2 = json::parse(inputArray.at(1));
  return solution.maxDotProduct(nums1, nums2);
}
