//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> findCoins(vector<int> &numWays) {
    int n = numWays.size();
    vector<int> dp(n + 1, 0);
    vector<int> ans;
    dp[0] = 1; // Base case: one way to make 0
    for (int i = 1; i <= n; ++i) {
      int cur = numWays[i - 1];
      if (dp[i] == cur - 1) {
        ++dp[i];
        ans.push_back(i);
        for (int j = i + 1; j <= n; ++j) {
          dp[j] += dp[j - i];
        }
      } else if (dp[i] != cur) {
        return {};
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
  vector<int> numWays = json::parse(inputArray.at(0));
  return solution.findCoins(numWays);
}
