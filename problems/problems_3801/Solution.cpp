//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>
#include <climits>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long minMergeCost(const vector<vector<int>> &lists) {
    int n = lists.size();
    int total = 1 << n;
    vector<int> h(total), g(total, 0);
    for (int i = 1; i < total; ++i) {
      for (int j = 0; j < n; ++j) {
        if (i >> j & 1) {
          g[i] += lists[j].size();
        }
      }
      int left = -1e9, right = 1e9;
      while (left < right) {
        int cnt = 0;
        int mid = (right + left) >> 1;
        for (int j = 0; j < n; ++j) {
          if (i >> j & 1) {
            cnt += upper_bound(lists[j].begin(), lists[j].end(), mid) -
                   lists[j].begin();
          }
        }
        if (cnt >= (g[i] + 1) / 2) {
          right = mid;
        } else {
          left = mid + 1;
        }
      }
      h[i] = left;
    }
    vector<long long> dp(total, LONG_MAX);
    for (int j = 0; j < n; ++j) {
      dp[1 << j] = 0;
    }
    for (int i = 1; i < total; ++i) {
      if (dp[i] == 0)
        continue;
      for (int j = i; j; j = (j - 1) & i) {
        if (j == i)
          continue;
        int k = i ^ j;
        dp[i] = min(dp[i], dp[j] + dp[k] + g[j] + g[k] + abs(h[j] - h[k]));
      }
    }
    return dp[total - 1];
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
  vector<vector<int>> lists = json::parse(inputArray.at(0));
  return solution.minMergeCost(lists);
}
