//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minimumTotal(const vector<vector<int>> &triangle) {
    int n = triangle.size();
    vector<int> dp(n);
    for (int i = 0; i < n; ++i) {
      if (i > 0) {
        dp[i] = dp[i - 1] + triangle[i][i];
      }
      for (int j = i - 1; j > 0; --j) {
        dp[j] = min(dp[j], dp[j - 1]) + triangle[i][j];
      }
      dp[0] += triangle[i][0];
    }
    return *min_element(dp.begin(), dp.end());
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
  vector<vector<int>> triangle = json::parse(inputArray.at(0));
  return solution.minimumTotal(triangle);
}
