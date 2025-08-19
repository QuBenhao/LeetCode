//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int countSquares(const vector<vector<int>> &matrix) {
    int m = matrix.size(), n = matrix[0].size();
    int ans = 0;
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (matrix[i][j] == 1) {
          dp[i + 1][j + 1] = min({dp[i][j], dp[i + 1][j], dp[i][j + 1]}) + 1;
          ans += dp[i + 1][j + 1];
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
  vector<vector<int>> matrix = json::parse(inputArray.at(0));
  return solution.countSquares(matrix);
}
