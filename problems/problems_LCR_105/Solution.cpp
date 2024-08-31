//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxAreaOfIsland(vector<vector<int>> &grid) {
    const vector<pair<int, int>> directions = {
        {0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    function<int(int, int)> dfs = [&](int i, int j) -> int {
      if (i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size() ||
          grid[i][j] == 0) {
        return 0;
      }
      grid[i][j] = 0;
      int res = 1;
      for (const auto &direction : directions) {
        res += dfs(i + direction.first, j + direction.second);
      }
      return res;
    };
    int max_area = 0;
    for (int i = 0; i < grid.size(); i++) {
      for (int j = 0; j < grid[0].size(); j++) {
        if (grid[i][j] == 1) {
          max_area = max(max_area, dfs(i, j));
        }
      }
    }
    return max_area;
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
  return solution.maxAreaOfIsland(grid);
}
