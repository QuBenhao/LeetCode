//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool checkDivisibility(int n) {
    int64_t m = 1;
    int s = 0;
    for (int num = n; num > 0; num /= 10) {
      int d = num % 10;
      s += d;
      m *= d;
    }
    return n % (m + s) == 0;
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
  return solution.checkDivisibility(n);
}
