//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maximizeWin(vector<int> &prizePositions, int k) {
    int ans = 0;
    int n = static_cast<int>(prizePositions.size());
    vector<int> dp(n + 1, 0);
    for (int left = 0, right = 0; right < n; ++right) {
      while (prizePositions[right] - prizePositions[left] > k) {
        ++left;
      }
      dp[right + 1] = max(dp[right], right - left + 1);
      ans = max(ans, dp[left] + right - left + 1);
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
  vector<int> prizePositions = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.maximizeWin(prizePositions, k);
}
