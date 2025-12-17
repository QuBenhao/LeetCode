//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

constexpr int MOD = 1e9 + 7;

class Solution {
public:
  int waysToStep(int n) {
    array<int, 4> dp{1, 2, 4, 0};
    for (int i = 3; i < n; ++i) {
      dp[i % 4] =
          ((dp[(i + 1) % 4] + dp[(i + 2) % 4]) % MOD + dp[(i + 3) % 4]) % MOD;
    }
    return dp[(n + 3) % 4];
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
  return solution.waysToStep(n);
}
