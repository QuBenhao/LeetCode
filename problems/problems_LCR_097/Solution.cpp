//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int numDistinct(string s, string t) {
    int m = static_cast<int>(s.size()), n = static_cast<int>(t.size());
    vector<vector<uint64_t>> dp(m + 1, vector<uint64_t>(n + 1));
    for (int i = 0; i <= m; i++) {
      dp[i][0] = 1;
    }
    for (int i = 1; i <= m; i++) {
      for (int j = 1; j <= n; j++) {
        if (s[i - 1] == t[j - 1]) {
          dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
        } else {
          dp[i][j] = dp[i - 1][j];
        }
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
  string s = json::parse(inputArray.at(0));
  string t = json::parse(inputArray.at(1));
  return solution.numDistinct(s, t);
}
