//go:build ignore
#include "cpp/common/Solution.h"

#include <stack>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool parseBoolExpr(string s) {
        stack<char> nums, ops;
        for (char c : s) {
            if (c == ',') continue;
            if (c == 't' || c == 'f') nums.push(c);
            if (c == '|' || c == '&' || c == '!') ops.push(c);
            if (c == '(') nums.push('-');
            if (c == ')') {
                char op = ops.top(); ops.pop();
                char cur = ' ';
                while (!nums.empty() && nums.top() != '-') {
                    char top = nums.top(); nums.pop();
                    cur = cur == ' ' ? top : calc(top, cur, op);
                }
                if (op == '!') cur = cur == 't' ? 'f' : 't';
                nums.pop(); nums.push(cur);
            }
        }
        return nums.top() == 't';
    }
    char calc(char a, char b, char op) {
        bool x = a == 't', y = b == 't';
        bool ans = op == '|' ? x | y : x & y;
        return ans ? 't' : 'f';
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
  string expression = json::parse(inputArray.at(0));
  return solution.parseBoolExpr(expression);
}
