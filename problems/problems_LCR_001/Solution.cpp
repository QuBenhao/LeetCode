//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int divide(int a, int b) {
    if (a == INT_MIN && b == -1) {
      return INT_MAX;
    }
    // To allow abs of INT_MIN, we need to use unsigned int
    unsigned int dividend = abs(a), divisor = abs(b), res = 0;
    for (int i = 31; i >= 0; i--) {
      if ((dividend >> i) >= divisor) {
        res |= 1 << i;
        dividend -= divisor << i;
      }
    }
    return (a > 0) == (b > 0) ? res : -res;
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
  int a = json::parse(inputArray.at(0));
  int b = json::parse(inputArray.at(1));
  return solution.divide(a, b);
}
