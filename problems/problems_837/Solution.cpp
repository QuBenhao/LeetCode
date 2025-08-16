//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  double new21Game(int n, int k, int maxPts) {
    vector<double> dp(n + 1, 0.0);
    double s = 0.0;
    for (int i = n; i >= 0; --i) {
      dp[i] = i >= k ? 1.0 : s / maxPts;
      s += dp[i];
      if (i + maxPts <= n) {
        s -= dp[i + maxPts];
      }
    }
    return dp[0];
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
  int k = json::parse(inputArray.at(1));
  int maxPts = json::parse(inputArray.at(2));
  return solution.new21Game(n, k, maxPts);
}
