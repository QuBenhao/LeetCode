//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int flipLights(int n, int presses) {
    if (presses == 0)
      return 1;
    if (n == 1)
      return 2;
    if (n == 2)
      return presses == 1 ? 3 : 4;
    return presses == 1 ? 4 : presses == 2 ? 7 : 8;
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
  int n = json::parse(inputArray.at(0));
  int presses = json::parse(inputArray.at(1));
  return solution.flipLights(n, presses);
}
