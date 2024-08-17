//go:build ignore
#include "cpp/common/Solution.h"
#include <stack>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int evalRPN(vector<string> &tokens) {
    stack<int> values;
    for (const string &token : tokens) {
      if (token == "+" || token == "-" || token == "*" || token == "/") {
        int b = values.top();
        values.pop();
        switch (token[0]) {
        case '+':
          values.top() += b;
          break;
        case '-':
          values.top() -= b;
          break;
        case '*':
          values.top() *= b;
          break;
        case '/':
          values.top() /= b;
          break;
        }
      } else {
        values.push(stoi(token.c_str()));
      }
    }
    return values.top();
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
  vector<string> tokens = json::parse(inputArray.at(0));
  return solution.evalRPN(tokens);
}
