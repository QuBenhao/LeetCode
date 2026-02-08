//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

constexpr long long INF = 1e18;

class Solution {
public:
  long long maxScore(const vector<int> &nums1, const vector<int> &nums2, int k) {
    int m = nums1.size(), n = nums2.size();
    vector dp(m + 1, vector(n + 1, vector<long long>(k + 1, -INF)));
    dp[0][0][0] = 0;
    for (int i = 0; i <= m; ++i) {
      for (int j = 0; j <= n; ++j) {
        for (int r = 0; r <= k; ++r) {
          if (i > 0)
            dp[i][j][r] = max(dp[i][j][r], dp[i - 1][j][r]);
          if (j > 0)
            dp[i][j][r] = max(dp[i][j][r], dp[i][j - 1][r]);
          if (i > 0 && j > 0 && r > 0) {
            dp[i][j][r] = max(dp[i][j][r], dp[i - 1][j - 1][r - 1] +
                                               1LL * nums1[i - 1] * nums2[j - 1]);
          }
        }
      }
    }
    return dp[m][n][k];
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
  int k = json::parse(inputArray.at(2));
  return solution.maxScore(nums1, nums2, k);
}
