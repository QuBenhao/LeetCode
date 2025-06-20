//go:build ignore
#include "cpp/common/Solution.h"

#include <queue>
#include <unordered_set>

using namespace std;
using json = nlohmann::json;

class Solution {
  constexpr static int dirs[4][2]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

public:
  int shortestPathAllKeys(vector<string> &grid) {
    int m = grid.size(), n = grid[0].size();
    int goal = 0;
    queue<tuple<int, int, int>> q;
    unordered_set<int> blocked, visited;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        char c = grid[i][j];
        if (c == '@') {
          q.emplace(i, j, 0);
          visited.insert(i * n + j);
        } else if (c >= 'a' && c <= 'f') {
          goal |= 1 << (c - 'a');
        } else if (c == '#') {
          blocked.insert(i * n + j);
        }
      }
    }
    for (int steps = 0; !q.empty(); ++steps) {
      int size = q.size();
      for (int i = 0; i < size; ++i) {
        auto [x, y, keys] = q.front();
        q.pop();
        if (keys == goal) {
          return steps;
        }
        for (const auto &[dx, dy] : dirs) {
          int nx = x + dx, ny = y + dy;
          if (nx < 0 || nx >= m || ny < 0 || ny >= n ||
              blocked.contains(nx * n + ny)) {
            continue;
          }
          char c = grid[nx][ny];
          if ('A' <= c && c <= 'F' && !(keys & (1 << (c - 'A')))) {
            continue;  // Blocked by a door
          }
          int newKeys = keys;
          if ('a' <= c && c <= 'f') {
            newKeys |= 1 << (c - 'a');  // Collect a key
            if (newKeys == goal) {
              return steps + 1;  // All keys collected
            }
          }
          int status = newKeys * m * n + nx * n + ny;
          if (!visited.contains(status)) {
            visited.insert(status);
            q.emplace(nx, ny, newKeys);
          }
        }
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
  vector<string> grid = json::parse(inputArray.at(0));
  return solution.shortestPathAllKeys(grid);
}
