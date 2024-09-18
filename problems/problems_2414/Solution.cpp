//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int longestContinuousSubstring(string s) {
    int ans = 1, n = static_cast<int>(s.size());
    for (int i = 0, cur = 1; i < n - 1; i++) {
      if (s[i + 1] - s[i] == 1) {
        cur++;
        ans = max(ans, cur);
      } else {
        cur = 1;
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
  return solution.longestContinuousSubstring(s);
}
