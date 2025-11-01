//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

constexpr int DIRS[4][2]{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

class Solution {
public:
  int countUnguarded(int m, int n, const vector<vector<int>> &guards,
                     const vector<vector<int>> &walls) {
    vector<vector<int>> grid(m, vector<int>(n));
    for (const auto &g : guards) {
      grid[g[0]][g[1]] = -1;
    }
    for (const auto &w : walls) {
      grid[w[0]][w[1]] = -1;
    }
    for (const auto &g : guards) {
      for (const auto &d : DIRS) {
        int x = g[0] + d[0], y = g[1] + d[1];
        while (0 <= x && x < m && 0 <= y && y < n && grid[x][y] != -1) {
          grid[x][y] = 1;
          x += d[0];
          y += d[1];
        }
      }
    }
    int ans = 0;
    for (const auto &row : grid) {
      for (const auto &g : row) {
        if (g == 0) {
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
  int m = json::parse(inputArray.at(0));
  int n = json::parse(inputArray.at(1));
  vector<vector<int>> guards = json::parse(inputArray.at(2));
  vector<vector<int>> walls = json::parse(inputArray.at(3));
  return solution.countUnguarded(m, n, guards, walls);
}
