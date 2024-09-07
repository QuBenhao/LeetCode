//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<vector<string>> solveNQueens(int n) {
    vector<vector<int>> res;
    vector<int> path;
    vector<bool> col(n, false), dg(2 * n, false), udg(2 * n, false);
    function<void(int)> backtrack = [&](int r) {
      if (r == n) {
        res.push_back(path);
        return;
      }
      for (int c = 0; c < n; c++) {
        int idx1 = r + c, idx2 = n - 1 - r + c;
        if (col[c] || dg[idx1] || udg[idx2])
          continue;
        col[c] = dg[idx1] = udg[idx2] = true;
        path.push_back(c);
        backtrack(r + 1);
        path.pop_back();
        col[c] = dg[idx1] = udg[idx2] = false;
      }
    };
    backtrack(0);
    vector<vector<string>> ret;
    for (auto &p : res) {
      vector<string> tmp(n, string(n, '.'));
      for (int i = 0; i < n; i++)
        tmp[i][p[i]] = 'Q';
      ret.push_back(tmp);
    }
    return ret;
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
  int n = json::parse(inputArray.at(0));
  return solution.solveNQueens(n);
}
