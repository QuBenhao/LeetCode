//go:build ignore
#include "cpp/common/Solution.h"

#include <algorithm>
#include <bit>
#include <numeric>
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> pathExistenceQueries(int n, const vector<int> &nums, int maxDiff,
                                   const vector<vector<int>> &queries) {
    vector<int> idxes(n);
    iota(idxes.begin(), idxes.end(), 0);
    sort(idxes.begin(), idxes.end(),
         [&nums](int a, int b) { return nums[a] < nums[b]; });
    vector<int> mapped(n);
    for (int i = 0; i < n; ++i) {
      mapped[idxes[i]] = i;
    }

    int m = bit_width(static_cast<uint32_t>(n));
    vector<vector<int>> pa(n, vector<int>(m));
    int left = 0;
    for (int i = 0; i < n; ++i) {
      while (nums[idxes[i]] - nums[idxes[left]] > maxDiff) {
        ++left;
      }
      pa[i][0] = left;
    }

    for (int j = 1; j < m; ++j) {
      for (int i = 0; i < n; ++i) {
        pa[i][j] = pa[pa[i][j - 1]][j - 1];
      }
    }

    vector<int> ans(queries.size());
    for (int i = 0; i < queries.size(); ++i) {
      int u = mapped[queries[i][0]];
      int v = mapped[queries[i][1]];
      if (u == v) {
        ans[i] = 0;
        continue;
      }
      if (u > v) {
        swap(u, v);
      }
      int res = 0;
      for (int k = m-1; k >= 0; --k) {
        if (pa[v][k] > u) {
          res |= 1 << k;
          v = pa[v][k];
        }
      }
      ans[i] = pa[v][0] > u ? -1 : res + 1;
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
  vector<int> nums = json::parse(inputArray.at(1));
  int maxDiff = json::parse(inputArray.at(2));
  vector<vector<int>> queries = json::parse(inputArray.at(3));
  return solution.pathExistenceQueries(n, nums, maxDiff, queries);
}
