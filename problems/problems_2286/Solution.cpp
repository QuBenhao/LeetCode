//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class BookMyShow {
  int n, m;
  vector<int> mn;
  vector<int64_t> sum;

  // Increase the element at index i by val
  void update(int o, int l, int r, int i, int val) {
    if (l == r) {
      mn[o] += val;
      sum[o] += val;
      return;
    }
    int m = (l + r) / 2;
    if (i <= m) {
      update(o * 2, l, m, i, val);
    } else {
      update(o * 2 + 1, m + 1, r, i, val);
    }
    mn[o] = min(mn[o * 2], mn[o * 2 + 1]);
    sum[o] = sum[o * 2] + sum[o * 2 + 1];
  }

  // Return the sum of elements in [L,R]
  int64_t querySum(int o, int l, int r, int L, int R) {
    if (L <= l && r <= R) {
      return sum[o];
    }
    int64_t res = 0;
    int m = (l + r) / 2;
    if (L <= m) {
      res = querySum(o * 2, l, m, L, R);
    }
    if (R > m) {
      res += querySum(o * 2 + 1, m + 1, r, L, R);
    }
    return res;
  }

  // Return the leftmost position in [0,R] whose value is <= val, or -1 if none exists
  int findFirst(int o, int l, int r, int R, int val) {
    if (mn[o] > val) {
      return -1; // Every value in the interval exceeds val
    }
    if (l == r) {
      return l;
    }
    int m = (l + r) / 2;
    if (mn[o * 2] <= val) {
      return findFirst(o * 2, l, m, R, val);
    }
    if (R > m) {
      return findFirst(o * 2 + 1, m + 1, r, R, val);
    }
    return -1;
  }

public:
  BookMyShow(int n, int m) : n(n), m(m), mn(4 << __lg(n)), sum(4 << __lg(n)) {}

  vector<int> gather(int k, int maxRow) {
    // Find the first bucket that can hold k more liters of water
    int r = findFirst(1, 0, n - 1, maxRow, m - k);
    if (r < 0) { // No such bucket exists
      return {};
    }
    int c = querySum(1, 0, n - 1, r, r);
    update(1, 0, n - 1, r, k); // Pour water
    return {r, c};
  }

  bool scatter(int k, int maxRow) {
    // Total amount of water in [0,maxRow]
    int64_t s = querySum(1, 0, n - 1, 0, maxRow);
    if (s > (int64_t)m * (maxRow + 1) - k) {
      return false; // The buckets already contain too much water
    }
    // Start with the first bucket that is not full
    int i = findFirst(1, 0, n - 1, maxRow, m - 1);
    while (k) {
      int left = min(m - (int)querySum(1, 0, n - 1, i, i), k);
      update(1, 0, n - 1, i, left); // Pour water
      k -= left;
      i++;
    }
    return true;
  }
};

/**
 * Your BookMyShow object will be instantiated and called as such:
 * BookMyShow* obj = new BookMyShow(n, m);
 * vector<int> param_1 = obj->gather(k,maxRow);
 * bool param_2 = obj->scatter(k,maxRow);
 */

json leetcode::qubh::Solve(string input_json_values) {
  vector<string> inputArray;
  size_t pos = input_json_values.find('\n');
  while (pos != string::npos) {
    inputArray.push_back(input_json_values.substr(0, pos));
    input_json_values = input_json_values.substr(pos + 1);
    pos = input_json_values.find('\n');
  }
  inputArray.push_back(input_json_values);

  vector<string> operators = json::parse(inputArray[0]);
  vector<vector<json>> op_values = json::parse(inputArray[1]);
  auto obj0 = make_shared<BookMyShow>(op_values[0][0], op_values[0][1]);
  vector<json> ans = {nullptr};
  for (size_t i = 1; i < op_values.size(); i++) {
    if (operators[i] == "gather") {
      ans.push_back(obj0->gather(op_values[i][0], op_values[i][1]));
      continue;
    }
    if (operators[i] == "scatter") {
      ans.push_back(obj0->scatter(op_values[i][0], op_values[i][1]));
      continue;
    }
    ans.push_back(nullptr);
  }
  return ans;
}
