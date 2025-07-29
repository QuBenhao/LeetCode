//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>
#include <cctype>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> diffWaysToCompute(const string &expression) {
    int n = expression.size();
    vector<vector<vector<int>>> dp(n, vector<vector<int>>(n));
    auto dfs = [&](this auto &&dfs, int l, int r) -> vector<int> {
      if (!dp[l][r].empty()) {
        return dp[l][r];
      }
      if (r < l) {
        dp[l][r].emplace_back(0);
        return dp[l][r];
      }
      bool is_all_digits =
          all_of(expression.begin() + l, expression.begin() + r + 1, ::isdigit);
      if (is_all_digits) {
        dp[l][r].emplace_back(stoi(expression.substr(l, r - l + 1)));
      } else {
        for (int i = l; i <= r; ++i) {
          if (isdigit(expression[i])) {
            continue;
          }
          const auto &left_vals = dfs(l, i - 1);
          const auto &right_vals = dfs(i + 1, r);
          for (int left_val : left_vals) {
            for (int right_val : right_vals) {
              int result;
              switch (expression[i]) {
              case '+':
                result = left_val + right_val;
                break;
              case '-':
                result = left_val - right_val;
                break;
              case '*':
                result = left_val * right_val;
                break;
              }
              dp[l][r].emplace_back(result);
            }
          }
        }
      }
      return dp[l][r];
    };
    return dfs(0, n - 1);
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
  string expression = json::parse(inputArray.at(0));
  return solution.diffWaysToCompute(expression);
}
