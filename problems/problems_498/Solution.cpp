//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> findDiagonalOrder(const vector<vector<int>> &mat) {
    int m = mat.size(), n = mat[0].size();
    vector<int> result(m * n);
    int idx = 0;
    for (int k = 0; k < m + n; ++k) {
      int x, d;
      int upper = min(k, m - 1), lower = max(0, k - n + 1);
      if (k % 2 == 0) {
        x = upper;
        d = -1;
      } else {
        x = lower;
        d = 1;
      }
      while (x >= lower && x <= upper) {
        result[idx++] = mat[x][k - x];
        x += d;
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
  vector<vector<int>> mat = json::parse(inputArray.at(0));
  return solution.findDiagonalOrder(mat);
}
