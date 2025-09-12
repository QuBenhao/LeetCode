//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class UnionFind {
  vector<int> fa;
  vector<int> size;

public:
  int cc;
  explicit UnionFind(int n) : fa(n), size(n, 1), cc(n) {
    for (int i = 0; i < n; i++) {
      fa[i] = i;
    }
  }

  int find(int x) {
    if (fa[x] != x) {
      fa[x] = find(fa[x]);
    }
    return fa[x];
  }

  bool merge(int x, int y) {
    int px = find(x), py = find(y);
    if (px == py) {
      return false;
    }
    fa[px] = py;
    size[py] += size[px];
    cc--;
    return true;
  }

  int get_size(int x) { return size[find(x)]; }
};

constexpr array<array<int, 2>, 4> DIRS({{0, 1}, {1, 0}, {0, -1}, {-1, 0}});

class Solution {
public:
  int largestIsland(const vector<vector<int>> &grid) {
    int n = grid.size();
    auto pointToIdx = [&n](int x, int y) -> int { return x * n + y; };
    UnionFind uf(n * n);
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 0) {
          continue;
        }
        int p = pointToIdx(i, j);
        for (const auto &dir : DIRS) {
          int nx = i + dir[0], ny = j + dir[1];
          if (nx < 0 || nx >= n || ny < 0 || ny >= n || grid[nx][ny] != 1) {
            continue;
          }
          uf.merge(p, pointToIdx(nx, ny));
        }
        ans = max(ans, uf.get_size(uf.find(p)));
      }
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] != 0) {
          continue;
        }
        int tot = 1;
        unordered_set<int> explored;
        for (const auto &dir : DIRS) {
          int nx = i + dir[0], ny = j + dir[1];
          if (nx < 0 || nx >= n || ny < 0 || ny >= n || grid[nx][ny] != 1) {
            continue;
          }
          int root = uf.find(pointToIdx(nx, ny));
          if (explored.contains(root)) {
            continue;
          }
          explored.insert(root);
          tot += uf.get_size(root);
        }
        ans = max(ans, tot);
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
  return solution.largestIsland(grid);
}
