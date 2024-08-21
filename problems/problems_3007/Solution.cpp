//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long findMaximumNumber(long long k, int x) {
    long long num = 0LL, pre_one = 0LL;
    for (long long i = __lg((k + 1) << x); i >= 0; i--) {
      long long cur = (pre_one << i) + (i / x << i >> 1);
      if (cur <= k) {
        k -= cur;
        num |= 1LL << i;
        pre_one += (i + 1) % x == 0;
      }
    }
    return num - 1;
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
  long long k = json::parse(inputArray.at(0));
  int x = json::parse(inputArray.at(1));
  return solution.findMaximumNumber(k, x);
}
