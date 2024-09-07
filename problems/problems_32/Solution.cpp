//go:build ignore
#include "cpp/common/Solution.h"
#include <stack>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int longestValidParentheses(string s) {
    stack<int> stack;
    int ans = 0, n = static_cast<int>(s.length());
    for (int i = 0; i < n; i++) {
      if (s[i] == '(') {
        stack.push(i);
      } else {
        if (!stack.empty() && s[stack.top()] == '(') {
          stack.pop();
          ans = max(ans, i - (stack.empty() ? -1 : stack.top()));
        } else {
          stack.push(i);
        }
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
  return solution.longestValidParentheses(s);
}
