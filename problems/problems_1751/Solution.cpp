//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxValue(vector<vector<int>> &events, int k) {
    sort(
        events.begin(), events.end(),
        [](const auto &a, const auto &b) { return a[1] < b[1]; });
    int n = events.size();
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
    for (int i = 0; i < n; ++i) {
      int p =
          lower_bound(events.begin(), events.end() + i, events[i][0],
                      [](const auto &e, int lower) { return e[1] < lower; }) -
          events.begin();
      for (int j = 1; j <= k; ++j) {
        dp[i + 1][j] = max(dp[i][j], dp[p][j - 1] + events[i][2]);
      }
    }
    return dp[n][k];
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
  vector<vector<int>> events = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.maxValue(events, k);
}
