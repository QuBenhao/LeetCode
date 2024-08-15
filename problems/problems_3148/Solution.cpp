//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxScore(vector<vector<int>> &grid) {
    int ans = INT32_MIN;
    vector<int> cols_min(grid[0].size(), INT32_MAX);
    for (auto row : grid) {
      int pre_min = INT32_MAX;
      for (size_t j = 0; j < row.size(); j++) {
        ans = max(ans, row[j] - min(pre_min, cols_min[j]));
        cols_min[j] = min(cols_min[j], row[j]);
        pre_min = min(pre_min, cols_min[j]);
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
  return solution.maxScore(grid);
}
