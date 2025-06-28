//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  string interpret(string command) {
    string result;
    int n = command.size();
    for (int i = 0; i < n; ++i) {
      if (command[i] == 'G') {
        result += 'G';
      } else {
        if (command[i + 1] == ')') {
          result += 'o';
          ++i;  // Skip the next character
        } else {
          result += "al";
          i += 3;  // Skip the next three characters
        }
      }
    }
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
  string command = json::parse(inputArray.at(0));
  return solution.interpret(command);
}
