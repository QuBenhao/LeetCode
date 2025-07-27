//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<vector<int>> shiftGrid(const vector<vector<int>> &grid, int k) {
    int m = grid.size(), n = grid[0].size();
    k %= m * n;
    if (k == 0)
      return grid;
    vector<vector<int>> result(m, vector<int>(n));
    int x = k / n, y = k % n;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        result[x][y] = grid[i][j];
        if (++y == n) {
          y = 0;
          ++x;
        }
        x %= m;
      }
    }
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
  vector<vector<int>> grid = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.shiftGrid(grid, k);
}
