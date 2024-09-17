//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minCut(string s) {
    int n = static_cast<int>(s.size());
    if (n == 0) {
      return 0;
    }
    vector<vector<bool>> isPal(n, vector<bool>(n, false));
    for (int i = 0; i < n; i++) {
      isPal[i][i] = true;
      for (int j = 0; j < i; j++) {
        if (s[j] == s[i] && (j + 1 >= i - 1 || isPal[j + 1][i - 1])) {
          isPal[j][i] = true;
        }
      }
    }
    vector<int> dp(n, INT_MAX / 2);
    for (int i = 0; i < n; i++) {
      if (isPal[0][i]) {
        dp[i] = 0;
      } else {
        for (int j = 0; j < i; j++) {
          if (isPal[j + 1][i]) {
            dp[i] = min(dp[i], dp[j] + 1);
          }
        }
      }
    }
    return dp[n - 1];
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
  return solution.minCut(s);
}
