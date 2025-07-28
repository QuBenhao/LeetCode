//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

const int INF = -0x3f3f3f3f;

class Solution {
public:
  int cherryPickup(const vector<vector<int>> &grid) {
    int n = grid.size();
    vector<vector<vector<int>>> dp(
        n * 2 + 1, vector<vector<int>>(n + 1, vector<int>(n + 1, INF)));
    dp[2][1][1] = grid[0][0];
    for (int step = 3; step <= n * 2; ++step) {
      for (int i1 = max(1, step - n); i1 <= min(step - 1, n); ++i1) {
        for (int i2 = i1; i2 <= min(step - 1, n); ++i2) {
          int j1 = step - i1, j2 = step - i2;
          int v1 = grid[i1 - 1][j1 - 1], v2 = grid[i2 - 1][j2 - 1];
          if (v1 == -1 || v2 == -1) {
            continue;
          }
          dp[step][i1][i2] = i1 == i2 ? v1 : v1 + v2;
          dp[step][i1][i2] +=
              max(dp[step - 1][i1 - 1][i2 - 1],
                  max(dp[step - 1][i1 - 1][i2],
                      max(dp[step - 1][i1][i2 - 1], dp[step - 1][i1][i2])));
        }
      }
    }
    return max(dp[n * 2][n][n], 0);
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
  vector<vector<int>> grid = json::parse(inputArray.at(0));
  return solution.cherryPickup(grid);
}
