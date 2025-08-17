//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

const int MOD = 1e9 + 7;

class Solution {
public:
  int xorAfterQueries(vector<int> &nums, const vector<vector<int>> &queries) {
    for (const auto &query : queries) {
      int l = query[0], r = query[1], k = query[2], v = query[3];
      for (int i = l; i <= r; i += k) {
        nums[i] = (1LL * nums[i] * v) % MOD;
      }
    }
    int ans = 0;
    for (int num : nums) {
      ans ^= num;
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
  vector<vector<int>> queries = json::parse(inputArray.at(1));
  return solution.xorAfterQueries(nums, queries);
}
