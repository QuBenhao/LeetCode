//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long maxSubarrays(int n, const vector<vector<int>> &conflictingPairs) {
    vector<int> g0(n + 1, n + 1), g1(n + 1, n + 1);
    for (const auto &pair : conflictingPairs) {
      int a = pair[0], b = pair[1];
      if (a > b)
        swap(a, b);
      if (b < g0[a]) {
        g1[a] = g0[a];
        g0[a] = b;
      } else if (b < g1[a]) {
        g1[a] = b;
      }
    }
    int64_t ans = 0, max_extra = 0, extra = 0;
    int b0 = n + 1, b1 = n + 1;
    for (int i = n; i > 0; --i) {
      int pre_b = b0;

      int b = g0[i], c = g1[i];
      if (b < b0) {
        b1 = min(b0, c);
        b0 = b;
      } else if (b < b1) {
        b1 = b;
      } else if (c < b1) {
        b1 = c;
      }
      ans += b0 - i;
      if (b0 != pre_b) {
        extra = 0;
      }
      extra += b1 - b0;
      max_extra = max(max_extra, extra);
    }
    return ans + max_extra;
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
  vector<vector<int>> conflictingPairs = json::parse(inputArray.at(1));
  return solution.maxSubarrays(n, conflictingPairs);
}
