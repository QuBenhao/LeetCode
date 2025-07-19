//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int countIslands(const vector<vector<int>> &grid, int k) {
    int ans = 0;
    int m = grid.size(), n = grid[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    const vector<pair<int, int>> directions{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    auto dfs = [&](this auto &&dfs, int x, int y) -> int {
      int cur = grid[x][y] % k;
      for (const auto &[dx, dy] : directions) {
        int nx = x + dx, ny = y + dy;
        if (nx < 0 || nx >= m || ny < 0 || ny >= n || visited[nx][ny] ||
            grid[nx][ny] == 0) {
          continue;
        }
        visited[nx][ny] = true;
        cur = (cur + dfs(nx, ny)) % k;
      }
      return cur;
    };

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 0 || visited[i][j]) {
          continue;
        }
        visited[i][j] = true;
        int cur = dfs(i, j);
        if (cur == 0) {
          ++ans;
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
  vector<vector<int>> grid = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.countIslands(grid, k);
}
