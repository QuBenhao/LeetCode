//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int countNumbersWithUniqueDigits(int n) {
    if (n == 0)
      return 1;
    int ans = 10;
    int last = 9;
    for (int i = 2; i <= n; ++i) {
      int cur = last * (11 - i);
      ans += cur;
      last = cur;
    }
    return ans;
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
  return solution.countNumbersWithUniqueDigits(n);
}
