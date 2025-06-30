//go:build ignore
#include "cpp/common/Solution.h"
#include <cctype>
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<string> letterCasePermutation(string s) {
    vector<string> result;
    auto dfs = [&](auto &&dfs, string &current, int index) -> void {
      if (index == s.size()) {
        result.push_back(current);
        return;
      }
      dfs(dfs, current, index + 1);
      if (isalpha(s[index])) {
        current[index] = s[index] ^ 32;  // Toggle case using bitwise XOR
        dfs(dfs, current, index + 1);
        current[index] ^= 32;  // Revert back to original case
      }
    };

    string current = s;
    dfs(dfs, current, 0);
    return result;
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
  return solution.letterCasePermutation(s);
}
