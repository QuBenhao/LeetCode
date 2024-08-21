//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long minEnd(int n, int x) {
    long long ans = x;
    n--;
    for (int i = 0, j = 0; n >> j > 0; i++) {
      if ((ans >> i & 1) == 0) {
        ans |= (1LL & (n >> j)) << i;
        j++;
      }
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
  int x = json::parse(inputArray.at(1));
  return solution.minEnd(n, x);
}
