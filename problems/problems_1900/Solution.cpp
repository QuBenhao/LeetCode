//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> earliestAndLatest(int n, int first, int second) {
    if (first + second == n + 1) {
      return {1, 1};
    }

    if (first + second > n + 1) {
      tie(first, second) = pair(n + 1 - second, n + 1 - first);
    }

    auto calc_earliest_rounds = [&](int n) -> int {
      int res = 1;

      if (first + second <= (n + 1) / 2) {
        // 计算满足 first+second > ceil(n / 2^(k+1)) 的最小 k，推导过程见题解
        int k = bit_width((n - 1u) / (first + second - 1)) - 1;
        n = ((n - 1) >> k) + 1;  // n = ceil(n / 2^k)
        res += k;

        if (second - first > 1) {
          return res + 1;
        }
      }

      // 情况 1 和情况 3 合并，情况 2 合并到最后的 return
      if (second - first == 1 ||
          (second > (n + 1) / 2 && second - first == 2)) {
        // 先把 n 变成 ceil(n/2)，然后计算需要多少次 ceil(n/2) 的操作才能把 n
        // 变成偶数，推导过程见题解 这里把 (n+1)/2 和 n-1 合并，得到 (n+1)/2-1 =
        // (n-1)/2
        return res + 1 + countr_zero((n - 1u) / 2);
      }

      if (second > (n + 1) / 2 && first % 2 == 0 && first + second == n) {
        res++;
      }

      return res + 1;
    };

    int earliest = calc_earliest_rounds(n);
    int latest = min(bit_width(n - 1u), n + 1 - second);
    return {earliest, latest};
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
  int firstPlayer = json::parse(inputArray.at(1));
  int secondPlayer = json::parse(inputArray.at(2));
  return solution.earliestAndLatest(n, firstPlayer, secondPlayer);
}
