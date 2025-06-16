//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

const int MOD = 1e9 + 7;

class Solution {
  int fast_pow(uint64_t base, int exp) {
    uint64_t result = 1;
    while (exp > 0) {
      if (exp % 2 == 1) {
        result = (result * base) % MOD;
      }
      base = (base * base) % MOD;
      exp /= 2;
    }
    return result;
  }

  int comb(int n, int k) {
    if (k > n)
      return 0;
    if (k == 0 || k == n)
      return 1;

    uint64_t numerator = 1;
    uint64_t denominator = 1;
    for (int i = 0; i < k; ++i) {
      numerator = (numerator * (n - i)) % MOD;
      denominator = (denominator * (i + 1)) % MOD;
    }
    return (numerator * fast_pow(denominator, MOD - 2)) % MOD;
  }

public:
  int countGoodArrays(int n, int m, int k) {
    uint64_t res = m;
    res = ((res * fast_pow(m - 1, n - k - 1)) % MOD) * comb(n - 1, k);
    return res % MOD;
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
  int m = json::parse(inputArray.at(1));
  int k = json::parse(inputArray.at(2));
  return solution.countGoodArrays(n, m, k);
}
