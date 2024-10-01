//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int mincostTickets(vector<int> &days, vector<int> &costs) {
    size_t n = days.size();
    vector<int> dp(n + 1, 0);
    for (size_t i = 0, j = 0, k = 0; i < n; ++i) {
      while (days[j] <= days[i] - 7)
        ++j;
      while (days[k] <= days[i] - 30)
        ++k;
      dp[i + 1] = min({dp[i] + costs[0], dp[j] + costs[1], dp[k] + costs[2]});
    }
    return dp[n];
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
  vector<int> days = json::parse(inputArray.at(0));
  vector<int> costs = json::parse(inputArray.at(1));
  return solution.mincostTickets(days, costs);
}
