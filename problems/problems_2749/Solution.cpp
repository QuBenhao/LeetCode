//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int makeTheIntegerZero(int num1, int num2) {
    int64_t x = num1;
    for (int k = 1;; ++k) {
      x -= num2;
      if (k > x) {
        break;
      }
      if (__builtin_popcountll(x) <= k) {
        return k;
      }
    }
    return -1;
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
  int num1 = json::parse(inputArray.at(0));
  int num2 = json::parse(inputArray.at(1));
  return solution.makeTheIntegerZero(num1, num2);
}
