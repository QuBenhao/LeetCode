//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxCollectedFruits(const vector<vector<int>> &fruits) {
    int n = fruits.size();
    int ans = fruits[0][0] + fruits[n - 1][n - 1];
    vector<int> dp1(n, 0);
    vector<int> dp2(n, 0);
    dp1[n - 1] = fruits[0][n - 1];
    dp2[n - 1] = fruits[n - 1][0];
    for (int i = 1; i < n - 1; ++i) {
      ans += fruits[i][i];
      vector<int> dp1_new(n, 0);
      vector<int> dp2_new(n, 0);
      for (int j = max(n - 1 - i, i + 1); j < n - 1; ++j) {
        dp1_new[j] = max(max(dp1[j - 1], dp1[j]), dp1[j + 1]) + fruits[i][j];
        dp2_new[j] = max(max(dp2[j - 1], dp2[j]), dp2[j + 1]) + fruits[j][i];
      }
      dp1_new[n - 1] = max(dp1[n - 2], dp1[n - 1]) + fruits[i][n - 1];
      dp2_new[n - 1] = max(dp2[n - 2], dp2[n - 1]) + fruits[n - 1][i];
      dp1 = std::move(dp1_new);
      dp2 = std::move(dp2_new);
    }
    return ans + dp1[n - 1] + dp2[n - 1];
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
  vector<vector<int>> fruits = json::parse(inputArray.at(0));
  return solution.maxCollectedFruits(fruits);
}
