//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  double champagneTower(int poured, int query_row, int query_glass) {
    vector<double> dp(1, poured);
    for (int i = 1; i <= query_row; ++i) {
      vector<double> next_dp(i + 1, 0.0);
      for (int j = 0; j < i; ++j) {
        double excess = max(0.0, (dp[j] - 1.0) / 2.0);
        next_dp[j] += excess;
        next_dp[j + 1] += excess;
      }
      dp = std::move(next_dp);
    }
    return min(1.0, dp[query_glass]);
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
  int poured = json::parse(inputArray.at(0));
  int query_row = json::parse(inputArray.at(1));
  int query_glass = json::parse(inputArray.at(2));
  return solution.champagneTower(poured, query_row, query_glass);
}
