//go:build ignore
#include "cpp/common/Solution.h"
#include <cstdint>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long minArraySum(const vector<int> &nums, int k) {
    vector<int64_t> mod_min(k, INT64_MAX);
    mod_min[0] = 0;
    int64_t cur = 0;
    int mod = 0;
    for (const auto &num : nums) {
      mod = (mod + num) % k;
      cur = min(cur + num, mod_min[mod]);
      mod_min[mod] = cur;
    }
    return cur;
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
  return solution.minArraySum(nums, k);
}
