//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

const int MOD = 1e9 + 7;

class Solution {
public:
  int sumSubseqWidths(vector<int> &nums) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    vector<int> pow2(n);
    pow2[0] = 1;
    for (int i = 1; i < n; ++i) {
      pow2[i] = (pow2[i - 1] * 2) % MOD;
    }
    int64_t result = 0;
    for (int i = 0; i < n; ++i) {
      result =
          (result +
           ((int64_t)(pow2[i] - pow2[n - i - 1] + MOD) % MOD * nums[i]) % MOD) %
          MOD;
    }
    return result;
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
  return solution.sumSubseqWidths(nums);
}
