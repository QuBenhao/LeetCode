//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

const int MOD = 1e9 + 7;

class Solution {
public:
  int possibleStringCount(string word, int k) {
    int n = word.size();
    vector<int> groups;
    int64_t ans = 1;
    for (int i = 0; i < n; ) {
      int start = i;
      while (i < n && word[i] == word[start]) {
        ++i;
      }
      --k;
      int len = i - start;
      if (len > 1) {
        ans = ans * len % MOD;
        groups.push_back(len - 1);
      }
    }
    if (k <= 0) {
      return ans;
    }
    vector<int> dp(k, 1);
    for (int g : groups) {
      for (int i = 1; i < k; ++i) {
        dp[i] = (dp[i] + dp[i - 1]) % MOD;
      }
      for (int i = k - 1; i > g; --i) {
        dp[i] = (dp[i] - dp[i - g - 1] + MOD) % MOD;
      }
    }
    return (ans - dp[k - 1] + MOD) % MOD;
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
  string word = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.possibleStringCount(word, k);
}
