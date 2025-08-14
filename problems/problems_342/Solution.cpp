//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool isPowerOfFour(int n) {
    if (n <= 0 || (n & (n - 1)) != 0) {
      return false;  // Check if n is a power of 2
    }
    return (n - 1) % 3 == 0;  // Check if (n - 1) is divisible by 3
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
  return solution.isPowerOfFour(n);
}
