//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

template <typename T> class FenwickTree {
  vector<T> tree;

public:
  // 使用下标 1 到 n
  explicit FenwickTree(int n) : tree(n + 1) {}

  // a[i] 增加 val
  // 1 <= i <= n
  // 时间复杂度 O(log n)
  void update(int i, T val) {
    for (; i < tree.size(); i += i & -i) {
      tree[i] += val;
    }
  }

  // 求前缀和 a[1] + ... + a[i]
  // 1 <= i <= n
  // 时间复杂度 O(log n)
  T pre(int i) const {
    T res = 0;
    for (; i > 0; i &= i - 1) {
      res += tree[i];
    }
    return res;
  }

  // 求区间和 a[l] + ... + a[r]
  // 1 <= l <= r <= n
  // 时间复杂度 O(log n)
  T query(int l, int r) const {
    if (r < l) {
      return 0;
    }
    return pre(r) - pre(l - 1);
  }
};

class Solution {
  int popcount(int64_t x) {
    int count = 0;
    while (x > 1) {
      ++count;
      x = __builtin_popcountll(x);
    }
    return count;
  }

public:
  vector<int> popcountDepth(vector<long long> &nums,
                            const vector<vector<long long>> &queries) {
    vector<int> ans;
    int n = nums.size();
    vector<FenwickTree<int>> trees(6, FenwickTree<int>(n));
    for (int i = 0; i < n; ++i) {
      int depth = popcount(nums[i]);
      trees[depth].update(i + 1, 1);
    }
    for (const auto &query : queries) {
      if (query[0] == 1) {
        int l = query[1], r = query[2], k = query[3];
        ans.emplace_back(trees[k].query(l + 1, r + 1));
      } else {
        auto idx = query[1], val = query[2];
        int oldDepth = popcount(nums[idx]);
        int newDepth = popcount(val);
        nums[idx] = val;  // 更新原数组
        if (oldDepth != newDepth) {
          trees[oldDepth].update(idx + 1, -1);
          trees[newDepth].update(idx + 1, 1);
        }
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
  vector<long long> nums = json::parse(inputArray.at(0));
  vector<vector<long long>> queries = json::parse(inputArray.at(1));
  return solution.popcountDepth(nums, queries);
}
