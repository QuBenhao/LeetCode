//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  string solveEquation(const string &equation) {
    int k = 0, b = 0, sign = 1, cur = 0;
    char last = '1';
    for (char c : equation) {
      if (c >= '0' && c <= '9') {
        cur = cur * 10 + c - '0';
      } else {
        if (c == 'x') {
          if (last != '0' && cur == 0) {
            cur = 1;
          }
          k += sign * cur;
        } else {
          b += sign * cur;
          if (c == '=') {
            sign = 1;
            k *= -1;
            b *= -1;
          } else if (c == '-') {
            sign = -1;
          } else if (c == '+') {
            sign = 1;
          }
        }
        cur = 0;
      }
      last = c;
    }
    b += sign * cur;
    if (k == 0) {
      return b == 0 ? "Infinite solutions" : "No solution";
    }
    return "x=" + to_string(-b / k);
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
  string equation = json::parse(inputArray.at(0));
  return solution.solveEquation(equation);
}
