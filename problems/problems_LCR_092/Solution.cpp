//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minFlipsMonoIncr(string s) {
    int n = static_cast<int>(s.size());
    int ans = n, one = 0;
    for (int i = 0; i < n; i++) {
      ans = min(ans, one * 2 - i);
      one += s[i] == '1';
    }
    return min(one, ans + n - one);
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
  return solution.minFlipsMonoIncr(s);
}
