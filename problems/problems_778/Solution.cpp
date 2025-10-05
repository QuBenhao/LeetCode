//go:build ignore
#include "cpp/common/Solution.h"
#include <functional>
#include <queue>
#include <tuple>
#include <vector>

using namespace std;
using json = nlohmann::json;

constexpr array<array<int, 2>, 4> DIRS = {{
    {0, 1},  // right
    {1, 0},  // down
    {-1, 0}, // up
    {0, -1}  // left
}};

class Solution {
public:
  int swimInWater(const vector<vector<int>> &grid) {
    int n = grid.size();
    if (n == 1) {
      return 0;
    }
    vector<vector<bool>> explored(n, vector<bool>(n));
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>,
                   greater<tuple<int, int, int>>>
        min_heap;
    min_heap.emplace(grid[0][0], 0, 0);
    explored[0][0] = true;
    while (!min_heap.empty()) {
      auto [t, x, y] = min_heap.top();
      if (x == n - 1 && y == n - 1) {
        return t;
      }
      min_heap.pop();
      for (const auto &dir : DIRS) {
        int nx = x + dir[0], ny = y + dir[1];
        if (nx < 0 || nx == n || ny < 0 || ny == n || explored[nx][ny]) {
          continue;
        }
        min_heap.emplace(max(grid[nx][ny], t), nx, ny);
        explored[nx][ny] = true;
      }
    }
    return -1;
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
  return solution.swimInWater(grid);
}
