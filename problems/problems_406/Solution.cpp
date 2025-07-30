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
public:
  vector<vector<int>> reconstructQueue(vector<vector<int>> &people) {
    sort(people.begin(), people.end(),
         [](const vector<int> &a, const vector<int> &b) {
           return a[0] < b[0] || (a[0] == b[0] && a[1] > b[1]);
         });
    int n = people.size();
    FenwickTree<int> fenwick(n);
    vector<vector<int>> res(n);
    for (int i = 0; i < n; ++i) {
      int l = 1, r = n;
      while (l < r) {
        int mid = (l + r) / 2;
        if (fenwick.query(1, mid) >= mid - people[i][1]) {
          l = mid + 1;
        } else {
          r = mid;
        }
      }
      res[l - 1] = people[i];
      fenwick.update(l, 1);
    }
    return res;
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
  vector<vector<int>> people = json::parse(inputArray.at(0));
  return solution.reconstructQueue(people);
}
