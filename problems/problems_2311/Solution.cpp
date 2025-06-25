//go:build ignore
#include "cpp/common/Solution.h"

#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int longestSubsequence(const string& s, int k) {
    int ans = count(s.begin(), s.end(), '0');
    int n = s.length(), cur = 0;
    int max_len = min(n, 31);
    for (int i = 0; i < max_len; ++i) {
      if (s[n - 1 - i] == '1' && (cur | (1 << i)) <= k) {
        cur |= (1 << i);
        ++ans;
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
  string s = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.longestSubsequence(s, k);
}
