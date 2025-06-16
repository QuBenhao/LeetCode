//go:build ignore
#include "cpp/common/Solution.h"
#include <string>
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  string shortestSuperstring(vector<string> &words) {
    int n = words.size();
    vector<vector<int>> g(n, vector<int>(n, 0));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (i == j)
          continue;
        for (int k = min(words[i].size(), words[j].size()); k > 0; --k) {
          if (words[i].substr(words[i].size() - k) == words[j].substr(0, k)) {
            g[i][j] = k;
            break;
          }
        }
      }
    }
    int mask = 1 << n;
    vector<vector<int>> dp(mask, vector<int>(n, 0));
    vector<vector<int>> track(mask, vector<int>(n, -1));
    for (int s = 1; s < mask; ++s) {
      for (int i = 0; i < n; ++i) {
        if (!(s & (1 << i)))
          continue;
        for (int j = 0; j < n; ++j) {
          if (s & (1 << j))
            continue;
          int next_mask = s | (1 << j);
          int new_length = dp[s][i] + g[i][j];
          if (new_length > dp[next_mask][j]) {
            dp[next_mask][j] = new_length;
            track[next_mask][j] = i;
          }
        }
      }
    }
    int st = mask - 1;
    auto get_max = [&](int mk) -> int {
      int idx = -1, m = -1;
      for (int i = 0; i < n; ++i) {
        if ((mk >> i) & 1 && dp[mk][i] > m) {
          m = dp[mk][i];
          idx = i;
        }
      }
      return idx;
    };
    int idx = get_max(st);
    string result = words[idx];
    while (st > 0) {
      int prev = idx;
      idx = track[st][idx];
      st ^= 1 << prev;
      if (idx != -1) {
        result =
            words[idx].substr(0, words[idx].size() - g[idx][prev]) + result;
      } else {
        idx = get_max(st);
        if (idx != -1) {
          result = words[idx] + result;
        }
      }
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
  vector<string> words = json::parse(inputArray.at(0));
  return solution.shortestSuperstring(words);
}
