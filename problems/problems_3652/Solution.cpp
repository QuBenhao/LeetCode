//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long maxProfit(const vector<int> &prices, const vector<int> &strategy,
                      int k) {
    int n = prices.size();
    vector<int64_t> pre_sum(n + 1, 0), original_pre_sum(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      pre_sum[i + 1] = pre_sum[i] + prices[i] * strategy[i];
      original_pre_sum[i + 1] = original_pre_sum[i] + prices[i];
    }
    int64_t ans = pre_sum[n];
    for (int i = 0; i <= n - k; ++i) {
      int64_t cur = pre_sum[i] + pre_sum[n] - pre_sum[i + k];
      cur += original_pre_sum[i + k] - original_pre_sum[i + k / 2];
      ans = max(ans, cur);
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
  vector<int> prices = json::parse(inputArray.at(0));
  vector<int> strategy = json::parse(inputArray.at(1));
  int k = json::parse(inputArray.at(2));
  return solution.maxProfit(prices, strategy, k);
}
