//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> getNoZeroIntegers(int n) {
    int a = 0;
    int base = 1;
    int x = n;
    while (x > 1) {
      int d = x % 10;
      x /= 10;
      if (d <= 1) {
        x -= 1;
        d += 10;
      }
      a += d / 2 * base;
      base *= 10;
    }
    return {a, n - a};
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
  return solution.getNoZeroIntegers(n);
}
