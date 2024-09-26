//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool isInterleave(string s1, string s2, string s3) {
    size_t m = s1.size(), n = s2.size();
    if (m + n != s3.size()) {
      return false;
    }
    vector<vector<bool>> dp(m + 1, vector<bool>(n + 1));
    dp[0][0] = true;
    for (size_t i = 1; i <= m && s1[i - 1] == s3[i - 1]; i++) {
      dp[i][0] = true;
    }
    for (size_t i = 1; i <= n && s2[i - 1] == s3[i - 1]; i++) {
      dp[0][i] = true;
    }
    for (size_t i = 1; i <= m; i++) {
      for (size_t j = 1; j <= n; j++) {
        dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) ||
                   (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]);
      }
    }
    return dp[m][n];
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
  string s1 = json::parse(inputArray.at(0));
  string s2 = json::parse(inputArray.at(1));
  string s3 = json::parse(inputArray.at(2));
  return solution.isInterleave(s1, s2, s3);
}
