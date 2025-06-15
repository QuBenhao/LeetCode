//go:build ignore
#include "cpp/common/Solution.h"

#include <array>
#include <unordered_set>
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  string removeDuplicateLetters(string s) {
    array<int, 26> lastIndex;
    unordered_set<char> seen;
    vector<char> stack;

    int n = s.size();
    for (int i = 0; i < n; ++i) {
      lastIndex[s[i] - 'a'] = i;
    }
    for (int i = 0; i < n; ++i) {
      char c = s[i];
      if (seen.contains(c)) {
        continue;
      }
      while (!stack.empty() && stack.back() > c &&
             lastIndex[stack.back() - 'a'] > i) {
        seen.erase(stack.back());
        stack.pop_back();
      }
      stack.push_back(c);
      seen.insert(c);
    }
    return string(stack.begin(), stack.end());
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
  return solution.removeDuplicateLetters(s);
}
