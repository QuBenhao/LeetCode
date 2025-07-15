//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  string shortestCommonSupersequence(const string &str1, const string &str2) {
    int m = str1.size(), n = str2.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (str1[i] == str2[j]) {
          dp[i + 1][j + 1] = dp[i][j] + 1;
        } else {
          dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1]);
        }
      }
    }
    string result;
    for (int i = m - 1, j = n - 1; i >= 0 || j >= 0;) {
      if (i < 0) {
        result += str2[j--];
        continue;
      }
      if (j < 0) {
        result += str1[i--];
        continue;
      }
      if (str1[i] == str2[j]) {
        result += str1[i];
        --i;
        --j;
      } else if (dp[i + 1][j] <= dp[i][j + 1]) {
        result += str1[i--];
      } else {
        result += str2[j--];
      }
    }
    reverse(result.begin(), result.end());
    return result;
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
  string str1 = json::parse(inputArray.at(0));
  string str2 = json::parse(inputArray.at(1));
  return solution.shortestCommonSupersequence(str1, str2);
}
