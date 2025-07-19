//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

vector<int> DEPTH;
bool inited = false;
void init() {
  if (inited) {
    return;
  }
  inited = true;
  int64_t max_n = 1e15;
  int bit_len = 64 - __builtin_clzll(max_n);
  DEPTH = vector<int>(bit_len + 1);
  for (int i = 2; i <= bit_len; ++i) {
    int j = i;
    while (j > 1) {
      ++DEPTH[i];
      j = __builtin_popcount(j);
    }
  }
}

class Solution {
public:
  long long popcountDepth(long long n, int k) {
    init();
    if (k == 0) {
      return 1;
    }
    int length = 64 - __builtin_clzll(n);

    vector<vector<vector<int64_t>>> dp(
        length + 1, vector<vector<int64_t>>(length + 1, vector<int64_t>(2, -1)));

    auto dfs = [&](this auto &&dfs, int pos, bool limit, int count) -> int64_t {
      if (count < 0 || length - pos < count) {
        return 0;
      }
      if (pos == length) {
        return 1;
      }
      if (dp[pos][count][limit] != -1) {
        return dp[pos][count][limit];
      }

      int nd = (n >> (length - pos - 1)) & 1;
      int max_d = limit ? nd : 1;
      int64_t cur = 0;
      for (int d = 0; d <= max_d; ++d) {
        cur += dfs(pos + 1, limit && d == nd, count - d);
      }
      dp[pos][count][limit] = cur;
      return cur;
    };

    int64_t ans = 0;
    for (int i = 2; i <= length; ++i) {
      if (DEPTH[i] == k - 1) {
        ans += dfs(0, true, i);
      }
    }
    if (k == 1) {
      ans += dfs(0, true, 1) - 1;
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
  long long n = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.popcountDepth(n, k);
}
