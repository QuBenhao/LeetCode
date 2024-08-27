//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minimumSubstringsInPartition(string s) {
    int n = static_cast<int>(s.size());
    vector<int> dp(n + 1, n);
	dp[0] = 0;
    for (int i = 0; i < n; i++) {
      vector<int> cnt(26, 0);
      int max_cnt = 0;
      int count = 0;
      for (int j = i; j >= 0; j--) {
        int c = s[j] - 'a';
        if (cnt[c]++ == 0) {
          count++;
        }
        max_cnt = max(max_cnt, cnt[c]);
        if (i - j + 1 >= max_cnt * count) {
          dp[i + 1] = min(dp[i + 1], dp[j] + 1);
        }
      }
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
  string s = json::parse(inputArray.at(0));
  return solution.minimumSubstringsInPartition(s);
}
