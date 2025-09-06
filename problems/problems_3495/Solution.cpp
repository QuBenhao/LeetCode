//go:build ignore
#include "cpp/common/Solution.h"
#include <cmath>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long minOperations(const vector<vector<int>> &queries) {
    uint64_t ans = 0;
    auto helper = [](uint64_t s, int m) -> uint64_t {
      return m > s - m ? m : (s + 1) / 2;
    };
    auto preSum = [](this auto &&preSum, int num) -> uint64_t {
      if (num == 0) {
        return 0;
      }
      uint64_t b = (bitlen(num) + 1) / 2;
      int last = (1 << (2 * (b - 1))) - 1;
      return preSum(last) + b * (num - last);
    };
    for (const auto &q : queries) {
      int mx = (bitlen(q[1]) + 1) / 2;
      uint64_t sm = preSum(q[1]) - preSum(q[0] - 1);
      ans += helper(sm, mx);
    }
    return ans;
  }

private:
  static int bitlen(int x) { return x == 0 ? 0 : 32 - __builtin_clz(x); }
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
  vector<vector<int>> queries = json::parse(inputArray.at(0));
  return solution.minOperations(queries);
}
