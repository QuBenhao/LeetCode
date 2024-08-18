//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
  static constexpr int MOD = 1'000'000'007;
  static constexpr int SIZE = 6;

  using matrix = array<array<int, SIZE>, SIZE>;

  // 返回矩阵 a 和矩阵 b 相乘的结果
  matrix mul(matrix &a, matrix &b) {
    matrix c{};
    for (int i = 0; i < SIZE; i++) {
      for (int j = 0; j < SIZE; j++) {
        for (int k = 0; k < SIZE; k++) {
          c[i][j] = (c[i][j] + (long long)a[i][k] * b[k][j]) % MOD;
        }
      }
    }
    return c;
  }

  // 返回 n 个矩阵 a 相乘的结果
  matrix pow(matrix a, int n) {
    matrix res = {};
    for (int i = 0; i < SIZE; i++) {
      res[i][i] = 1; // 单位矩阵
    }
    while (n) {
      if (n & 1) {
        res = mul(res, a);
      }
      a = mul(a, a);
      n >>= 1;
    }
    return res;
  }

public:
  int checkRecord(int n) {
    matrix m = {{
        {{1, 1, 0, 1, 0, 0}},
        {{1, 0, 1, 1, 0, 0}},
        {{1, 0, 0, 1, 0, 0}},
        {{0, 0, 0, 1, 1, 0}},
        {{0, 0, 0, 1, 0, 1}},
        {{0, 0, 0, 1, 0, 0}},
    }};
    matrix res = pow(m, n);
    int ans = 0;
    for (int x : res[0]) {
      ans = (ans + x) % MOD;
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
  return solution.checkRecord(n);
}
