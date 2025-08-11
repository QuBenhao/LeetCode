//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

constexpr int MOD = 1e9 + 7;
bool inited = false;
array<int, 436> POWERS;
void init() {
  if (inited)
    return;
  inited = true;
  POWERS[0] = 1;
  for (int i = 1; i < 436; i++) {
    POWERS[i] = POWERS[i - 1] * 2 % MOD;
  }
}

class Solution {
public:
  vector<int> productQueries(int n, const vector<vector<int>> &queries) {
    init();
    vector<int> pre_sum{0};
    while (n > 0) {
      int lowbit = n & -n;
      int length = __builtin_ctz(lowbit);
      pre_sum.push_back(pre_sum.back() + length);
      n ^= lowbit;
    }
    vector<int> result;
    for (const auto &query : queries) {
      int left = query[0], right = query[1];
      result.push_back(POWERS[pre_sum[right + 1] - pre_sum[left]]);
    }
    return result;
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
  vector<vector<int>> queries = json::parse(inputArray.at(1));
  return solution.productQueries(n, queries);
}
