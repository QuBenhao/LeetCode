//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

constexpr int MOD = 1e9 + 7;

class Solution {
public:
  int numberOfWays(int n, int x) {
    vector<int> dp(n + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= n; ++i) {
      int64_t v = pow(i, x);
      if (v > n)
        break;
      for (int j = n; j >= v; --j) {
        dp[j] = (dp[j] + dp[j - v]) % MOD;
      }
    }
    return dp[n];
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
  int n = json::parse(inputArray.at(0));
  int x = json::parse(inputArray.at(1));
  return solution.numberOfWays(n, x);
}
