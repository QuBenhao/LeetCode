//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long minCost(const vector<int> &basket1, const vector<int> &basket2) {
    unordered_map<int, int> count;
    int n = basket1.size();
    for (int i = 0; i < n; ++i) {
      count[basket1[i]]++;
      count[basket2[i]]--;
    }
    vector<int> nums;
    int mn = INT_MAX;
    for (const auto &[num, cnt] : count) {
      if (cnt % 2 != 0) {
        return -1;  // Impossible to balance
      }
      mn = min(mn, num);
      for (int j = 0; j < abs(cnt) / 2; ++j) {
        nums.push_back(num);
      }
    }
    ranges::nth_element(nums, nums.begin() + nums.size() / 2);
    int64_t ans = 0;
    for (int i = 0; i < nums.size() / 2; ++i) {
      ans += min(nums[i], mn * 2);
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
  vector<int> basket1 = json::parse(inputArray.at(0));
  vector<int> basket2 = json::parse(inputArray.at(1));
  return solution.minCost(basket1, basket2);
}
