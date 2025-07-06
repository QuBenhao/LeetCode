//go:build ignore
#include "cpp/common/Solution.h"

#include <set>

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

class Solution {
public:
  vector<int> processQueries(int c, const vector<vector<int>> &connections,
                             const vector<vector<int>> &queries) {
    UnionFind uf(c);
    for (const auto &conn : connections) {
      uf.merge(conn[0] - 1, conn[1] - 1);
    }
    unordered_map<int, set<int>> groups;
    for (int i = 0; i < c; ++i) {
      groups[uf.find(i)].insert(i);
    }
    vector<int> result;
    for (const auto &query : queries) {
      int op = query[0], x = query[1] - 1;
      int pa = uf.find(x);
      if (op == 2) {
        groups[pa].erase(x);
      } else {
        if (groups[pa].empty()) {
          result.push_back(-1);
        } else {
          auto it = groups[pa].find(x);
          if (it == groups[pa].end()) {
            it = groups[pa].begin();
          }
          result.push_back(*it + 1);
        }
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
  int c = json::parse(inputArray.at(0));
  vector<vector<int>> connections = json::parse(inputArray.at(1));
  vector<vector<int>> queries = json::parse(inputArray.at(2));
  return solution.processQueries(c, connections, queries);
}
