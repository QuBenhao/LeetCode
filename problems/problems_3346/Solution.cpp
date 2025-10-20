//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>
#include <map>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxFrequency(const vector<int> &nums, int k, int numOperations) {
    unordered_map<int, int> counts;
    map<int, int> diff;
    for (const auto &num : nums) {
      ++counts[num];
      diff[num] += 0;
      ++diff[num - k];
      --diff[num + k + 1];
    }
    int ans = 0, sum_d = 0;
    for (const auto &[x, d] : diff) {
      sum_d += d;
      ans = max(ans, min(sum_d, counts[x] + numOperations));
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
  vector<int> nums = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  int numOperations = json::parse(inputArray.at(2));
  return solution.maxFrequency(nums, k, numOperations);
}
