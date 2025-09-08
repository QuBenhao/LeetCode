//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

constexpr int MOD = 1e9 + 7;

class Solution {
public:
  int peopleAwareOfSecret(int n, int delay, int forget) {
    vector<int> pre_sum(n + 1, 0);
    pre_sum[1] = 1;
    for (int i = 2; i <= n; ++i) {
      int inc = (pre_sum[max(i - delay, 0)] - pre_sum[max(i - forget, 0)]) % MOD;
      pre_sum[i] = (pre_sum[i - 1] + inc) % MOD;
    }
    return ((pre_sum[n] - pre_sum[max(n - forget, 0)]) % MOD + MOD) % MOD;
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
  int delay = json::parse(inputArray.at(1));
  int forget = json::parse(inputArray.at(2));
  return solution.peopleAwareOfSecret(n, delay, forget);
}
