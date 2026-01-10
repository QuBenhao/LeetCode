//go:build ignore
#include "cpp/common/Solution.h"
#include <numeric>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minimumDeleteSum(string s1, string s2) {
    int m = s1.size(), n = s2.size();
    if (m < n) {
      swap(s1, s2);
      swap(m, n);
    }
    int total =
        reduce(s1.begin(), s1.end(), 0) + reduce(s2.begin(), s2.end(), 0);
    vector dp(n + 1, 0);
    for (const auto &c : s1) {
      int pre = 0;
      for (int j = 0; j < n; ++j) {
        int tmp = dp[j + 1];
        if (s2[j] == c) {
          dp[j + 1] = pre + c;
        } else {
          dp[j + 1] = max(dp[j + 1], dp[j]);
        }
        pre = tmp;
      }
    }
    return total - dp[n] * 2;
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
  string s1 = json::parse(inputArray.at(0));
  string s2 = json::parse(inputArray.at(1));
  return solution.minimumDeleteSum(s1, s2);
}
