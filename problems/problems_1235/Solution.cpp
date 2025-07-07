//go:build ignore
#include "cpp/common/Solution.h"
#include <numeric>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int jobScheduling(const vector<int> &startTime, const vector<int> &endTime,
                    const vector<int> &profit) {
    int n = startTime.size();
    vector<int> idxes(n);
    iota(idxes.begin(), idxes.end(), 0);
    sort(idxes.begin(), idxes.end(),
         [&](int a, int b) { return endTime[a] < endTime[b]; });
    vector<int> dp(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      int idx = idxes[i];
      int j = lower_bound(idxes.begin(), idxes.begin() + i, startTime[idx],
                          [&endTime](int a, int b) { return endTime[a] <= b; }) -
              idxes.begin();
      dp[i + 1] = max(dp[i], dp[j] + profit[idx]);
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
  vector<int> startTime = json::parse(inputArray.at(0));
  vector<int> endTime = json::parse(inputArray.at(1));
  vector<int> profit = json::parse(inputArray.at(2));
  return solution.jobScheduling(startTime, endTime, profit);
}
