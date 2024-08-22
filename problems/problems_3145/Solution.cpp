//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
  int pow(long long x, long long n, long long mod) {
    long long res = 1 % mod;
    for (; n; n /= 2) {
      if (n % 2) {
        res = res * x % mod;
      }
      x = x * x % mod;
    }
    return res;
  }

  long long sum_e(long long k) {
    long long res = 0, n = 0, cnt1 = 0, sum_i = 0;
    for (long long i = __lg(k + 1); i; i--) {
      long long c = (cnt1 << i) + (i << (i - 1)); // 新增的幂次个数
      if (c <= k) {
        k -= c;
        res += (sum_i << i) + ((i * (i - 1) / 2) << (i - 1));
        sum_i += i;    // 之前填的 1 的幂次之和
        cnt1++;        // 之前填的 1 的个数
        n |= 1LL << i; // 填 1
      }
    }
    // 最低位单独计算
    if (cnt1 <= k) {
      k -= cnt1;
      res += sum_i;
      n |= 1; // 最低位填 1
    }
    // 剩余的 k 个幂次，由 n 的低 k 个 1 补充
    while (k--) {
      res += __builtin_ctzll(n);
      n &= n - 1; // 去掉最低位的 1（置为 0）
    }
    return res;
  }

public:
  vector<int> findProductsOfElements(vector<vector<long long>> &queries) {
    vector<int> ans;
    for (auto &q : queries) {
      auto er = sum_e(q[1] + 1);
      auto el = sum_e(q[0]);
      ans.push_back(pow(2, er - el, q[2]));
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
  vector<vector<long long>> queries = json::parse(inputArray.at(0));
  return solution.findProductsOfElements(queries);
}
