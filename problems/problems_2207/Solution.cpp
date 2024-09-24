//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long maximumSubsequenceCount(string text, string pattern) {
    int64_t ans = 0, p0 = 0, p1 = 0;
    for (const auto &c : text) {
      if (c == pattern[1]) {
        ans += p0;
        p1++;
      }
      if (c == pattern[0]) {
        p0++;
      }
    }
    return ans + max(p0, p1);
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
  string text = json::parse(inputArray.at(0));
  string pattern = json::parse(inputArray.at(1));
  return solution.maximumSubsequenceCount(text, pattern);
}
