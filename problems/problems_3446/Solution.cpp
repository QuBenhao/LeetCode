//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<vector<int>> sortMatrix(vector<vector<int>> &grid) {
    int n = grid.size();
    for (int i = 0; i < 2 * n - 1; ++i) {
      int row = i < n ? i : 0, col = i < n ? 0 : i - n + 1;
      vector<int> diagonal;
      for (int x = row, y = col; x < n && y < n; ++x, ++y) {
        diagonal.push_back(grid[x][y]);
      }
      if (i < n) {
        sort(diagonal.begin(), diagonal.end(), greater<int>());
      } else {
        sort(diagonal.begin(), diagonal.end());
      }
      for (const auto &v : diagonal) {
        grid[row][col] = v;
        row++;
        col++;
      }
    }
    return grid;
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
  return solution.sortMatrix(grid);
}
