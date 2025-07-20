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
    if (px < py) {
      swap(px, py);
    }
    fa[px] = py;
    size[py] += size[px];
    cc--;
    return true;
  }

  int get_size(int x) { return size[find(x)]; }
};

class Solution {
public:
  int countIslands(const vector<vector<int>> &grid, int k) {
    int ans = 0;
    int m = grid.size(), n = grid[0].size();

    UnionFind uf(m * n);
    auto idxTrans = [n](int x, int y) { return x * n + y; };

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 0) {
          continue;
        }
        if (i > 0 && grid[i - 1][j] != 0) {
          uf.merge(idxTrans(i - 1, j), idxTrans(i, j));
        }
        if (j > 0 && grid[i][j - 1] != 0) {
          uf.merge(idxTrans(i, j - 1), idxTrans(i, j));
        }
      }
    }
    unordered_map<int, int> mp;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 0) {
          continue;
        }
        int root = uf.find(idxTrans(i, j));
        mp[root] = (mp[root] + grid[i][j]) % k;
      }
    }
    for (const auto &[_, val] : mp) {
      if (val == 0) {
        ++ans;
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
