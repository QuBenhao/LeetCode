//go:build ignore
#include "cpp/common/Solution.h"
#include <array>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int findPermutationDifference(string s, string t) {
    int ans = 0;
    array<int, 26> idx_map = {0};
    for (int i = 0; i < static_cast<int>(s.length()); i++) {
      idx_map[s[i] - 'a'] += i;
      idx_map[t[i] - 'a'] -= i;
    }
    for (int i = 0; i < 26; i++) {
      ans += abs(idx_map[i]);
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
  string t = json::parse(inputArray.at(1));
  return solution.findPermutationDifference(s, t);
}
